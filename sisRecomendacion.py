from experta import * 
import datetime
class Juego(Fact):
    pass


class SistemaRecomendacion(KnowledgeEngine):
    @DefFacts()
    def baseDatosJuegos(self):
        
        yield Juego(name="Left 4 Dead 2", price_range=23.00,
        genres=["Zombies", "Co-op", "FPS", "Multiplayer", "Shooter", "Online Co-Op", "Action", "Survival", "Horror", "First-Person", "Gore", "Team-Based", "Moddable", "Survival Horror", "Post-apocalyptic", "Singleplayer", "Adventure", "Local Co-Op", "Replay Value", "Tactical"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Achievements", "Steam Trading Cards", "Captions available", "Steam Workshop", "Steam Cloud", "Valve Anti-Cheat enabled", "Stats", "Includes Source SDK", "Commentary available", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV", "Remote Play Together", "Family Sharing", "Co-op", "Multi-player", "HDR rendering", "Full Controller Support", "Native Steam Controller", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2009-11-17", user_rating=9.6, multiplatform=False, achievements=True, steam_workshop=True, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["Danish", "Dutch", "English", "Finnish", "French", "German", "Italian", "Japanese", "Korean", "Norwegian", "Polish", "Portuguese - Portugal", "Russian", "Simplified Chinese", "Spanish - Spain", "Swedish", "Traditional Chinese", "Hungarian", "Turkish", "Bulgarian", "Czech", "Greek", "Portuguese - Brazil", "Romanian", "Spanish - Latin America", "Thai", "Ukrainian", "Vietnamese"],
        steam_trading_cards=True, min_ram=2, min_storage=13, controller_support=True)

        yield Juego(name="The Witcher 3", price_range=96.00,
        genres=["Open World", "RPG", "Story Rich", "Atmospheric", "Mature", "Fantasy", "Adventure", "Singleplayer", "Nudity", "Choices Matter", "Great Soundtrack", "Third Person", "Medieval", "Action", "Multiple Endings", "Action RPG", "Magic", "Dark Fantasy", "Dark", "Sandbox"],
        categories=["Single-player", "Steam Achievements", "Steam Trading Cards", "Steam Cloud", "Remote Play on Tablet", "Remote Play on TV", "Family Sharing", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Partial Controller Support"],
        singleplayer=True, online_multiplayer=False, release_date="2015-05-18", user_rating=9.5, multiplatform=True, achievements=True, steam_workshop=True, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Arabic", "Czech", "Hungarian", "Japanese", "Korean", "Polish", "Portuguese - Brazil", "Russian", "Traditional Chinese", "Turkish", "Simplified Chinese", "Portuguese - Portugal"],
        steam_trading_cards=True, min_ram=6, min_storage=50, controller_support=True)

        yield Juego(name="Counter-Strike", price_range=0.0, 
        genres=["FPS", "Shooter", "Multiplayer", "Competitive", "Action", "Team-Based", "eSports", "Tactical", "First-Person", "PvP", "Online Co-Op", "Co-op", "Strategy", "Military", "War", "Difficult", "Trading", "Realistic", "Fast-Paced", "Moddable"],
        categories=["Cross-Platform Multiplayer", "Steam Trading Cards", "Steam Workshop", "In-App Purchases", "Valve Anti-Cheat enabled", "Stats", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV", "Multi-player", "Native Steam Controller", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=False, online_multiplayer=True, release_date="2012-08-21", user_rating=8.7, multiplatform=True, achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "German", "French", "Italian", "Korean", "Spanish - Spain", "Simplified Chinese", "Traditional Chinese", "Russian", "Thai", "Japanese", "Portuguese - Portugal", "Polish", "Danish", "Dutch", "Finnish", "Norwegian", "Swedish", "Hungarian", "Czech", "Romanian", "Turkish", "Portuguese - Brazil", "Bulgarian", "Greek", "Ukrainian", "Spanish - Latin America", "Vietnamese"],
        steam_trading_cards=True, min_ram=8, min_storage=85, controller_support=False)

        yield Juego(name="Dota 2", price_range=0.0,
        genres=["Free to Play", "MOBA", "Multiplayer", "Strategy", "eSports", "Team-Based", "Competitive", "Action", "Online Co-Op", "PvP", "Difficult", "Co-op", "RTS", "RPG", "Tower Defense", "Fantasy", "Character Customization", "Replay Value", "Action RPG", "Simulation"],
        categories=["Steam Trading Cards", "Steam Workshop", "SteamVR Collectibles", "In-App Purchases", "Valve Anti-Cheat enabled", "Multi-player", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2013-07-9", user_rating=8.1, multiplatform=True, achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["Portuguese - Brazil", "Bulgarian", "Czech", "Danish", "Dutch", "Finnish", "French", "German", "Greek", "Hungarian", "Italian", "Japanese", "Korean", "Spanish - Latin America", "Norwegian", "Polish", "Portuguese - Portugal", "Romanian", "Russian", "Simplified Chinese", "Spanish - Spain", "Swedish", "Traditional Chinese", "Thai", "Turkish", "Ukrainian", "Vietnamese"],
        steam_trading_cards=True, min_ram=4, min_storage=60, controller_support=False)

        yield Juego(name="HELLDIVERS™ 2", price_range=139,
        genres=["Online Co-Op", "Action", "Third-Person Shooter", "Multiplayer", "Shooter", "Co-op", "PvE", "Sci-fi", "Space", "Third Person", "Capitalism", "Extraction Shooter", "Comedy", "Gore", "Violent", "Difficult", "Great Soundtrack", "Psychological Horror", "Singleplayer", "Open World"],
        categories=["Online Co-op", "Steam Achievements", "In-App Purchases", "Family Sharing", "Multi-player", "Co-op", "Partial Controller Support", "DualShock Controllers (USB Only)", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=True, online_multiplayer=True, release_date="2024-02-8", user_rating=8.4, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["German", "French", "Italian", "Spanish - Spain", "Simplified Chinese", "Traditional Chinese", "Russian", "Japanese", "Portuguese - Portugal", "Polish", "Portuguese - Brazil", "Spanish - Latin America", "Korean"],
        steam_trading_cards=True, min_ram=8, min_storage=100, controller_support=True)

        yield Juego(name="Stardew Valley", price_range=39.95,
        genres=["Farming Sim", "Pixel Graphics", "Life Sim", "Multiplayer", "RPG", "Relaxing", "Agriculture", "Simulation", "Crafting", "Sandbox", "Indie", "Building", "Singleplayer", "Casual", "Open World", "2D", "Cute", "Dating Sim", "Great Soundtrack", "Fishing"],
        categories=["Single-player", "Online Co-op", "LAN Co-op", "Shared/Split Screen Co-op", "Steam Achievements", "Steam Trading Cards", "Steam Cloud", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play Together", "Family Sharing", "Multi-player", "Co-op", "Full Controller Support", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Shared/Split Screen"],
        singleplayer=True, online_multiplayer=True, release_date="2016-02-26", user_rating=9.7, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "German", "Spanish - Spain", "Japanese", "Portuguese - Brazil", "Russian", "Simplified Chinese", "French", "Italian", "Hungarian", "Korean", "Turkish"],
        steam_trading_cards=True, min_ram=2, min_storage=0.5, controller_support=True)
        
        yield Juego(name="PUBG: BATTLEGROUNDS", price_range=0.0,
        genres=["Survival", "Shooter", "Battle Royale", "Multiplayer", "FPS", "PvP", "Third-Person Shooter", "Action", "Online Co-Op", "Tactical", "Co-op", "First-Person", "Strategy", "Early Access", "Competitive", "Third Person", "Team-Based", "Difficult", "Simulation", "Stealth"],
        categories=["Online PvP", "Stats", "Remote Play on Phone", "Remote Play on Tablet", "Multi-player", "PvP"],
        singleplayer=True, online_multiplayer=True, release_date="2017-12-21", user_rating=5.8, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "Korean", "Simplified Chinese", "French", "German", "Spanish - Spain", "Arabic", "Japanese", "Polish", "Portuguese - Portugal", "Russian", "Turkish", "Thai", "Italian", "Portuguese - Brazil", "Traditional Chinese", "Ukrainian"],
        steam_trading_cards=True, min_ram=8, min_storage=40, controller_support=True)
                
        yield Juego(name="Call of Duty®", price_range=0.0,
        genres=["FPS", "Multiplayer", "Shooter", "Action", "Singleplayer", "Military", "First-Person", "War", "Modern", "Tactical", "Violent", "Co-op", "Realistic", "Story Rich", "Atmospheric", "Mature", "Online Co-Op", "Gore", "Third-Person Shooter", "Third Person"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Cross-Platform Multiplayer", "Steam Achievements", "Captions available", "In-App Purchases", "Full Controller Support", "Multi-player", "PvP", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2022-10-26", user_rating=5.8, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Korean", "Polish", "Russian", "Traditional Chinese", "Japanese", "Spanish - Latin America", "Arabic", "Simplified Chinese", "Portuguese - Brazil", "Thai", "Portuguese - Portugal"],
        steam_trading_cards=True, min_ram=8, min_storage=149, controller_support=True)

        yield Juego(name="Tom Clancy's Rainbow Six Siege", price_range=75.00,
        genres=["FPS", "PvP", "eSports", "Multiplayer", "Tactical", "Shooter", "Competitive", "Online Co-Op", "Action", "Hero Shooter", "Team-Based", "Military", "Strategy", "War", "First-Person", "Realistic", "Co-op", "Destruction", "Difficult", "3D"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Trading Cards", "In-App Purchases", "Remote Play on Phone", "Remote Play on Tablet", "Multi-player", "Co-op", "Native Steam Controller", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Full Controller Support", "DualShock Controllers (USB Only)", "DualShock Controllers", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=False, online_multiplayer=True, release_date="2015-12-01", user_rating=8.5, multiplatform=False, achievements=False, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Czech", "Dutch", "Japanese", "Korean", "Polish", "Portuguese - Brazil", "Russian", "Traditional Chinese", "Simplified Chinese", "Turkish", "Thai"],
        steam_trading_cards=True, min_ram=6, min_storage=61, controller_support=False)

        yield Juego(name="Apex Legends", price_range=0.0,
        genres=["Free to Play", "Battle Royale", "Multiplayer", "FPS", "Shooter", "First-Person", "PvP", "Action", "Team-Based", "Hero Shooter", "Tactical", "Sci-fi", "Survival", "Loot", "Character Customization", "Funny", "Co-op", "Lore-Rich", "Cyberpunk", "Cinematic"],
        categories=["Online PvP", "Online Co-op", "Steam Achievements", "Steam Trading Cards", "In-App Purchases", "Multi-player", "Full Controller Support", "Co-op", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "DualShock Controllers (USB Only)", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=False, online_multiplayer=True, release_date="2020-11-05", user_rating=7.8, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Japanese", "Korean", "Polish", "Portuguese - Brazil", "Russian", "Simplified Chinese", "Traditional Chinese", "Spanish - Latin America", "Arabic"],
        steam_trading_cards=True, min_ram=6, min_storage=75, controller_support=True)

        yield Juego(name="Baldur's Gate 3", price_range=199.00,
        genres=["RPG", "Choices Matter", "Character Customization", "Story Rich", "Turn-Based Combat", "Dungeons & Dragons", "Adventure", "CRPG", "Fantasy", "Online Co-Op", "Romance", "Multiplayer", "Strategy", "Singleplayer", "Co-op Campaign", "Sexual Content", "Class-Based", "Dark Fantasy", "Combat", "Controller"],
        categories=["Single-player", "Online Co-op", "LAN Co-op", "Steam Achievements", "Steam Cloud", "Family Sharing", "Multi-player", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Full Controller Support", "DualShock Controllers (USB Only)", "DualShock Controllers", "DualSense Controllers (USB Only)", "DualSense Controllers", "Steam Input API Supported"],
        singleplayer=True, online_multiplayer=True, release_date="2023-08-03", user_rating=9.6, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "French", "German", "Spanish - Spain", "Polish", "Russian", "Simplified Chinese", "Turkish", "Portuguese - Brazil", "Italian", "Spanish - Latin America", "Traditional Chinese", "Ukrainian", "Korean", "Japanese"],
        steam_trading_cards=True, min_ram=8, min_storage=150, controller_support=False)

        yield Juego(name="Team Fortress 2", price_range=0.0,
        genres=["Free to Play", "Hero Shooter", "Multiplayer", "FPS", "Shooter", "Action", "Class-Based", "Team-Based", "Funny", "First-Person", "Online Co-Op", "Competitive", "Cartoony", "Trading", "Co-op", "Comedy", "Robots", "Tactical", "Cartoon", "Crafting"],
        categories=["Cross-Platform Multiplayer", "Steam Achievements", "Steam Trading Cards", "Captions available", "Steam Workshop", "In-App Purchases", "Valve Anti-Cheat enabled", "Stats", "Includes level editor", "Commentary available", "Remote Play on Phone", "Remote Play on Tablet", "HDR rendering", "Partial Controller Support", "Multi-player", "Native Steam Controller", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=False, online_multiplayer=True, release_date="2007-10-10", user_rating=9.3, multiplatform=False, achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "Danish", "Dutch", "Finnish", "French", "German", "Italian", "Japanese", "Norwegian", "Polish", "Portuguese - Portugal", "Russian", "Simplified Chinese", "Spanish - Spain", "Swedish", "Traditional Chinese", "Korean", "Czech", "Hungarian", "Portuguese - Brazil", "Turkish", "Greek", "Bulgarian", "Romanian", "Thai", "Ukrainian"],
        steam_trading_cards=True, min_ram=0.5, min_storage=15, controller_support=False)

        yield Juego(name="Rust", price_range=79.00,
        genres=["Survival", "Crafting", "Multiplayer", "Open World", "Open World Survival Craft", "Building", "PvP", "Sandbox", "Adventure", "First-Person", "Action", "Nudity", "FPS", "Shooter", "Co-op", "Online Co-Op", "Indie", "Early Access", "Post-apocalyptic", "Simulation"],
        categories=["MMO", "Online PvP", "Online Co-op", "Cross-Platform Multiplayer", "Steam Achievements", "Steam Trading Cards", "Steam Workshop", "In-App Purchases", "Valve Anti-Cheat enabled", "Stats", "Remote Play on Tablet", "Multi-player", "Co-op", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=False, online_multiplayer=True, release_date="2018-02-08", user_rating=8.6, multiplatform=False, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Japanese", "Korean", "Russian", "Simplified Chinese", "Ukrainian", "Polish", "Portuguese - Portugal", "Turkish", "Arabic", "Czech", "Danish", "Dutch", "Finnish", "Greek", "Norwegian", "Portuguese - Brazil", "Spanish - Latin America", "Swedish", "Traditional Chinese", "Vietnamese"],
        steam_trading_cards=True, min_ram=10, min_storage=25, controller_support=True)

        yield Juego(name="Grand Theft Auto V", price_range=150.0,
        genres=["Open World", "Action", "Multiplayer", "Crime", "Automobile Sim", "Third Person", "First-Person", "Mature", "Shooter", "Adventure", "Singleplayer", "Third-Person Shooter", "Racing", "Co-op", "Sandbox", "Atmospheric", "Funny", "Great Soundtrack", "Comedy", "Moddable"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Achievements", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV", "Multi-player", "Full Controller Support", "PvP", "Co-op"],
        singleplayer=False, online_multiplayer=True, release_date="2015-04-13", user_rating=8.6, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Korean", "Polish", "Portuguese - Brazil", "Russian", "Traditional Chinese", "Japanese", "Simplified Chinese", "Spanish - Latin America"],
        steam_trading_cards=True, min_ram=4, min_storage=110, controller_support=True)

        yield Juego(name="Crab Game", price_range=0.0,
        genres=["Psychological Horror", "Multiplayer", "Free to Play", "Battle Royale", "PvP", "Action", "First-Person", "Parkour", "3D", "Nudity", "FPS", "Platformer", "Physics", "Arcade", "Combat", "Casual", "Runner", "Racing", "3D Platformer", "Sci-fi"],
        categories=["Online PvP", "Online Co-op", "Multi-player", "PvP", "Co-op"],
        singleplayer=False, online_multiplayer=True, release_date="2021-10-28", user_rating=9.1, multiplatform=False, achievements=False, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English"],
        steam_trading_cards=True, min_ram=2, min_storage=0.2, controller_support=False)

        yield Juego(name="NARAKA: BLADEPOINT", price_range=0.0,
        genres=["Battle Royale", "Multiplayer", "Martial Arts", "PvP", "Action", "Female Protagonist", "Fighting", "Massively Multiplayer", "Third Person", "Survival", "Character Customization", "Hack and Slash", "Swordplay", "Anime", "Parkour", "Adventure", "Mature", "Free to Play", "Violent", "Gore"],
        categories=["Online PvP", "In-App Purchases", "Multi-player", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Partial Controller Support"],
        singleplayer=False, online_multiplayer=True, release_date="2021-05-12", user_rating=6.9, multiplatform=False, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "Simplified Chinese", "Traditional Chinese", "Japanese", "Korean", "French", "German", "Spanish - Spain", "Russian", "Turkish", "Portuguese - Portugal", "Vietnamese", "Thai", "Arabic", "Portuguese - Brazil", "Spanish - Latin America"],
        steam_trading_cards=True, min_ram=8, min_storage=35, controller_support=True)
    #1
    @Rule(Fact(price_range=MATCH.price_range))
    def recommendPrecio(self, price_range):
        juegos_recomendados = []
        for juego in self.baseDatosJuegos():
            if juego["price_range"] <= price_range:
                juegos_recomendados.append(juego["name"])
        if juegos_recomendados:
            print("Te recomendamos los siguientes juegos dentro del rango de precio de S/.{}:".format(price_range))
            for juego in juegos_recomendados:
                print("-", juego)
        else:
            print("Lo siento, no hay juegos disponibles dentro del rango de precio de S/.{}".format(price_range))
    #2
    @Rule(Fact(genres=MATCH.genres))
    def recommend_games_by_genre(self, genres):
        juegos_recomendados = []
        for juego in self.baseDatosJuegos():
            for genre in juego["genres"]:
                if genre in genres:
                    juegos_recomendados.append(juego["name"])
                    break  
        if juegos_recomendados:
            print("Te recomendamos los siguientes juegos con los géneros {}:".format(genres))
            for juego in juegos_recomendados:
                print("-", juego)
        else:
            print("Lo siento, no hay juegos disponibles con los géneros {}".format(genres))
    @Rule(Fact(languages=MATCH.languages))
    def recommend_games_by_language(self, languages):
        juegos_recomendados = []
        for juego in self.baseDatosJuegos():
            for language in juego["languages"]:
                if language in languages:
                    juegos_recomendados.append(juego["name"])
                    break  
        if juegos_recomendados:
            print("Te recomendamos los siguientes juegos con los idiomas {}:".format(languages))
            for juego in juegos_recomendados:
                print("-", juego)
        else:
            print("Lo siento, no hay juegos disponibles con los idiomas {}".format(languages))
    #3
    
    @Rule(Fact(singleplayer=MATCH.singleplayer))
    def recommend_games_by_singp(self,singleplayer):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["singleplayer"] == singleplayer:
                juegos.append(juego["name"])
        if juegos:
            if(singleplayer):
                print("Te recomendamos los siguientes juegos con tag Singleplayer:")
            else:
                print("Te recomendamos los siguientes juegos sin tag Singleplayer:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con el tag Singleplayer")
    
    #4
    @Rule(Fact(online_multiplayer=MATCH.online_multiplayer))
    def recommend_games_by_mult(self,online_multiplayer):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["online_multiplayer"] == online_multiplayer:
                juegos.append(juego["name"])
        if juegos:
            if (online_multiplayer):
                print("Te recomendamos los siguientes juegos con tag Multiplayer Online:")
            else:
                print("Te recomendamos los siguientes juegos sin tag Multiplayer Online:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con el tag Multiplayer Online")
    #5
    @Rule(Fact(release_date=MATCH.release_date))
    def recommendRelease(self,release_date):
        recomendados =[]
        lista = str(release_date).split('-')
        fecha = datetime.date(int(lista[0]),int(lista[1]),int(lista[2]))
        for juego in self.baseDatosJuegos():
            lista1 = str(juego["release_date"]).split('-')
            fechaRelease = datetime.date(int(lista1[0]),int(lista1[1]),int(lista1[2]))
            if (fechaRelease > fecha):
                recomendados.append(juego["name"])
        if (recomendados):
            print(f"Te recomendamos los siguientes juegos que salieron despues del: {fecha}")
            for juego in recomendados:
                print("-",juego)
        else:
            print("No hay juegos que hayan salido en una fecha mayor a la ingresada")
    #6
    @Rule(Fact(user_rating=MATCH.user_rating))
    def recommendByMinRating(self,user_rating):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["user_rating"] > user_rating:
                juegos.append(juego["name"])
        if juegos:
            print(f"Estos son los juegos con rating mayor a {user_rating}")
            for juego in juegos:
                print("-",juego)
        else:
            print(f"No existen juegos con mayor rating a {user_rating}")
    #7
    @Rule(Fact(multiplatform=MATCH.multiplatform))
    def recommend_games_by_multplat(self,multiplatform):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["multiplatform"] == multiplatform:
                juegos.append(juego["name"])
        if juegos:
            if(multiplatform):
                print("Te recomendamos los siguientes juegos con tag MultiPlataforma:")
            else:
                print("Te recomendamos los siguientes juegos sin tag MultiPlataforma:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con el tag MultiPlataforma")
    #8
    @Rule(Fact(achievements=MATCH.achievements))
    def recommend_games_by_achievements(self,achievements):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["achievements"] == achievements:
                juegos.append(juego["name"])
        if juegos:
            if(achievements):
                print("Te recomendamos los siguientes juegos con Logros Desbloqueables:")
            else:
                print("Te recomendamos los siguientes juegos sin Logros Desbloqueables:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con el Logros Desbloqueables")
    #9
    @Rule(Fact(steam_workshop=MATCH.steam_workshop))
    def recommend_games_by_workshop(self,steam_workshop):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["steam_workshop"] == steam_workshop:
                juegos.append(juego["name"])
        if juegos:
            if(steam_workshop):
                print("Te recomendamos los siguientes juegos con Workshop de Steam:")
            else:
                print("Te recomendamos los siguientes juegos sin Workshop de Steam:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con el Workshop de Steam")
    #10
    @Rule(Fact(in_app_purchases=MATCH.in_app_purchases))
    def recommend_games_by_inappPurchases(self,in_app_purchases):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["in_app_purchases"] == in_app_purchases:
                juegos.append(juego["name"])
        if juegos:
            if(in_app_purchases):
                print("Te recomendamos los siguientes juegos con Compras Integradas dentro del Juego:")
            else:
                print("Te recomendamos los siguientes juegos sin Compras Integradas dentro del Juego:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con Compras Integradas dentro del Juego:")
    #11
    @Rule(Fact(active_community_market=MATCH.active_community_market))
    def recommend_games_by_comMarket(self,active_community_market):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["active_community_market"] == active_community_market:
                juegos.append(juego["name"])
        if juegos:
            if(active_community_market):
                print("Te recomendamos los siguientes juegos con Mercado de la comunidad de Steam:")
            else:
                print("Te recomendamos los siguientes juegos sin Mercado de la comunidad de Steam:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con Mercado de la comunidad de Steam:")
    #12
    @Rule(Fact(remote_play=MATCH.remote_play))
    def recommend_games_by_remotePlay(self,remote_play):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["remote_play"] == remote_play:
                juegos.append(juego["name"])
        if juegos:
            if(remote_play):
                print("Te recomendamos los siguientes juegos con RemotePlay:")
            else:
                print("Te recomendamos los siguientes juegos sin RemotePlay:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con RemotePlay:")
    #13
    @Rule(Fact(steam_trading_cards=MATCH.steam_trading_cards))
    def recommend_games_by_tradingCards(self,steam_trading_cards):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["steam_trading_cards"] == steam_trading_cards:
                juegos.append(juego["name"])
        if juegos:
            if(steam_trading_cards):
                print("Te recomendamos los siguientes juegos con Cromos de Steam:")
            else:
                print("Te recomendamos los siguientes juegos sin Cromos de Steam:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con Cromos de Steam:")
    #14
    @Rule(Fact(min_ram=MATCH.min_ram))
    def recommendByMinRam(self,min_ram):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["min_ram"] < min_ram:
                juegos.append(juego["name"])
        if juegos:
            print(f"Estos son los juegos que puedes jugar con menos de {min_ram} GB de RAM")
            for juego in juegos:
                print("-",juego)
        else:
            print(f"No existen juegos con los que puedas jugar con menos de {min_ram} GB de RAM")
    
    #15
    @Rule(Fact(min_storage=MATCH.min_storage))
    def recommendByMinAlmacenamiento(self,min_storage):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["min_storage"] < min_storage:
                juegos.append(juego["name"])
        if juegos:
            print(f"Estos son los juegos que puedes jugar con menos de {min_storage} GB de Almacenamiento:")
            for juego in juegos:
                print("-",juego)
        else:
            print(f"No existen juegos con los que puedas jugar con menos de {min_storage} GB de Almacenamiento.")
    #16
    @Rule(Fact(controller_support=MATCH.controller_support))
    def recommend_games_by_controlSupp(self,controller_support):
        juegos=[]
        for juego in self.baseDatosJuegos():
            if juego["controller_support"] == controller_support:
                juegos.append(juego["name"])
        if juegos:
            if(controller_support):
                print("Te recomendamos los siguientes juegos con Soporte para Mandos:")
            else:
                print("Te recomendamos los siguientes juegos sin Soporte para Mandos:")
            for juego in juegos:
                print("-",juego)
        else:
            print("No hay juegos disponibles con Soporte para Mandos.")

sistema = SistemaRecomendacion()
sistema.reset()
sistema.declare(Fact(price_range=50))  
sistema.declare(Fact(genres=["Single-player","Multiplayer"]))
sistema.declare(Fact(languages=["Spanish","Italian"]))
sistema.declare(Fact(singleplayer=False))
sistema.declare(Fact(online_multiplayer=True))
sistema.declare(Fact(release_date="2015-05-10")) #formato yyyy/mm/dd
sistema.declare(Fact(user_rating=9.0))
sistema.declare(Fact(multiplatform=True))
sistema.declare(Fact(achievements=True))
sistema.declare(Fact(in_app_purchases=True))
sistema.declare(Fact(steam_trading_cards=False))
sistema.declare(Fact(min_ram=1))
sistema.declare(Fact(min_storage=10))
sistema.declare(Fact(controller_support=False))
sistema.run()
