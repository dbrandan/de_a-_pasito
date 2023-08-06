import tkinter as tk

# armado de root
root = tk.Tk ()
root.title     ("App music Desapacito")
# armado de frame
frame = tk.Frame(root).pack()
# modificar a grid de ser necesario
# armar dos botonoes registro y logeo
boton1 = tk.Button(frame, text= "registro usuario").pack()

boton2 = tk.Button(frame, text= "Acceso  usuario").pack()
root.mainloop()