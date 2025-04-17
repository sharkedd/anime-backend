import graphene
from ...services.jikan_api import buscar_anime_por_id
from ...models.anime_model import Anime, Aired # Importa los tipos de datos definidos en el modelo
class SaveAnime(graphene.Mutation):
    class Arguments:
        mal_id = graphene.Int(required=True) # ID de MyAnimeList, se obtendrán los datos necesarios a partir de esta

    success = graphene.Boolean() # Indica si la operación fue exitosa
    message = graphene.String() # Mensaje de respuesta

    def mutate(self, info, mal_id):
        result = buscar_anime_por_id(mal_id) # Llama a la función para buscar el anime por ID
        anime_data = result.get("data", '') # Obtiene los datos del anime de la respuesta
        print(anime_data) # Imprime el resultado de la búsqueda para depuración

        if not anime_data:
            return SaveAnime(success=False, message="Anime no encontrado") # Verifica si se encontraron datos
        
        try:
            aired_data = anime_data.get("aired", {})
            aired = Aired(
                from_date=aired_data.get("from"),
                to_date=aired_data.get("to"),
                string_date=aired_data.get("string")
            )

            anime = Anime(
                mal_id=anime_data.get("mal_id"),
                title=anime_data.get("title"),
                synopsis=anime_data.get("synopsis"),
                genres=[genre.get("name") for genre in anime_data.get("genres", [])], # Obtiene los géneros del anime
                episodes=anime_data.get("episodes"),
                type=anime_data.get("type"),
                image_url=anime_data.get("images", {}).get("jpg", {}).get("image_url"),
                aired=aired,
                rating=anime_data.get("rating"),
                score=anime_data.get("score"),
                rank=anime_data.get("rank"),
                status=anime_data.get("status"),
                airing=anime_data.get("airing"),
                trailer_url=anime_data.get("trailer", {}).get("url")
            )
            
            anime.save() # Guarda el anime en la base de datos
            return SaveAnime(success=True, message="Anime guardado exitosamente") # Retorna éxito
        except Exception as e:
            return SaveAnime(success=False, message=f"Error al guardar el anime: {str(e)}") # Maneja cualquier excepción que ocurra durante el proceso de guardado


        