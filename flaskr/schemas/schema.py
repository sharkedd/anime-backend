import graphene
from .anime.queries import AnimeQueries # Importa las consultas de anime
from .anime.mutations import SaveAnime  # Importa la mutación para guardar anime

class Query(
    AnimeQueries,  # Importa las consultas de anime
    graphene.ObjectType  # Clase base de Graphene para definir el esquema
):
    pass

class Mutation(graphene.ObjectType): # Clase base de Graphene para definir el esquema)
    SaveAnime = SaveAnime.Field()  # Define la mutación para guardar anime


schema = graphene.Schema(query=Query, mutation=Mutation)  # Crea el esquema de GraphQL con las consultas y mutaciones definidas