from tkinter import messagebox
import tkinter as tk
from tkcalendar import DateEntry
from sisRecomendacion import SistemaRecomendacion, Fact

generos = [
    "Zombies", "Shooter", "Action", "Survival", "Horror", "First-Person",
    "Survival Horror", "Adventure",  "Open World",
    "RPG (Role-Playing Game)"
]

categorias = [
    "Single-player", "Online PvP", "Online Co-op", 
    "Multi-player", "Co-op"
]

idiomas = [
    "English","Italian","Russian", "Simplified Chinese", "Spanish"
]

def obtener_datos():
    # Recoge los datos del formulario
    
    min_ram = ram_min.get()
    min_storage = almacenamiento_min.get()
    price_range = slider.get()
    singleplayer = singleplayer_var.get()
    online_multiplayer = online_multiplayer_var.get()
    release_date = release_date_entry.get()
    user_rating = user_rating_entry.get()
    multiplatform = multiplatform_var.get()
    achievements = achievements_var.get()
    steam_workshop = steam_workshop_var.get()
    in_app_purchases = in_app_purchases_var.get()
    active_community_market = active_community_market_var.get()
    remote_play = remote_play_var.get()
    steam_trading_cards = steam_trading_cards_var.get()
    controller_support = controller_support_var.get()
    genres = [genre for genre, var in genre_vars.items() if var.get()]
    categories = [category for category, var in category_vars.items() if var.get()]
    languages = [language for language, var in language_vars.items() if var.get()]

    sr = SistemaRecomendacion()
    sr.reset()
    recomendacion = sr.recomendarCompleto(min_ram,min_storage,price_range,genres,categories,singleplayer,online_multiplayer,release_date,user_rating,multiplatform,achievements,steam_workshop,in_app_purchases,active_community_market,remote_play,languages,steam_trading_cards,controller_support)
    sr.run()
    return recomendacion


root = tk.Tk()
root.title("Sistema de Recomendación de Juegos")
root.geometry("800x800")
root.resizable(False, False)


tk.Label(root, text="RAM mínima:").grid(row=0)
tk.Label(root, text="Almacenamiento mínimo:").grid(row=1)

tk.Label(root, text="Precio Maximo:").grid(row=2)
slider_callback = lambda event: show_value(int(slider.get()))
slider = tk.Scale(root, from_=1, to=200, orient="horizontal", command=slider_callback)
slider.grid(row=2, column=1, padx=10, pady=10)
value_label = tk.Label(root, text="")

def show_value(value):
    value_label.config(text=value)
show_value(slider.get())


genre_frame = tk.Frame(root)
genre_frame.grid(row=3, column=1, sticky="w")

category_frame = tk.Frame(root)
category_frame.grid(row=4, column=1, sticky="w")

tk.Label(root, text="¿Es para un solo jugador?:").grid(row=5)
singleplayer_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=singleplayer_var, value=True).grid(row=5, column=1)
tk.Radiobutton(root, text="No", variable=singleplayer_var, value=False).grid(row=5, column=2)

tk.Label(root, text="¿Tiene multijugador en línea?:").grid(row=6)
online_multiplayer_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=online_multiplayer_var, value=True).grid(row=6, column=1)
tk.Radiobutton(root, text="No", variable=online_multiplayer_var, value=False).grid(row=6, column=2)

tk.Label(root, text="Fecha de lanzamiento:").grid(row=7)
release_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
release_date_entry.grid(row=7, column=1)

tk.Label(root, text="Calificación minima de los usuarios:").grid(row=1, column=3)

tk.Label(root, text="¿Es multiplataforma?:").grid(row=2, column=3)
multiplatform_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=multiplatform_var, value=True).grid(row=2, column=4)
tk.Radiobutton(root, text="No", variable=multiplatform_var, value=False).grid(row=2, column=5)

tk.Label(root, text="¿Tiene logros?:").grid(row=3, column=3)
achievements_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=achievements_var, value=True).grid(row=3, column=4)
tk.Radiobutton(root, text="No", variable=achievements_var, value=False).grid(row=3, column=5)

tk.Label(root, text="¿Tiene taller de Steam?:").grid(row=4, column=3)
steam_workshop_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=steam_workshop_var, value=True).grid(row=4, column=4)
tk.Radiobutton(root, text="No", variable=steam_workshop_var, value=False).grid(row=4, column=5)

tk.Label(root, text="¿Tiene compras dentro de la aplicación?:").grid(row=5, column=3)
in_app_purchases_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=in_app_purchases_var, value=True).grid(row=5, column=4)
tk.Radiobutton(root, text="No", variable=in_app_purchases_var, value=False).grid(row=5, column=5)

