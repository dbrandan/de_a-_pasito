
import tkinter as tk
from tkinter import ttk
import json

# Cargar datos desde el archivo JSON o crear un diccionario vacío si no existe el archivo
try:
    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)
except FileNotFoundError:
    usuarios = {}

# Función de inicio de sesión
def login():
    global label_status
    username = entry_username.get()
    password = entry_password.get()
    if username in usuarios and usuarios[username] == password:
        label_status.config(text="Inicio de sesión exitoso", fg="green")
        show_user_interface()
    else:
        label_status.config(text="Nombre de usuario o contraseña incorrectos", fg="red")

# Función para mostrar la interfaz de usuarios
def show_user_interface():
    # Ocultar widgets de inicio de sesión y registro
    frame.pack_forget()
    button_login.pack_forget()
    button_registro.pack_forget()

    # Crear widgets para la interfaz de usuario
    label_music_title = tk.Label(ventana, text="Lista de Músicas:", font=("Helvetica", 14))
    label_music_title.pack()

    listbox_music = tk.Listbox(ventana, selectmode=tk.SINGLE, width=30)
    listbox_music.pack()

    # Ejemplo de lista de música
    songs = ["Canción 1", "Canción 2", "Canción 3"]
    for song in songs:
        listbox_music.insert(tk.END, song)

    # Botones para la reproducción de música
    button_play = ttk.Button(ventana, text="▶ Play", width=10, command=play_music, style="TPlayButton.TButton")
    button_play.pack(side=tk.LEFT, padx=10)

    button_pause = ttk.Button(ventana, text="⏸ Pause", width=10, command=pause_music, style="TPauseButton.TButton")
    button_pause.pack(side=tk.LEFT, padx=10)

    button_previous = ttk.Button(ventana, text="⏮ Anterior", width=10, command=previous_track, style="TPreviousButton.TButton")
    button_previous.pack(side=tk.LEFT, padx=10)

    button_next = ttk.Button(ventana, text="⏭ Siguiente", width=10, command=next_track, style="TNextButton.TButton")
    button_next.pack(side=tk.LEFT, padx=10)

# Función para reproducir música
def play_music():
    # Implementar lógica para reproducir música
    print("Reproduciendo música...")

# Función para pausar música
def pause_music():
    # Implementar lógica para pausar música
    print("Música en pausa.")

# Función para cambiar a la pista anterior
def previous_track():
    # Implementar lógica para cambiar a la pista anterior
    print("Pista anterior.")

# Función para cambiar a la siguiente pista
def next_track():
    # Implementar lógica para cambiar a la siguiente pista
    print("Siguiente pista.")

# Función para el registro de usuarios
def register():
    global label_status, usuarios
    username = entry_username.get()
    password = entry_password.get()

    # Verificar si el nombre de usuario ya existe
    if username in usuarios:
        label_status.config(text="Nombre de usuario ya existe", fg="red")
    else:
        # Verificar si la contraseña cumple con los requisitos (por ejemplo, longitud mínima, caracteres especiales, etc.)
        # Aquí puedes agregar tus propias reglas de validación para la contraseña
        if len(password) >= 6:
            usuarios[username] = password
            label_status.config(text="Registro exitoso", fg="green")
            # Guardar los datos actualizados en el archivo JSON
            with open("usuarios.json", "w") as file:
                json.dump(usuarios, file)
        else:
            label_status.config(text="La contraseña no cumple con los requisitos", fg="red")

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
entry_username = tk.Entry(frame, font=("Helvetica", 12))
entry_username.grid(row=1, column=1, padx=padding, pady=padding)

# Crear etiqueta de contraseña
label_password = tk.Label(frame, text="Contraseña:", bg="white")
label_password.grid(row=2, column=0, padx=padding, pady=padding)

# Crear entrada de contraseña
entry_password = tk.Entry(frame, show="*", font=("Helvetica", 12))
entry_password.grid(row=2, column=1, padx=padding, pady=padding)

# Crear botón de inicio de sesión
button_login = ttk.Button(frame, text="Iniciar sesión", command=login, style="TLoginButton.TButton")
button_login.grid(row=3, column=0, padx=padding, pady=padding)

# Crear botón de registro
button_registro = ttk.Button(frame, text="Registro de usuario", command=register, style="TRegisterButton.TButton")
button_registro.grid(row=3, column=1, padx=padding, pady=padding)

# Crear etiqueta de estado
label_status = tk.Label(ventana, text="", fg="red", bg="white")
label_status.pack(pady=padding)

# Estilo personalizado para los botones
style = ttk.Style()
style.configure("TPlayButton.TButton", foreground="white", background="red", font=("Helvetica", 12))
style.configure("TPauseButton.TButton", foreground="white", background="red", font=("Helvetica", 12))
style.configure("TPreviousButton.TButton", foreground="white", background="red", font=("Helvetica", 12))
style.configure("TNextButton.TButton", foreground="white", background="#1E90FF", font=("Helvetica", 12))  # Cambio de color a azul más oscuro
style.configure("TLoginButton.TButton", foreground="white", background="blue", font=("Helvetica", 12))
style.configure("TRegisterButton.TButton", foreground="white", background="green", font=("Helvetica", 12))

# Iniciar la aplicación
ventana.mainloop()