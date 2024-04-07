from experta import * 

class Juego(Fact):
    pass

class SistemaRecomendacion(KnowledgeEngine):
    DefFacts
    def baseDatosJuegos(self):
        yield Juego(name="Left 4 Dead 2", price_range="$", genres=["Action", "Adventure", "Action", "FPS"])
        yield Juego(name="The Witcher 3", price_range="$$", genres=["RPG", "Adventure"],singleplayer=True, online_multiplayer=False, release_date="2015-05-19",user_rating=4.8, multiplatform=True, achievements=True,steam_workshop=True, in_app_purchases=False, active_community_market=True,remote_play=True, languages=["English", "Spanish"],steam_trading_cards=True, min_ram="8GB", min_storage="50GB",controller_support=True)
        yield Juego(name="Juego 1")
