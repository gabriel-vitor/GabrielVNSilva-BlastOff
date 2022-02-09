import ormar
from config import database, metadata

class Produto(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "produtos"

    id: int = ormar.Integer(primary_key=True)
    titulo: str = ormar.String(max_length=100)
    descricao: str = ormar.String(max_length=100)
    valor: float = ormar.Float()


