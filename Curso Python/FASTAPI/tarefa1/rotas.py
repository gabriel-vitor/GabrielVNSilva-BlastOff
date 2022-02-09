from fastapi import APIRouter

from controllers import produto_controller as produtos
from controllers import usuario_controller as usuarios

router = APIRouter()

router.include_router(produtos.router, prefix='/produtos')
router.include_router(usuarios.router, prefix='/usuarios')