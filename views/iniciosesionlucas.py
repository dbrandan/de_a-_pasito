ctk.set_appearance_mode("dark")

# COLORES
blanco = "#eee"
gris = "#444444"
cian = "#00ffff"
rosa = "#FF69B4"

class VistaInicio(ctk.CTkFrame):
    def init(self, master=None, controlador=None):
        super().init(master)
        self.master = master
        self.controlador = controlador

        # FONDO Y DISEÑO
        self.config(bg=gris)
        self.canvas = tk.Canvas(self, bg=gris, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # TITULO
        self.titulo = ctk.CTkLabel(self.canvas, text="BIENVENIDO", font=("Helvetica", 30), text_color=blanco)
        self.titulo.pack(pady=40, padx=10)

        self.linea1 = ctk.CTkLabel(self.canvas, text="___", font=("Helvetica", 30), text_color=rosa)
        self.linea1.pack(pady=10, padx=10)

        # ENTRYS
        self.nombre = ctk.CTkEntry(self.canvas, placeholder_text="Nombre...", border_color=cian, corner_radius=10)
        self.nombre.pack(pady=10, padx=10)
        self.password = ctk.CTkEntry(self.canvas, placeholder_text="Contraseña...", border_color=rosa, show="*", corner_radius=10)
        self.password.pack(pady=10, padx=10)

        # BOTONES
        def IniciarSesion(self):
            pass

        def registrarCuenta(self, label):
            pass

        enviar_icon = tk.PhotoImage(file="ruta/a/icono_enviar.png")
        self.enviar = ctk.CTkButton(self.canvas, image=enviar_icon, text="ENVIAR", compound=tk.LEFT, corner_radius=10, fg_color=cian,
                                    command=IniciarSesion)
        self.enviar.pack(pady=10, padx=10)

        registrar_icon = tk.PhotoImage(file="ruta/a/icono_registrar.png")
        self.registrar = ctk.CTkButton(self.canvas, image=registrar_icon, text="REGISTRARSE", compound=tk.LEFT, corner_radius=10, fg_color=rosa,
                                       command=lambda: registrarCuenta(self.titulo))
        self.registrar.pack(pady=10, padx=10)

        self.linea2 = ctk.CTkLabel(self.canvas, text="___", font=("Helvetica", 30), text_color=cian)
        self.linea2.pack(pady=10, padx=10)

if name == "main":
    app = VistaInicio()
    app.mainloop()