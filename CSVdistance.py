from Interface import *
import csv
class CSV(Interface):
    def  getLatitudLongitud(self, ciudad, pais):
        latitud = 0
        longitud = 0
        with open("worldcities.csv", encoding="utf8") as file:
            line = csv.reader(file)
            for row in line:
                if row[1] == ciudad and row[4] == pais:
                    latitud = float(row[2])
                    longitud = float(row[3])
                    return latitud, longitud
            return "ciudad o país no encontrado"
