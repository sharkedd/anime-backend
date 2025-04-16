import graphene
from .anime.queries import AnimeQueries

class Query(
    AnimeQueries,  # Importa las consultas de anime
    graphene.ObjectType  # Clase base de Graphene para definir el esquema
):
    pass

schema = graphene.Schema(query=Query)