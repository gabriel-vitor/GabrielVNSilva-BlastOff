import ormar
from config import database, metadata

class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "usuarios"

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=20)
    cpf: str = ormar.String(max_length=14)
    pagamento: str = ormar.String(max_length=100)
