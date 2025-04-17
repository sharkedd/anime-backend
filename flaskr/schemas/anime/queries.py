import graphene
from .types import AnimeType
from ...services.jikan_api import buscar_anime_avanzado

# Definición de la clase de consulta
class AnimeQueries(graphene.ObjectType):

    buscar_anime = graphene.List(
        AnimeType,
        nombre=graphene.String(required=True)
    )

    busqueda_avanzada = graphene.List(
        AnimeType,
        nombre=graphene.String(),
        tipo=graphene.String(),
        estado=graphene.String(),
        min_score=graphene.Float(),
        genero=graphene.String()
    )

    en_emision = graphene.List(AnimeType)

    # Resolver: buscar_anime
    def resolve_buscar_anime(self, info, nombre):
        params = {"q": nombre}
        resultado = buscar_anime_avanzado(params)
        return resultado.get("data", [])

    # Resolver: busqueda_avanzada
    def resolve_busqueda_avanzada(self, info, nombre=None, tipo=None, estado=None, min_score=None, genero=None):
        params = {}
        if nombre: params["q"] = nombre
        if tipo: params["type"] = tipo
        if estado: params["status"] = estado
        if genero: params["genres"] = genero  # En Jikan se usa el ID de género

        resultado = buscar_anime_avanzado(params)
        return resultado.get("data", [])

    # Resolver: en_emision
    def resolve_en_emision(self, info):
        resultado = buscar_anime_avanzado({"status": "airing"})
        return resultado.get("data", [])