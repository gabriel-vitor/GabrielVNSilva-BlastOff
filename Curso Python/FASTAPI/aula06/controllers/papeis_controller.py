from fastapi import APIRouter

from models.papel import Papel

router = APIRouter()

# o banco de dados é feito de forma assincrona (async)
# então os metodos precisam ser assincronos

@router.post("/")
async def add_item(papel: Papel):
    await papel.save()
    return papel

@router.get("/")
async def list_item():
    return await Papel.objects.all()