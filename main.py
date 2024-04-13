from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry
from sisRecomendacion import SistemaRecomendacion, Fact

generos = [
    "Zombies", "Co-op", "FPS (First Person Shooter)", "Multiplayer", "Shooter",
    "Online Co-Op", "Action", "Survival", "Horror", "First-Person", "Gore",
    "Team-Based", "Moddable", "Survival Horror", "Post-apocalyptic", "Singleplayer",
    "Adventure", "Local Co-Op", "Replay Value", "Tactical", "Open World",
    "RPG (Role-Playing Game)", "Story Rich", "Atmospheric", "Mature", "Fantasy",
    "Nudity", "Choices Matter", "Great Soundtrack", "Third Person", "Medieval",
    "Action RPG", "Magic", "Dark Fantasy", "Dark", "Sandbox", "Competitive",
    "eSports", "Tactical", "PvP (Player vs Player)", "Strategy", "Military",
    "War", "Difficult", "Trading", "Realistic", "Fast-Paced", "MOBA (Multiplayer Online Battle Arena)",
    "RTS (Real-Time Strategy)", "Tower Defense", "Character Customization", "Replay Value",
    "Simulation", "Sci-fi", "Space", "Capitalism", "Extraction Shooter", "Comedy",
    "Violent", "Psychological Horror", "Farming Sim", "Pixel Graphics", "Life Sim",
    "Relaxing", "Agriculture", "Crafting", "Indie", "Building", "Casual",
    "2D", "Cute", "Dating Sim", "Fishing", "Battle Royale", "Stealth",
    "Automobile Sim", "Looter Shooter", "MMORPG (Massively Multiplayer Online Role-Playing Game)",
    "Cyberpunk", "Hero Shooter", "Loot", "Funny", "Lore-Rich", "Combat",
    "Platformer", "Physics", "Arcade", "Runner", "Racing", "3D Platformer",
    "Martial Arts", "Female Protagonist", "Fighting", "Hack and Slash", "Swordplay",
    "Anime", "Parkour", "Adventure", "Gothic", "Co-op Campaign", "Sexual Content",
    "Class-Based", "Destruction", "MMO (Massively Multiplayer Online)", "Dungeon Crawler",
    "Inventory Management"
]

categorias = [
    "Single-player", "Online PvP", "Online Co-op", "Steam Achievements", "Steam Trading Cards",
    "Steam Cloud", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV",
    "Family Sharing", "Multi-player", "Co-op", "Full Controller Support", "Cloud Gaming",
    "Cloud Gaming (NVIDIA)", "Shared/Split Screen", "LAN Co-op", "Shared/Split Screen Co-op",
    "Steam Workshop", "SteamVR Collectibles", "In-App Purchases", "Valve Anti-Cheat enabled",
    "Stats", "Includes Source SDK", "Commentary available", "Cross-Platform Multiplayer",
    "HDR rendering", "Native Steam Controller", "PvP", "Steam Leaderboards", "In-App Purchases",
    "Partial Controller Support", "DualShock Controllers (USB Only)", "DualSense Controllers (USB Only)",
    "DualSense Controllers", "Includes level editor", "Steam Input API Supported", "SteamVR Collectibles",
    "Captions available", "Steam Achievements", "Remote Play on Tablet", "Partial Controller Support",
    "Steam Trading Cards", "Cloud Gaming", "Cloud Gaming (NVIDIA)"
]

idiomas = [
    "Danish", "Dutch", "English", "Finnish", "French", "German", "Italian", "Japanese", "Korean",
    "Norwegian", "Polish", "Portuguese", "Russian", "Simplified Chinese", "Spanish", "Swedish",
    "Traditional Chinese", "Hungarian", "Turkish", "Bulgarian", "Czech", "Greek", "Portuguese",
    "Romanian", "Spanish - Latin America", "Thai", "Ukrainian", "Vietnamese"
]