tk.Label(root, text="¿Tiene mercado comunitario activo?:").grid(row=6, column=3)
active_community_market_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=active_community_market_var, value=True).grid(row=6, column=4)
tk.Radiobutton(root, text="No", variable=active_community_market_var, value=False).grid(row=6, column=5)

tk.Label(root, text="¿Tiene juego remoto?:").grid(row=7, column=3)
remote_play_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=remote_play_var, value=True).grid(row=7, column=4)
tk.Radiobutton(root, text="No", variable=remote_play_var, value=False).grid(row=7, column=5)

language_frame = tk.Frame(root)
language_frame.grid(row=8, column=4, sticky="w")

tk.Label(root, text="¿Tiene tarjetas de intercambio de Steam?:").grid(row=9, column=3)
steam_trading_cards_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=steam_trading_cards_var, value=True).grid(row=9, column=4)
tk.Radiobutton(root, text="No", variable=steam_trading_cards_var, value=False).grid(row=9, column=5)

tk.Label(root, text="¿Tiene soporte para controladores?:").grid(row=10, column=3)
controller_support_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=controller_support_var, value=True).grid(row=10, column=4)
tk.Radiobutton(root, text="No", variable=controller_support_var, value=False).grid(row=10, column=5)

ram_min = tk.Entry(root)
almacenamiento_min = tk.Entry(root)
price_range_entry = tk.Entry(root)
genres_entry = tk.Entry(root)
categories_entry = tk.Entry(root)
singleplayer_entry = tk.Entry(root)
online_multiplayer_entry = tk.Entry(root)
release_date_entry = tk.Entry(root)
user_rating_entry = tk.Entry(root)
multiplatform_entry = tk.Entry(root)
achievements_entry = tk.Entry(root)
steam_workshop_entry = tk.Entry(root)
in_app_purchases_entry = tk.Entry(root)
active_community_market_entry = tk.Entry(root)
remote_play_entry = tk.Entry(root)
languages_entry = tk.Entry(root)
steam_trading_cards_entry = tk.Entry(root)
controller_support_entry = tk.Entry(root)

ram_min.grid(row=0, column=1)
almacenamiento_min.grid(row=1, column=1)
user_rating_entry.grid(row=1, column=4)


# Create Checkbuttons for genres and insert into the frame
genre_vars = {}
for genre in generos:
    var = tk.BooleanVar()
    genre_vars[genre] = var
    cb = tk.Checkbutton(genre_frame, text=genre, variable=var, onvalue=True, offvalue=False)
    cb.pack(anchor="w")

# Create Checkbuttons for categories and insert into the frame
category_vars = {}
for category in categorias:
    var = tk.BooleanVar()
    category_vars[category] = var
    cb = tk.Checkbutton(category_frame, text=category, variable=var, onvalue=True, offvalue=False)
    cb.pack(anchor="w")

# Create Checkbuttons for languages and insert into the frame
language_vars = {}
for language in idiomas:
    var = tk.BooleanVar()
    language_vars[language] = var
    cb = tk.Checkbutton(language_frame, text=language, variable=var, onvalue=True, offvalue=False)
    cb.pack(anchor="w")

def mostrar_ventana_emergente():
    ventana_emergente = tk.Toplevel(root)
    ventana_emergente.title("Reconmendación")
    ventana_emergente.geometry("1500x200")
    ventana_emergente.resizable(False, False)
    mensaje1 = tk.Label(ventana_emergente, text="Nombre: " + obtener_datos()[0]["name"])
    mensaje1.pack(pady=1)
    mensaje2 = tk.Label(ventana_emergente, text="Precio: " + str(obtener_datos()[0]["price_range"]))
    mensaje2.pack(pady=1)
    mensaje3 = tk.Label(ventana_emergente, text="Genero: " + str(obtener_datos()[0]["genres"]))
    mensaje3.pack(pady=1)
    mensaje4 = tk.Label(ventana_emergente, text="Categoria: " + str(obtener_datos()[0]["categories"]))
    mensaje4.pack(pady=1)
    mensaje5 = tk.Label(ventana_emergente, text="Fecha de Lanzamiento: " + obtener_datos()[0]["release_date"])
    mensaje5.pack(pady=1)
    mensaje5 = tk.Label(ventana_emergente, text="Lenguajes: " + str(obtener_datos()[0]["languages"]))
    mensaje5.pack(pady=1)
    mensaje5 = tk.Label(ventana_emergente, text="Memoria Ram Minima: " + str(obtener_datos()[0]["min_ram"]) + " GB")
    mensaje5.pack(pady=1)
    boton_cerrar = tk.Button(ventana_emergente, text="Cerrar", command=ventana_emergente.destroy)
    boton_cerrar.pack()

tk.Button(root, text='Recomendar', command=mostrar_ventana_emergente).grid(row=8, columnspan=2, pady=4)



root.mainloop()




