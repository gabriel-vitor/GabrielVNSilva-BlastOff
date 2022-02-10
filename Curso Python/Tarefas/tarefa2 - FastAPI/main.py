from fastapi import FastAPI
from models import Product, User
from mongoengine import connect
import json

app = FastAPI()
connect(db="store", host="localhost", port=27017)


@app.get("/get_all_products")
def get_all_products():
    products = json.loads(Product.objects().to_json())
    return {"products": products}


from fastapi import Path


@app.get("/get_product/{prod_id}")
def get_product(prod_id: int = Path(..., gt=0)):
    product = Product.objects.get(prod_id=prod_id)
    product_dict = {
                        "prod_id": product.prod_id,
                        "name": product.name,
                        "price": product.price,
                        "description": product.description
                    }
    
    return product_dict


from fastapi import Query
from mongoengine.queryset.visitor import Q


@app.get("/search_products")
def search_products(name: str, price: float = Query(None, gt=1)):
    products = json.loads(Product.objects.filter(Q(name__icontains=name) | Q(price=price)).to_json())
    return {"products": products}


from pydantic import BaseModel
from fastapi import Body


class NewProduct(BaseModel):
    prod_id: int
    name: str
    price: float
    description: str


@app.post("/add_product")
def add_product(product: NewProduct):
    new_product = Product(prod_id=product.prod_id,
                           name=product.name,
                           price=product.price,
                           description=product.description)

    new_product.save()
    return {"message": "Product added"}


class NewUser(BaseModel):
    username: str
    password: str


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


@app.post("/sign_up")
def sign_up(new_user: NewUser):
    user = User(username=new_user.username,
                password=get_password_hash(new_user.password))
    user.save()

    return {"message": "New user created sucessfully"}


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(username, password):
    try:
        user = json.loads(User.objects.get(username=username).to_json())
        password_check = pwd_context.verify(password, user['password'])
        return password_check
    except User.DoesNotExist:
        return False


from datetime import timedelta, datetime
from jose import jwt
from secrets import token_hex

SECRET_KEY = str(token_hex(32))
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()

    expire = datetime.utcnow() + expires_delta

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if authenticate_user(username, password):
        access_token = create_access_token(
                       data={"sub": username}, expires_delta=timedelta(minutes=30)
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")


@app.get("/")
def home(token: str = Depends(oauth2_scheme)):
    return {"token": token}