from fastapi import APIRouter

from models.produto import Produto

router = APIRouter()

# o banco de dados é feito de forma assincrona (async)
# então os metodos precisam ser assincronos

@router.post("/")
async def add_item(produto: Produto):
    await produto.save()
    return produto

@router.get("/")
async def list_item():
    return await Produto.objects.all()