import tkinter as tk
from views.login import Login
# armado de root
root = tk.Tk ()
root.title     ("App music Desapacito")
# armado de frame
frame = tk.Frame(root).pack()
# modificar a grid de ser necesario
# armar dos botonoes registro y logeo
boton1 = tk.Button(frame, text= "registro usuario",justify=["left"]).pack()

boton2 = tk.Button(frame, text= "Acceso  usuario",justify=["right"],command=).pack()
root.mainloop()