import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.ventana_formulario = Ventana.Tk()
        self.label_nombre = Ventana.Label(self.ventana_formulario, text="Digite el nombre: ")
        self.entry_nombre = Ventana.Entry(self.ventana_formulario)
        self.boton_enviar = Ventana.Button(self.ventana_formulario, text="Guardar Cliente", command=self.evento_click)
        self.boton_limpi = Ventana.Button(self.ventana_formulario, text="Limpiar", command=lambda: self.evento_borrar())

        self.label_nombre.pack()
        self.entry_nombre.pack()
        self.boton_enviar.pack()
        self.boton_limpi.pack()

        self.ventana_formulario.mainloop()

    def evento_click(self):
        nombre = self.entry_nombre.get()
        print(f"Nombre guardado: {nombre}")

    def evento_borrar(self):
        self.entry_nombre.delete(0, Ventana.END)

# Ejecutar la aplicación
Formulario()