def obtener_datos():
    # Recoge los datos del formulario
    min_ram = ram_min.get()
    min_storage = almacenamiento_min.get()
    price_range = price_range_entry.get()
    genres = genres_entry.get()
    categories = categories_entry.get()
    singleplayer = singleplayer_entry.get()
    online_multiplayer = online_multiplayer_entry.get()
    release_date = release_date_entry.get()
    user_rating = user_rating_entry.get()
    multiplatform = multiplatform_entry.get()
    achievements = achievements_entry.get()
    steam_workshop = steam_workshop_entry.get()
    in_app_purchases = in_app_purchases_entry.get()
    active_community_market = active_community_market_entry.get()
    remote_play = remote_play_entry.get()
    languages = languages_entry.get()
    steam_trading_cards = steam_trading_cards_entry.get()
    controller_support = controller_support_entry.get()

    # Crea una instancia de tu sistema de recomendación
    sr = SistemaRecomendacion()
    sr.reset()  # Reinicia el motor de inferencia
    sr.declare(Fact(min_ram=min_ram,min_storage=min_storage,price_range=price_range,genres=genres,categories=categories,singleplayer=singleplayer,
               online_multiplayer=online_multiplayer,
               release_date=release_date,user_rating=user_rating,
               multiplatform=multiplatform,achievements=achievements,
               steam_workshop=steam_workshop,in_app_purchases=in_app_purchases,
               active_community_market=active_community_market, remote_play=remote_play,
               languages=languages,steam_trading_cards=steam_trading_cards,
               controller_support=controller_support))  # Declara los hechos
    sr.run()  # Ejecuta el motor de inferencia

    recomendaciones = sr.recommendBySpecsPriceGenresCategoriesSingpMultpReleaseDateUserRateMultPlatAchievementsWorkShopAppPurchasesRemote_playLanguagesTrading(
        min_ram, min_storage, price_range, genres, categories, singleplayer, online_multiplayer, release_date,
        user_rating, multiplatform, achievements, steam_workshop, in_app_purchases, active_community_market,
        remote_play, languages, steam_trading_cards, controller_support)

    # Muestra las recomendaciones
    print(recomendaciones)

root = tk.Tk()
root.title("Sistema de Recomendación de Juegos")
root.geometry("800x770")
root.resizable(False, False)

# Crear campos del formulario
tk.Label(root, text="RAM mínima:").grid(row=0)
tk.Label(root, text="Almacenamiento mínimo:").grid(row=1)

tk.Label(root, text="Precio Minimo:").grid(row=2)
slider_callback = lambda event: show_value(int(slider.get()))
slider = tk.Scale(root, from_=1, to=200, orient="horizontal", command=slider_callback)
slider.grid(row=2, column=1, padx=10, pady=10)
value_label = tk.Label(root, text="")

def show_value(value):
    value_label.config(text=value)
show_value(slider.get())

tk.Label(root, text="Géneros:").grid(row=3)
combo_generos = tk.Listbox(root, selectmode='multiple', height=10)
combo_generos.grid(row=3, column=1)
for genero in generos:
    combo_generos.insert(tk.END, genero)

tk.Label(root, text="Categorías:").grid(row=4)
lb = tk.Listbox(root, selectmode=tk.MULTIPLE)
for categoria in categorias:
    lb.insert(tk.END, categoria)
lb.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)

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

tk.Label(root, text="Calificación de los usuarios:").grid(row=1, column=3)

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

tk.Label(root, text="Idiomas:").grid(row=8, column=3)
lb = tk.Listbox(root, selectmode=tk.MULTIPLE)
for idioma in idiomas:
    lb.insert(tk.END, idioma)
lb.grid(row=8, column=4, sticky=tk.W, padx=10, pady=5)

tk.Label(root, text="¿Tiene tarjetas de intercambio de Steam?:").grid(row=9, column=3)
steam_trading_cards_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=steam_trading_cards_var, value=True).grid(row=9, column=4)
tk.Radiobutton(root, text="No", variable=steam_trading_cards_var, value=False).grid(row=9, column=5)

tk.Label(root, text="¿Tiene soporte para controladores?:").grid(row=10, column=3)
controller_support_var = tk.BooleanVar()
tk.Radiobutton(root, text="Sí", variable=controller_support_var, value=True).grid(row=10, column=4)
tk.Radiobutton(root, text="No", variable=controller_support_var, value=False).grid(row=10, column=5)

# Crear entradas para cada campo
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

# Posicionar las entradas en la grilla
ram_min.grid(row=0, column=1)
almacenamiento_min.grid(row=1, column=1)
user_rating_entry.grid(row=1, column=4)

tk.Button(root, text='Recomendar', command=obtener_datos).grid(row=8, columnspan=2, pady=4)
root.mainloop()




