import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class RegistroVehiculos:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vehículos")
        self.vehiculos = []

        # Labels y Entrys
        self.labels_text = ["Placa", "Marca", "Color", "Tipo (Residente/Visitante)"]
        self.entries = {}
        
        for i, text in enumerate(self.labels_text):
            tk.Label(root, text=text).grid(row=i, column=0)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1)
            self.entries[text] = entry
        
        # Botones
        tk.Button(root, text="Guardar", command=lambda: self.guardar_vehiculo()).grid(row=5, column=0)
        tk.Button(root, text="Limpiar", command=lambda: self.limpiar_campos()).grid(row=5, column=1)
        tk.Button(root, text="Mostrar Registros", command=lambda: self.mostrar_registros()).grid(row=6, column=0, columnspan=2)
        
        # Label para mostrar registros
        self.label_registro = tk.Label(root, text="", fg="blue")
        self.label_registro.grid(row=7, column=0, columnspan=2)

    def guardar_vehiculo(self):
        datos = {campo: self.entries[campo].get().strip() for campo in self.labels_text}
        if "" in datos.values():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        datos["Hora de Ingreso"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.vehiculos.append(datos)
        self.limpiar_campos()
        messagebox.showinfo("Éxito", "Vehículo registrado exitosamente")

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def mostrar_registros(self):
        if not self.vehiculos:
            self.label_registro.config(text="No hay registros aún")
        else:
            registros_texto = "\n".join([f"{v['Placa']} - {v['Marca']} - {v['Color']} - {v['Tipo (Residente/Visitante)']} - {v['Hora de Ingreso']}" for v in self.vehiculos])
            self.label_registro.config(text=registros_texto)
        print(self.vehiculos)  # Mostrar en consola también

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroVehiculos(root)
    root.mainloop()
