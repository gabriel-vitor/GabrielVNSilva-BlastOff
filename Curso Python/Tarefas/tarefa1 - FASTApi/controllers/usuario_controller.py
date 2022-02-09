from fastapi import APIRouter

from models.usuario import Usuario

router = APIRouter()

# o banco de dados é feito de forma assincrona (async)
# então os metodos precisam ser assincronos

@router.post("/")
async def add_item(usuario: Usuario):
    await usuario.save()
    return usuario

@router.get("/")
async def list_item():
    return await Usuario.objects.all()