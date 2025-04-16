import graphene
from ..services.jikan_api import buscar_anime_avanzado 
# Definición del esquema de GraphQL

# Definición del tipo de fechas relevantes (Emisión y finalización)
class AiredType(graphene.ObjectType):
    from_date = graphene.String()
    to_date = graphene.String()
    string_date = graphene.String()

    def resolve_from_date(parent, info):
        return parent.get("from")
    
    def resolve_to_date(parent, info):
        return parent.get("to")
    
    def resolve_string_date(parent, info):
        return parent.get("string")
    
# Definición del tipo de anime
class AnimeType(graphene.ObjectType):
    #Información básica
    mal_id = graphene.Int() #id de MyAnimeList
    title = graphene.String() # Titulo del anime
    synopsis = graphene.String() # Sinopsis del anime
    genres = graphene.List(graphene.String) # Géneros del anime
    episodes = graphene.Int() # Número de episodios
    type = graphene.String() # Tipo de anime (TV, Movie, etc.)
    image_url = graphene.String() # URL de la imagen del anime

    # Información adicional
    aired = graphene.Field(AiredType) # Fechas de emisión
    rating = graphene.String() # Calificación del anime
    score = graphene.Float() # Puntuación del anime
    rank = graphene.Int() # Ranking del anime
    status = graphene.String() # Estado del anime (Finalizado, En emisión, etc.)
    airing = graphene.Boolean() # Si está en emisión
    trailer_url = graphene.String() # URL del tráiler

    def resolve_image_url(parent, info):
        return parent.get("images", {}).get("jpg", {}).get("image_url")
    
    def resolve_trailer_url(parent, info):
        return parent.get("trailer", {}).get("url")
    
    def resolve_genres(parent, info):
        return [genre.get("name") for genre in parent.get("genres", [])]



# Definición de la clase de consulta
class Query(graphene.ObjectType):

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

schema = graphene.Schema(query=Query)
