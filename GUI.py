from tkinter import ttk
import tkinter as tk
from Factory import Factory
import math
class Application(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.factory = Factory()
        parent.title("Distancia entre ciudades")
        
        self.etiqueta_opcion = ttk.Label(parent, text="Elija una opción: ")
        self.etiqueta_opcion.place(x=20, y=20)
        self.combo_opcion = ttk.Combobox(
            self,
            state="readonly",
            values=["API", "CSV", "Mock"]
        )
        self.combo_opcion.place(x=120, y=20)
        self.etiqueta_pais1 = ttk.Label(parent, text="Ingrese el primer país:")
        self.etiqueta_pais1.place(x=20, y=50)
        
        self.input_pais1 = ttk.Entry(parent)
        self.input_pais1.place(x=140, y=50, width=100)
        
        self.etiqueta_ciudad1 = ttk.Label(parent, text="Ingrese la primera ciudad:")
        self.etiqueta_ciudad1.place(x=20, y=80)
        
        self.input_ciudad1 = ttk.Entry(parent)
        self.input_ciudad1.place(x=165, y=80, width=100)
        
        
        self.etiqueta_pais2 = ttk.Label(parent, text="Ingrese el segundo país:")
        self.etiqueta_pais2.place(x=20, y=110)
        
        self.input_pais2 = ttk.Entry(parent)
        self.input_pais2.place(x=152, y=110, width=100)
        
        self.etiqueta_ciudad2 = ttk.Label(parent, text="Ingrese la segunda ciudad:")
        self.etiqueta_ciudad2.place(x=20, y=140)
        
        self.input_ciudad2 = ttk.Entry(parent)
        self.input_ciudad2.place(x=165, y=140, width=100)
       
        self.etiqueta_distancia = ttk.Label(parent, text="Distancia: n/a")
        self.etiqueta_distancia.place(x=20, y=170)
        self.button = ttk.Button(
            text="Calcular Distancia",
            command=self.calculate_distance
        )
        self.button.place(x=70, y=200)
        parent.config(width=300, height=400)
        self.place(width=300, height=400)
        
    def metodo_haversine(self, lat1, lon1, lat2, lon2):
        
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        dist_lon = lon2_rad - lon1_rad
        dist_lat = lat2_rad - lat1_rad
        a = math.sin(dist_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dist_lon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        
        return 6371 * c
    
    def calculate_distance(self):
        
        pais1 = self.input_pais1.get()
        ciudad1 = self.input_ciudad1.get()
        pais2 = self.input_pais2.get()
        ciudad2 = self.input_ciudad2.get()
        
        if self.combo_opcion.current() !=-1:
            self.service = self.factory.seleccionarServicio(self.combo_opcion.current()+1)
        
        lat, long = self.service.getLatitudLongitud(ciudad1, pais1)
        lat2, long2 = self.service.getLatitudLongitud(ciudad2, pais2)
        
        distancia = self.metodo_haversine(lat, long, lat2, long2)
        self.etiqueta_distancia.config(text=f"Distancia: {distancia} km")
