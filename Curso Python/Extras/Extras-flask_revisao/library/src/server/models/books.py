from flask_restplus import fields

from src.server.instance import server
book = server.api.model('Book', {
    'id': fields.String(description='O ID do registro'),
    'title': fields.String(required=True, min_Length=1, max_length=200, description='o titulo do livro.')
})