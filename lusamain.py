
import tkinter as tk
import customtkinter as ctk
from models.ubicacion0 import Ubicacion
from views.iniciosesion import VistaInicio
from views.ubicacion import VistaUbicacion
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_ubicacion import ControladorUbicacion

class Aplicacion(ctk.CTk):
    def init(self):
        super().init()
        self.title("FESTIX")
        self.geometry("400x500")
        self.resizable(False, False)
        self.configure(bg="#444444")  # Color de fondo para el marco principal
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        ubicaciones = Ubicacion.from_json("data/ubicacion.json")

        controlador_inicio = ControladorInicio(self)
        controlador_ubicaciones = ControladorUbicacion(self, ubicaciones)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_ubicaciones = VistaUbicacion(self, controlador_ubicaciones)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_ubicaciones)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        # Transición suave entre cambios de vista
        self.vista_actual = self.current_frame if hasattr(self, 'current_frame') else None
        self.current_frame = frame_destino
        if self.vista_actual:
            self.vista_actual.grid_remove()
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame.tkraise()

if name == "main":
    app = Aplicacion()
    app.mainloop()
