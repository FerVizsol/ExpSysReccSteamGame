from experta import * 

class Juego(Fact):
    pass

class SistemaRecomendacion(KnowledgeEngine):
    DefFacts
    def baseDatosJuegos(self):
        yield Juego(name="Left 4 Dead 2", price_range="S/.23.00",
        genres=["Zombies", "Co-op", "FPS", "Multiplayer", "Shooter", "Online Co-Op", "Action", "Survival", "Horror", "First-Person", "Gore", "Team-Based", "Moddable", "Survival Horror", "Post-apocalyptic", "Singleplayer", "Adventure", "Local Co-Op", "Replay Value", "Tactical"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Achievements", "Steam Trading Cards", "Captions available", "Steam Workshop", "Steam Cloud", "Valve Anti-Cheat enabled", "Stats", "Includes Source SDK", "Commentary available", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV", "Remote Play Together", "Family Sharing", "Co-op", "Multi-player", "HDR rendering", "Full Controller Support", "Native Steam Controller", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2009-11-17", user_rating=9.6, multiplatform=False, achievements=True, steam_workshop=True, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["Danish", "Dutch", "English", "Finnish", "French", "German", "Italian", "Japanese", "Korean", "Norwegian", "Polish", "Portuguese - Portugal", "Russian", "Simplified Chinese", "Spanish - Spain", "Swedish", "Traditional Chinese", "Hungarian", "Turkish", "Bulgarian", "Czech", "Greek", "Portuguese - Brazil", "Romanian", "Spanish - Latin America", "Thai", "Ukrainian", "Vietnamese"],
        steam_trading_cards=True, min_ram="2GB", min_storage="13GB", controller_support=True)

        yield Juego(name="The Witcher 3", price_range="S/.96.00",
        genres=["Open World", "RPG", "Story Rich", "Atmospheric", "Mature", "Fantasy", "Adventure", "Singleplayer", "Nudity", "Choices Matter", "Great Soundtrack", "Third Person", "Medieval", "Action", "Multiple Endings", "Action RPG", "Magic", "Dark Fantasy", "Dark", "Sandbox"],
        categories=["Single-player", "Steam Achievements", "Steam Trading Cards", "Steam Cloud", "Remote Play on Tablet", "Remote Play on TV", "Family Sharing", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Partial Controller Support"],
        singleplayer=True, online_multiplayer=False, release_date="2015-05-18", user_rating=9.5, multiplatform=True, achievements=True, steam_workshop=True, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Arabic", "Czech", "Hungarian", "Japanese", "Korean", "Polish", "Portuguese - Brazil", "Russian", "Traditional Chinese", "Turkish", "Simplified Chinese", "Portuguese - Portugal"],
        steam_trading_cards=True, min_ram="6GB", min_storage="50GB", controller_support=True)

        yield Juego(name="Counter-Strike", price_range="Free", 
        genres=["FPS", "Shooter", "Multiplayer", "Competitive", "Action", "Team-Based", "eSports", "Tactical", "First-Person", "PvP", "Online Co-Op", "Co-op", "Strategy", "Military", "War", "Difficult", "Trading", "Realistic", "Fast-Paced", "Moddable"],
        categories=["Cross-Platform Multiplayer", "Steam Trading Cards", "Steam Workshop", "In-App Purchases", "Valve Anti-Cheat enabled", "Stats", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV", "Multi-player", "Native Steam Controller", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=False, online_multiplayer=True, release_date="2012-08-21", user_rating=8.7, multiplatform=True, achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "German", "French", "Italian", "Korean", "Spanish - Spain", "Simplified Chinese", "Traditional Chinese", "Russian", "Thai", "Japanese", "Portuguese - Portugal", "Polish", "Danish", "Dutch", "Finnish", "Norwegian", "Swedish", "Hungarian", "Czech", "Romanian", "Turkish", "Portuguese - Brazil", "Bulgarian", "Greek", "Ukrainian", "Spanish - Latin America", "Vietnamese"],
        steam_trading_cards=True, min_ram="8GB", min_storage="85GB", controller_support=False)

        yield Juego(name="Dota 2", price_range="Free",
        genres=["Free to Play", "MOBA", "Multiplayer", "Strategy", "eSports", "Team-Based", "Competitive", "Action", "Online Co-Op", "PvP", "Difficult", "Co-op", "RTS", "RPG", "Tower Defense", "Fantasy", "Character Customization", "Replay Value", "Action RPG", "Simulation"],
        categories=["Steam Trading Cards", "Steam Workshop", "SteamVR Collectibles", "In-App Purchases", "Valve Anti-Cheat enabled", "Multi-player", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2013-07-9", user_rating=8.1, multiplatform=True, achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["Portuguese - Brazil", "Bulgarian", "Czech", "Danish", "Dutch", "Finnish", "French", "German", "Greek", "Hungarian", "Italian", "Japanese", "Korean", "Spanish - Latin America", "Norwegian", "Polish", "Portuguese - Portugal", "Romanian", "Russian", "Simplified Chinese", "Spanish - Spain", "Swedish", "Traditional Chinese", "Thai", "Turkish", "Ukrainian", "Vietnamese"],
        steam_trading_cards=True, min_ram="4GB", min_storage="60GB", controller_support=False)

        yield Juego(name="HELLDIVERS™ 2", price_range="S/.139",
        genres=["Online Co-Op", "Action", "Third-Person Shooter", "Multiplayer", "Shooter", "Co-op", "PvE", "Sci-fi", "Space", "Third Person", "Capitalism", "Extraction Shooter", "Comedy", "Gore", "Violent", "Difficult", "Great Soundtrack", "Psychological Horror", "Singleplayer", "Open World"],
        categories=["Online Co-op", "Steam Achievements", "In-App Purchases", "Family Sharing", "Multi-player", "Co-op", "Partial Controller Support", "DualShock Controllers (USB Only)", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=True, online_multiplayer=True, release_date="2024-02-8", user_rating=8.4, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["German", "French", "Italian", "Spanish - Spain", "Simplified Chinese", "Traditional Chinese", "Russian", "Japanese", "Portuguese - Portugal", "Polish", "Portuguese - Brazil", "Spanish - Latin America", "Korean"],
        steam_trading_cards=True, min_ram="8GB", min_storage="100GB", controller_support=True)

        yield Juego(name="Stardew Valley", price_range="S/.39.95",
        genres=["Farming Sim", "Pixel Graphics", "Life Sim", "Multiplayer", "RPG", "Relaxing", "Agriculture", "Simulation", "Crafting", "Sandbox", "Indie", "Building", "Singleplayer", "Casual", "Open World", "2D", "Cute", "Dating Sim", "Great Soundtrack", "Fishing"],
        categories=["Single-player", "Online Co-op", "LAN Co-op", "Shared/Split Screen Co-op", "Steam Achievements", "Steam Trading Cards", "Steam Cloud", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play Together", "Family Sharing", "Multi-player", "Co-op", "Full Controller Support", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Shared/Split Screen"],
        singleplayer=True, online_multiplayer=True, release_date="2016-02-26", user_rating=9.7, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "German", "Spanish - Spain", "Japanese", "Portuguese - Brazil", "Russian", "Simplified Chinese", "French", "Italian", "Hungarian", "Korean", "Turkish"],
        steam_trading_cards=True, min_ram="2GB", min_storage="0.5GB", controller_support=True)
        
        yield Juego(name="PUBG: BATTLEGROUNDS", price_range="Free",
        genres=["Survival", "Shooter", "Battle Royale", "Multiplayer", "FPS", "PvP", "Third-Person Shooter", "Action", "Online Co-Op", "Tactical", "Co-op", "First-Person", "Strategy", "Early Access", "Competitive", "Third Person", "Team-Based", "Difficult", "Simulation", "Stealth"],
        categories=["Online PvP", "Stats", "Remote Play on Phone", "Remote Play on Tablet", "Multi-player", "PvP"],
        singleplayer=True, online_multiplayer=True, release_date="2017-12-21", user_rating=5.8, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "Korean", "Simplified Chinese", "French", "German", "Spanish - Spain", "Arabic", "Japanese", "Polish", "Portuguese - Portugal", "Russian", "Turkish", "Thai", "Italian", "Portuguese - Brazil", "Traditional Chinese", "Ukrainian"],
        steam_trading_cards=True, min_ram="8GB", min_storage="40GB", controller_support=True)
                
        yield Juego(name="Call of Duty®", price_range="Free",
        genres=["FPS", "Multiplayer", "Shooter", "Action", "Singleplayer", "Military", "First-Person", "War", "Modern", "Tactical", "Violent", "Co-op", "Realistic", "Story Rich", "Atmospheric", "Mature", "Online Co-Op", "Gore", "Third-Person Shooter", "Third Person"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Cross-Platform Multiplayer", "Steam Achievements", "Captions available", "In-App Purchases", "Full Controller Support", "Multi-player", "PvP", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2022-10-26", user_rating=5.8, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Korean", "Polish", "Russian", "Traditional Chinese", "Japanese", "Spanish - Latin America", "Arabic", "Simplified Chinese", "Portuguese - Brazil", "Thai", "Portuguese - Portugal"],
        steam_trading_cards=True, min_ram="8GB", min_storage="149GB", controller_support=True)

        yield Juego(name="Tom Clancy's Rainbow Six Siege", price_range="S/.75.00",
        genres=["FPS", "PvP", "eSports", "Multiplayer", "Tactical", "Shooter", "Competitive", "Online Co-Op", "Action", "Hero Shooter", "Team-Based", "Military", "Strategy", "War", "First-Person", "Realistic", "Co-op", "Destruction", "Difficult", "3D"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Trading Cards", "In-App Purchases", "Remote Play on Phone", "Remote Play on Tablet", "Multi-player", "Co-op", "Native Steam Controller", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Full Controller Support", "DualShock Controllers (USB Only)", "DualShock Controllers", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=False, online_multiplayer=True, release_date="2015-12-01", user_rating=8.5, multiplatform=False, achievements=False, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Czech", "Dutch", "Japanese", "Korean", "Polish", "Portuguese - Brazil", "Russian", "Traditional Chinese", "Simplified Chinese", "Turkish", "Thai"],
        steam_trading_cards=True, min_ram="6GB", min_storage="61GB", controller_support=False)

        yield Juego(name="Apex Legends", price_range="Free",
        genres=["Free to Play", "Battle Royale", "Multiplayer", "FPS", "Shooter", "First-Person", "PvP", "Action", "Team-Based", "Hero Shooter", "Tactical", "Sci-fi", "Survival", "Loot", "Character Customization", "Funny", "Co-op", "Lore-Rich", "Cyberpunk", "Cinematic"],
        categories=["Online PvP", "Online Co-op", "Steam Achievements", "Steam Trading Cards", "In-App Purchases", "Multi-player", "Full Controller Support", "Co-op", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "DualShock Controllers (USB Only)", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=False, online_multiplayer=True, release_date="2020-11-05", user_rating=7.8, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Japanese", "Korean", "Polish", "Portuguese - Brazil", "Russian", "Simplified Chinese", "Traditional Chinese", "Spanish - Latin America", "Arabic"],
        steam_trading_cards=True, min_ram="6GB", min_storage="75GB", controller_support=True)

        yield Juego(name="Baldur's Gate 3", price_range="S/.199.00",
        genres=["RPG", "Choices Matter", "Character Customization", "Story Rich", "Turn-Based Combat", "Dungeons & Dragons", "Adventure", "CRPG", "Fantasy", "Online Co-Op", "Romance", "Multiplayer", "Strategy", "Singleplayer", "Co-op Campaign", "Sexual Content", "Class-Based", "Dark Fantasy", "Combat", "Controller"],
        categories=["Single-player", "Online Co-op", "LAN Co-op", "Steam Achievements", "Steam Cloud", "Family Sharing", "Multi-player", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Full Controller Support", "DualShock Controllers (USB Only)", "DualShock Controllers", "DualSense Controllers (USB Only)", "DualSense Controllers", "Steam Input API Supported"],
        singleplayer=True, online_multiplayer=True, release_date="2023-08-03", user_rating=9.6, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "French", "German", "Spanish - Spain", "Polish", "Russian", "Simplified Chinese", "Turkish", "Portuguese - Brazil", "Italian", "Spanish - Latin America", "Traditional Chinese", "Ukrainian", "Korean", "Japanese"],
        steam_trading_cards=True, min_ram="8GB", min_storage="150GB", controller_support=False)

        yield Juego(name="Team Fortress 2", price_range="Free",
        genres=["Free to Play", "Hero Shooter", "Multiplayer", "FPS", "Shooter", "Action", "Class-Based", "Team-Based", "Funny", "First-Person", "Online Co-Op", "Competitive", "Cartoony", "Trading", "Co-op", "Comedy", "Robots", "Tactical", "Cartoon", "Crafting"],
        categories=["Cross-Platform Multiplayer", "Steam Achievements", "Steam Trading Cards", "Captions available", "Steam Workshop", "In-App Purchases", "Valve Anti-Cheat enabled", "Stats", "Includes level editor", "Commentary available", "Remote Play on Phone", "Remote Play on Tablet", "HDR rendering", "Partial Controller Support", "Multi-player", "Native Steam Controller", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=False, online_multiplayer=True, release_date="2007-10-10", user_rating=9.3, multiplatform=False, achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        languages=["English", "Danish", "Dutch", "Finnish", "French", "German", "Italian", "Japanese", "Norwegian", "Polish", "Portuguese - Portugal", "Russian", "Simplified Chinese", "Spanish - Spain", "Swedish", "Traditional Chinese", "Korean", "Czech", "Hungarian", "Portuguese - Brazil", "Turkish", "Greek", "Bulgarian", "Romanian", "Thai", "Ukrainian"],
        steam_trading_cards=True, min_ram="0.5GB", min_storage="15GB", controller_support=False)

        yield Juego(name="Rust", price_range="S/79.00",
        genres=["Survival", "Crafting", "Multiplayer", "Open World", "Open World Survival Craft", "Building", "PvP", "Sandbox", "Adventure", "First-Person", "Action", "Nudity", "FPS", "Shooter", "Co-op", "Online Co-Op", "Indie", "Early Access", "Post-apocalyptic", "Simulation"],
        categories=["MMO", "Online PvP", "Online Co-op", "Cross-Platform Multiplayer", "Steam Achievements", "Steam Trading Cards", "Steam Workshop", "In-App Purchases", "Valve Anti-Cheat enabled", "Stats", "Remote Play on Tablet", "Multi-player", "Co-op", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=False, online_multiplayer=True, release_date="2018-02-08", user_rating=8.6, multiplatform=False, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Japanese", "Korean", "Russian", "Simplified Chinese", "Ukrainian", "Polish", "Portuguese - Portugal", "Turkish", "Arabic", "Czech", "Danish", "Dutch", "Finnish", "Greek", "Norwegian", "Portuguese - Brazil", "Spanish - Latin America", "Swedish", "Traditional Chinese", "Vietnamese"],
        steam_trading_cards=True, min_ram="10GB", min_storage="25GB", controller_support=True)

        yield Juego(name="Grand Theft Auto V", price_range="Free",
        genres=["Open World", "Action", "Multiplayer", "Crime", "Automobile Sim", "Third Person", "First-Person", "Mature", "Shooter", "Adventure", "Singleplayer", "Third-Person Shooter", "Racing", "Co-op", "Sandbox", "Atmospheric", "Funny", "Great Soundtrack", "Comedy", "Moddable"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Achievements", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV", "Multi-player", "Full Controller Support", "PvP", "Co-op"],
        singleplayer=False, online_multiplayer=True, release_date="2015-04-13", user_rating=8.6, multiplatform=True, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Korean", "Polish", "Portuguese - Brazil", "Russian", "Traditional Chinese", "Japanese", "Simplified Chinese", "Spanish - Latin America"],
        steam_trading_cards=True, min_ram="4GB", min_storage="110GB", controller_support=True)

        yield Juego(name="Crab Game", price_range="Free",
        genres=["Psychological Horror", "Multiplayer", "Free to Play", "Battle Royale", "PvP", "Action", "First-Person", "Parkour", "3D", "Nudity", "FPS", "Platformer", "Physics", "Arcade", "Combat", "Casual", "Runner", "Racing", "3D Platformer", "Sci-fi"],
        categories=["Online PvP", "Online Co-op", "Multi-player", "PvP", "Co-op"],
        singleplayer=False, online_multiplayer=True, release_date="2021-10-28", user_rating=9.1, multiplatform=False, achievements=False, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English"],
        steam_trading_cards=True, min_ram="2GB", min_storage="0.2GB", controller_support=False)

        yield Juego(name="NARAKA: BLADEPOINT", price_range="Free",
        genres=["Battle Royale", "Multiplayer", "Martial Arts", "PvP", "Action", "Female Protagonist", "Fighting", "Massively Multiplayer", "Third Person", "Survival", "Character Customization", "Hack and Slash", "Swordplay", "Anime", "Parkour", "Adventure", "Mature", "Free to Play", "Violent", "Gore"],
        categories=["Online PvP", "In-App Purchases", "Multi-player", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Partial Controller Support"],
        singleplayer=False, online_multiplayer=True, release_date="2021-05-12", user_rating=6.9, multiplatform=False, achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English", "Simplified Chinese", "Traditional Chinese", "Japanese", "Korean", "French", "German", "Spanish - Spain", "Russian", "Turkish", "Portuguese - Portugal", "Vietnamese", "Thai", "Arabic", "Portuguese - Brazil", "Spanish - Latin America"],
        steam_trading_cards=True, min_ram="8GB", min_storage="35GB", controller_support=True)


