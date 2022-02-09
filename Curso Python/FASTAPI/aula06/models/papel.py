import ormar
from config import database, metadata

class Produto(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "papeis"

    id: int = ormar.Integer(primary_key=True)
    titulo: str = ormar.String(max_length=100)
    descricao: str = ormar.String(max_length=100)
    cnpj: str = ormar.String(max_length=20)