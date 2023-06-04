from Interface import Interface
import requests

class API(Interface):
    def getLatitudLongitud(self, ciudad, pais):
        response= requests.get(f"https://nominatim.openstreetmap.org/search?q={ciudad.lower()},{pais.lower()}&format=json")
        body = response.json()
        if not body or len(body) == 0:
            return "ciudad o país no encontrado"
        latitud = float(body[0].get("lat"))
        longitud = float(body[0].get("lon"))
        return latitud, longitud
