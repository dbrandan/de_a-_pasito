import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "academia":
        label_status.config(text="Inicio de sesión exitoso", fg="green")
    else:
        label_status.config(text="Nombre de usuario o contraseña incorrectos", fg="red")

# Crear la ventana
ventana = tk.Tk()
ventana.title("App Music Despacito")
ventana.geometry("400x200")  # Tamaño de la ventana

# Configurar color de fondo para la ventana
ventana.configure(background="#F0F0F0")

# Configurar padding uniforme para todos los widgets
padding = 10

# Crear frame para el contenido
frame = tk.Frame(ventana, bg="white")
frame.pack(pady=padding)

# Crear etiqueta de título
label_title = tk.Label(frame, text="¡Bienvenido a App Music Despacito!", font=("Helvetica", 16), bg="white")
label_title.grid(row=0, columnspan=2, padx=padding, pady=padding)

# Crear etiqueta de nombre de usuario
label_username = tk.Label(frame, text="Nombre de usuario:", bg="white")
label_username.grid(row=1, column=0, padx=padding, pady=padding)

# Crear entrada de nombre de usuario
entry_username = tk.Entry(frame)
entry_username.grid(row=1, column=1, padx=padding, pady=padding)

# Crear etiqueta de contraseña
label_password = tk.Label(frame, text="Contraseña:", bg="white")
label_password.grid(row=2, column=0, padx=padding, pady=padding)

# Crear entrada de contraseña
entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=2, column=1, padx=padding, pady=padding)

# Crear botón de inicio de sesión
button_login = tk.Button(frame, text="Iniciar sesión", command=login, bg="blue", fg="white", font=("Helvetica", 12), width=10)
button_login.grid(row=3, column=0, padx=padding, pady=padding)

# Crear botón de registro
button_registro = tk.Button(frame, text="Registro de usuario", bg="green", fg="white", font=("Helvetica", 12), width=15)
button_registro.grid(row=3, column=1, padx=padding, pady=padding)

# Crear etiqueta de estado
label_status = tk.Label(ventana, text="", fg="red", bg="white")
label_status.pack(pady=padding)

# Iniciar el bucle de eventos
ventana.mainloop()