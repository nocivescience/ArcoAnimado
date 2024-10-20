import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Tkinter")

# Crear una etiqueta
label = tk.Label(root, text="¡Hola, Tkinter!")
label.pack()

# Crear un botón
button = tk.Button(root, text="Clic aquí", command=root.quit)
button.pack()

# Iniciar el bucle principal
root.mainloop()
