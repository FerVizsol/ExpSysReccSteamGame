from sisRecomendacion import *
import tkinter as tk
from tkinter import ttk

class SistemaRecomendacionJuegoSteam:
    def __init__(self, master):
        self.master = master
        master.title("Sistema Experto de Recomendacion de Juegos de Steam")
        master.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        form_frame = ttk.Frame(self.master)
        form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.precioTag = ttk.Label(form_frame, text="Rango de Precios:")
        self.precioTag.grid(row=0, column=0, sticky="w")
        self.precioInput = ttk.Entry(form_frame)
        self.precioInput.grid(row=0, column=1)

        self.generosTag = ttk.Label(form_frame, text="Géneros:")
        self.generosTag.grid(row=1, column=0, sticky="w")
        self.generosInput = ttk.Entry(form_frame)
        self.generosInput.grid(row=1, column=1)
        self.envioBoton = ttk.Button(form_frame, text="Enviar", command=self.submit_preferences)
        self.envioBoton.grid(row=2, columnspan=2)
        self.engine = SistemaRecomendacion()

    def submit_preferences(self):
        precioRango = self.precioInput.get()
        generos = self.generosInput.get()
        self.engine.reset()
        self.engine.declare(Juego(precioRango=precioRango, generos=generos))
        self.engine.run()

root = tk.Tk()
app = SistemaRecomendacionJuegoSteam(root)
root.mainloop()

