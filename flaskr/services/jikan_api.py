# jikan_api.py
import requests

JIKAN_API_BASE_URL = "https://api.jikan.moe/v4"


def buscar_anime_avanzado(params):
    url = f"{JIKAN_API_BASE_URL}/anime"
    
    base_params = {
        "sfw": "true",  # Solo resultados seguros
    }
    params.update(base_params)  # Actualiza los parámetros con los valores por defecto
    print(params)
    try:
        respuesta = requests.get(url, params=params)    
        respuesta.raise_for_status()
        #obtiene el nombre de los anime de la respuesta
        data = respuesta.json()
        for anime in data.get("data", []):
            print(anime.get("title"))
            print(anime.get("type"))
            print()

        return data
    except requests.RequestException as e:
        return {"error": "Error al llamar a la API de Jikan", "detalle": str(e)}
    
