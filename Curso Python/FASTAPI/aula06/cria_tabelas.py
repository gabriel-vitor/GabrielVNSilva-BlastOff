from tkinter.tix import MAIN
from pip import main
import sqlalchemy

from config import DATABASE_URL, metadata
from models.papel import Papel

def configurar_banco(database_url = DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)

if __name__ == "__main__":
    configurar_banco()