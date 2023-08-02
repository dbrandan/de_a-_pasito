import tkinter as tk
import customtkinter as ctk
#import pygame
import os
import json

ctk.set_appearance_mode("dark")

blanco = "#eee"
gris = "#444444"
cian = "#00ffff"
rosa = "#FF69B4"

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reproductor de Música")
        self.geometry("400x400")
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.logged_in = False  # Variable para verificar si el usuario ha iniciado sesión

        # Cargar el estado de inicio de sesión al iniciar la aplicación
        self.load_session()

        self.create_widgets()

    def create_widgets(self):
        if not self.logged_in:
            # Formulario de Registro
            self.label_register = tk.Label(self, text="Registro", font=("Helvetica", 16))
            self.label_register.pack(pady=10)

            self.label_username = tk.Label(self, text="Nombre de usuario:")
            self.label_username.pack()
            self.entry_username = tk.Entry(self)
            self.entry_username.pack(pady=5)

            self.label_password = tk.Label(self, text="Contraseña:")
            self.label_password.pack()
            self.entry_password = tk.Entry(self, show="*")
            self.entry_password.pack(pady=5)

            self.btn_register = tk.Button(self, text="Registrarse", command=self.register)
            self.btn_register.pack(pady=10)

            self.btn_login = tk.Button(self, text="Iniciar Sesión", command=self.login)
            self.btn_login.pack(pady=5)

            self.label_login_status = tk.Label(self, text="")
            self.label_login_status.pack(pady=5)

        else:
            # Mostrar mensaje de inicio de sesión exitoso si ya se ha iniciado sesión
            self.label_login_status = tk.Label(self, text="Sesión iniciada como " + self.current_user["username"])
            self.label_login_status.pack(pady=10)

        # agregar los widgets para cargar y reproducir pistas de música

    def validate_password(self, password):
        # Implementar lógica para validar la contraseña
        pass

    def register(self):
        # Implementar lógica para el registro
        pass

    def login(self):
        # Implementar lógica de inicio de sesión aquí
        # Mostrar una ventana de inicio de sesión para que el usuario ingrese sus credenciales
        # verificar si las credenciales son correctas comparándolas con las almacenadas en el archivo JSON o base de datos
        # Si las credenciales son correctas, establece self.logged_in en True y muestra un mensaje de bienvenida
        # Si las credenciales no son correctas, muestra un mensaje de error de inicio de sesión
        # Finalmente, si el inicio de sesión fue exitoso, actualiza la interfaz para mostrar las opciones para cargar y reproducir música
        pass

    def save_session(self):
        # Implementar lógica para guardar el estado de inicio de sesión en un archivo JSON
        pass

    def load_session(self):
        # Implementar lógica para cargar el estado de inicio de sesión desde un archivo JSON
        pass

    def on_closing(self):
        # Implementar lógica para preguntar antes de cerrar la aplicación
        # Por ejemplo, si el usuario ha iniciado sesión y desea cerrar la aplicación, muestra un mensaje de confirmación antes de cerrarla
        pass

    # ... otros métodos para cargar y reproducir pistas de música ...

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()