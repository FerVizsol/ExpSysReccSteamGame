from experta import * 
import datetime
class Juego(Fact):
    pass


class SistemaRecomendacion(KnowledgeEngine):
    @DefFacts()
    def baseDatosJuegos(self):
        
        yield Juego(name="Left 4 Dead 2", price_range=22.00, discount=False, percentage_discount=0,
        genres=["Zombies", "Co-op", "FPS", "Multiplayer", "Shooter", "Online Co-Op", "Action", "Survival", "Horror", "First-Person", "Gore", "Team-Based", "Moddable", "Survival Horror", "Post-apocalyptic", "Singleplayer", "Adventure", "Local Co-Op", "Replay Value", "Tactical"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Achievements", "Steam Trading Cards", "Captions available", "Steam Workshop", "Steam Cloud", "Valve Anti-Cheat enabled", "Stats", "Includes Source SDK", "Commentary available", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV", "Remote Play Together", "Family Sharing", "Co-op", "Multi-player", "HDR rendering", "Full Controller Support", "Native Steam Controller", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2009-11-17", last_update= "2024-03-26", user_rating=9.6, multiplatform=False,
        achievements=True, steam_workshop=True, in_app_purchases=False, active_community_market=True, remote_play=True,
        developer="Valve", publisher="Valve", age_rating=False, age_rating_score=0, dlc=True, dlc_count=3, award_steam=0,
        languages=["Danish", "Dutch", "English", "Finnish", "French", "German", "Italian", "Japanese", "Korean", "Norwegian", "Polish", "Portuguese", "Russian", "Simplified Chinese", "Spanish", "Swedish", "Traditional Chinese", "Hungarian", "Turkish", "Bulgarian", "Czech", "Greek", "Portuguese", "Romanian", "Spanish - Latin America", "Thai", "Ukrainian", "Vietnamese"],
        steam_trading_cards=True, min_ram="2GB", min_storage="13GB", controller_support=True)

        yield Juego(name="The Witcher 3", price_range=96.00, discount=False, percentage_discount=0,
        genres=["Open World", "RPG", "Story Rich", "Atmospheric", "Mature", "Fantasy", "Adventure", "Singleplayer", "Nudity", "Choices Matter", "Great Soundtrack", "Third Person", "Medieval", "Action", "Multiple Endings", "Action RPG", "Magic", "Dark Fantasy", "Dark", "Sandbox"],
        categories=["Single-player", "Steam Achievements", "Steam Trading Cards", "Steam Cloud", "Remote Play on Tablet", "Remote Play on TV", "Family Sharing", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Partial Controller Support"],
        singleplayer=True, online_multiplayer=False, release_date="2015-05-18", last_update= "2024-04-09", user_rating=9.5, multiplatform=True,
        achievements=True, steam_workshop=True, in_app_purchases=False, active_community_market=True, remote_play=True,
        developer="CD PROJEKT RED", publisher="CD PROJEKT RED", age_rating=True, age_rating_score=17, dlc=True, dlc_count=19, award_steam=1,
        languages=["English", "French", "Italian", "German", "Spanish", "Arabic", "Czech", "Hungarian", "Japanese", "Korean", "Polish", "Portuguese", "Russian", "Traditional Chinese", "Turkish", "Simplified Chinese", "Portuguese"],
        steam_trading_cards=True, min_ram="6GB", min_storage="50GB", controller_support=True)

        yield Juego(name="Counter-Strike 2", price_range=0.0, discount=False, percentage_discount=0,
        genres=["FPS", "Shooter", "Multiplayer", "Competitive", "Action", "Team-Based", "eSports", "Tactical", "First-Person", "PvP", "Online Co-Op", "Co-op", "Strategy", "Military", "War", "Difficult", "Trading", "Realistic", "Fast-Paced", "Moddable"],
        categories=["Cross-Platform Multiplayer", "Steam Trading Cards", "Steam Workshop", "In-App Purchases", "Valve Anti-Cheat enabled", "Stats", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV", "Multi-player", "Native Steam Controller", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=False, online_multiplayer=True, release_date="2012-08-21", last_update= "2024-04-02", user_rating=8.7, multiplatform=True,
        achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        developer="Valve", publisher="Valve", age_rating=True, age_rating_score=17, dlc=True, dlc_count=19, award_steam=1,
        languages=["English", "German", "French", "Italian", "Korean", "Spanish", "Simplified Chinese", "Traditional Chinese", "Russian", "Thai", "Japanese", "Portuguese", "Polish", "Danish", "Dutch", "Finnish", "Norwegian", "Swedish", "Hungarian", "Czech", "Romanian", "Turkish", "Portuguese", "Bulgarian", "Greek", "Ukrainian", "Spanish - Latin America", "Vietnamese"],
        steam_trading_cards=True, min_ram="8GB", min_storage="85GB", controller_support=False)

        yield Juego(name="Dota 2", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Free to Play", "MOBA", "Multiplayer", "Strategy", "eSports", "Team-Based", "Competitive", "Action", "Online Co-Op", "PvP", "Difficult", "Co-op", "RTS", "RPG", "Tower Defense", "Fantasy", "Character Customization", "Replay Value", "Action RPG", "Simulation"],
        categories=["Steam Trading Cards", "Steam Workshop", "SteamVR Collectibles", "In-App Purchases", "Valve Anti-Cheat enabled", "Multi-player", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2013-07-9", last_update= "2024-03-21", user_rating=8.1, multiplatform=True,
        achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        developer="Valve", publisher="Valve", age_rating=False, age_rating_score=0, dlc=True, dlc_count=44, award_steam=0,
        languages=["Portuguese", "Bulgarian", "Czech", "Danish", "Dutch", "Finnish", "French", "German", "Greek", "Hungarian", "Italian", "Japanese", "Korean", "Spanish - Latin America", "Norwegian", "Polish", "Portuguese", "Romanian", "Russian", "Simplified Chinese", "Spanish", "Swedish", "Traditional Chinese", "Thai", "Turkish", "Ukrainian", "Vietnamese"],
        steam_trading_cards=True, min_ram="4GB", min_storage="60GB", controller_support=False)

        yield Juego(name="HELLDIVERS™ 2", price_range=139, discount=False, percentage_discount=0,
        genres=["Online Co-Op", "Action", "Third-Person Shooter", "Multiplayer", "Shooter", "Co-op", "PvE", "Sci-fi", "Space", "Third Person", "Capitalism", "Extraction Shooter", "Comedy", "Gore", "Violent", "Difficult", "Great Soundtrack", "Psychological Horror", "Singleplayer", "Open World"],
        categories=["Online Co-op", "Steam Achievements", "In-App Purchases", "Family Sharing", "Multi-player", "Co-op", "Partial Controller Support", "DualShock Controllers (USB Only)", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=True, online_multiplayer=True, release_date="2024-02-8", last_update= "2024-04-02", user_rating=8.4, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        developer="Arrowhead Game Studios", publisher="PlayStation PC LLC", age_rating=True, age_rating_score=17, dlc=True, dlc_count=13, award_steam=1,
        languages=["German", "French", "Italian", "Spanish", "Simplified Chinese", "Traditional Chinese", "Russian", "Japanese", "Portuguese", "Polish", "Portuguese", "Spanish - Latin America", "Korean"],
        steam_trading_cards=True, min_ram="8GB", min_storage="100GB", controller_support=True)

        yield Juego(name="Stardew Valley", price_range=39.95, discount=False, percentage_discount=0,
        genres=["Farming Sim", "Pixel Graphics", "Life Sim", "Multiplayer", "RPG", "Relaxing", "Agriculture", "Simulation", "Crafting", "Sandbox", "Indie", "Building", "Singleplayer", "Casual", "Open World", "2D", "Cute", "Dating Sim", "Great Soundtrack", "Fishing"],
        categories=["Single-player", "Online Co-op", "LAN Co-op", "Shared/Split Screen Co-op", "Steam Achievements", "Steam Trading Cards", "Steam Cloud", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play Together", "Family Sharing", "Multi-player", "Co-op", "Full Controller Support", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Shared/Split Screen"],
        singleplayer=True, online_multiplayer=True, release_date="2016-02-26", last_update= "2024-03-19", user_rating=9.7, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        developer="ConcernedApe", publisher="ConcernedApe", age_rating=True, age_rating_score=10, dlc=False, dlc_count=0, award_steam=1,
        languages=["English", "German", "Spanish", "Japanese", "Portuguese", "Russian", "Simplified Chinese", "French", "Italian", "Hungarian", "Korean", "Turkish"],
        steam_trading_cards=True, min_ram="2GB", min_storage="0.5GB", controller_support=True)
        
        yield Juego(name="PUBG: BATTLEGROUNDS", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Survival", "Shooter", "Battle Royale", "Multiplayer", "FPS", "PvP", "Third-Person Shooter", "Action", "Online Co-Op", "Tactical", "Co-op", "First-Person", "Strategy", "Early Access", "Competitive", "Third Person", "Team-Based", "Difficult", "Simulation", "Stealth"],
        categories=["Online PvP", "Stats", "Remote Play on Phone", "Remote Play on Tablet", "Multi-player", "PvP"],
        singleplayer=True, online_multiplayer=True, release_date="2017-12-21", last_update= "2024-01-10", user_rating=5.8, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        developer="KRAFTON, Inc.", publisher="KRAFTON, Inc.", age_rating=True, age_rating_score=13, dlc=True, dlc_count=12, award_steam=1,
        languages=["English", "Korean", "Simplified Chinese", "French", "German", "Spanish", "Arabic", "Japanese", "Polish", "Portuguese", "Russian", "Turkish", "Thai", "Italian", "Portuguese", "Traditional Chinese", "Ukrainian"],
        steam_trading_cards=True, min_ram="8GB", min_storage="40GB", controller_support=True)
                
        yield Juego(name="Call of Duty®", price_range=0.0, discount=False, percentage_discount=0,
        genres=["FPS", "Multiplayer", "Shooter", "Action", "Singleplayer", "Military", "First-Person", "War", "Modern", "Tactical", "Violent", "Co-op", "Realistic", "Story Rich", "Atmospheric", "Mature", "Online Co-Op", "Gore", "Third-Person Shooter", "Third Person"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Cross-Platform Multiplayer", "Steam Achievements", "Captions available", "In-App Purchases", "Full Controller Support", "Multi-player", "PvP", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2022-10-26", last_update= "2024-05-27", user_rating=5.8, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        developer="Sledgehammer Games, Treyarch, Infinity Ward, Beenox, Raven Software, High Moon Studios, Demonware", publisher="Activision", age_rating=True, age_rating_score=17, dlc=True, dlc_count=66, award_steam=0,
        languages=["English", "French", "Italian", "German", "Spanish", "Korean", "Polish", "Russian", "Traditional Chinese", "Japanese", "Spanish - Latin America", "Arabic", "Simplified Chinese", "Portuguese", "Thai", "Portuguese"],
        steam_trading_cards=True, min_ram="8GB", min_storage="149GB", controller_support=True)

        yield Juego(name="Call of Juarez: Gunslinger", price_range=47.99, discount=False, percentage_discount=0,
        genres=["Western", "FPS", "Action", "Shooter", "Singleplayer", "Story Rich", "Bullet Time", "Comedy", "First-Person", "Narration", "Adventure", "Dynamic Narration", "Funny", "Violent", "Atmospheric", "Arcade", "Gore", "America", "Historical", "Alternate History"],
        categories=["Single-player", "Steam Achievements", "Steam Trading Cards", "Steam Cloud", "Steam Leaderboards", "Family Sharing", "Full Controller Support", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=False, release_date="2022-10-26", last_update= "2023-05-31", user_rating=5.8, multiplatform=False,
        achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=False, remote_play=False,
        developer="Techland", publisher="Techland Publishing", age_rating=True, age_rating_score=17, dlc=False, dlc_count=0, award_steam=1,
        languages=["English", "German", "French", "Italian", "Spanish", "Russian", "Japanese", "Polish", "Portuguese"],
        steam_trading_cards=False, min_ram="2GB", min_storage="5GB", controller_support=False)

        yield Juego(name="Tom Clancy's Rainbow Six Siege", price_range=75.00, discount=False, percentage_discount=0,
        genres=["FPS", "PvP", "eSports", "Multiplayer", "Tactical", "Shooter", "Competitive", "Online Co-Op", "Action", "Hero Shooter", "Team-Based", "Military", "Strategy", "War", "First-Person", "Realistic", "Co-op", "Destruction", "Difficult", "3D"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Trading Cards", "In-App Purchases", "Remote Play on Phone", "Remote Play on Tablet", "Multi-player", "Co-op", "Native Steam Controller", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Full Controller Support", "DualShock Controllers (USB Only)", "DualShock Controllers", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=True, online_multiplayer=True, release_date="2015-12-01", last_update= "2024-03-12", user_rating=8.5, multiplatform=False,
        achievements=False, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        developer="Ubisoft", publisher="Ubisoft", age_rating=True, age_rating_score=17, dlc=True, dlc_count=64, award_steam=1,
        languages=["English", "French", "Italian", "German", "Spanish", "Czech", "Dutch", "Japanese", "Korean", "Polish", "Portuguese", "Russian", "Traditional Chinese", "Simplified Chinese", "Turkish", "Thai"],
        steam_trading_cards=True, min_ram="6GB", min_storage="61GB", controller_support=False)

        yield Juego(name="Apex Legends", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Free to Play", "Battle Royale", "Multiplayer", "FPS", "Shooter", "First-Person", "PvP", "Action", "Team-Based", "Hero Shooter", "Tactical", "Sci-fi", "Survival", "Loot", "Character Customization", "Funny", "Co-op", "Lore-Rich", "Cyberpunk", "Cinematic"],
        categories=["Online PvP", "Online Co-op", "Steam Achievements", "Steam Trading Cards", "In-App Purchases", "Multi-player", "Full Controller Support", "Co-op", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "DualShock Controllers (USB Only)", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=False, online_multiplayer=True, release_date="2020-11-05", last_update= "2024-02-13", user_rating=7.8, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=False, remote_play=True,
        developer="Respawn", publisher="Electronic Arts", age_rating=True, age_rating_score=13, dlc=True, dlc_count=28, award_steam=1,
        languages=["English", "French", "Italian", "German", "Spanish", "Japanese", "Korean", "Polish", "Portuguese", "Russian", "Simplified Chinese", "Traditional Chinese", "Spanish - Latin America", "Arabic"],
        steam_trading_cards=True, min_ram="6GB", min_storage="75GB", controller_support=True)

        yield Juego(name="Baldur's Gate 3", price_range=199.00, discount=False, percentage_discount=0,
        genres=["RPG", "Choices Matter", "Character Customization", "Story Rich", "Turn-Based Combat", "Dungeons & Dragons", "Adventure", "CRPG", "Fantasy", "Online Co-Op", "Romance", "Multiplayer", "Strategy", "Singleplayer", "Co-op Campaign", "Sexual Content", "Class-Based", "Dark Fantasy", "Combat", "Controller"],
        categories=["Single-player", "Online Co-op", "LAN Co-op", "Steam Achievements", "Steam Cloud", "Family Sharing", "Multi-player", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Full Controller Support", "DualShock Controllers (USB Only)", "DualShock Controllers", "DualSense Controllers (USB Only)", "DualSense Controllers", "Steam Input API Supported"],
        singleplayer=True, online_multiplayer=True, release_date="2023-08-03", last_update= "2024-04-10", user_rating=9.6, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=False, remote_play=True,
        developer="Larian Studios", publisher="Larian Studios", age_rating=True, age_rating_score=17, dlc=True, dlc_count=2, award_steam=1,
        languages=["English", "French", "German", "Spanish", "Polish", "Russian", "Simplified Chinese", "Turkish", "Portuguese", "Italian", "Spanish - Latin America", "Traditional Chinese", "Ukrainian", "Korean", "Japanese"],
        steam_trading_cards=True, min_ram="8GB", min_storage="150GB", controller_support=False)

        yield Juego(name="Team Fortress 2", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Free to Play", "Hero Shooter", "Multiplayer", "FPS", "Shooter", "Action", "Class-Based", "Team-Based", "Funny", "First-Person", "Online Co-Op", "Competitive", "Cartoony", "Trading", "Co-op", "Comedy", "Robots", "Tactical", "Cartoon", "Crafting"],
        categories=["Cross-Platform Multiplayer", "Steam Achievements", "Steam Trading Cards", "Captions available", "Steam Workshop", "In-App Purchases", "Valve Anti-Cheat enabled", "Stats", "Includes level editor", "Commentary available", "Remote Play on Phone", "Remote Play on Tablet", "HDR rendering", "Partial Controller Support", "Multi-player", "Native Steam Controller", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=False, online_multiplayer=True, release_date="2007-10-10", last_update= "2024-01-09", user_rating=9.3, multiplatform=False,
        achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        developer="Valve", publisher="Valve", age_rating=False, age_rating_score=0, dlc=True, dlc_count=6, award_steam=0,
        languages=["English", "Danish", "Dutch", "Finnish", "French", "German", "Italian", "Japanese", "Norwegian", "Polish", "Portuguese", "Russian", "Simplified Chinese", "Spanish", "Swedish", "Traditional Chinese", "Korean", "Czech", "Hungarian", "Portuguese", "Turkish", "Greek", "Bulgarian", "Romanian", "Thai", "Ukrainian"],
        steam_trading_cards=True, min_ram="0.5GB", min_storage="15GB", controller_support=False)

        yield Juego(name="Rust", price_range=79.00, discount=False, percentage_discount=0,
        genres=["Survival", "Crafting", "Multiplayer", "Open World", "Open World Survival Craft", "Building", "PvP", "Sandbox", "Adventure", "First-Person", "Action", "Nudity", "FPS", "Shooter", "Co-op", "Online Co-Op", "Indie", "Early Access", "Post-apocalyptic", "Simulation"],
        categories=["MMO", "Online PvP", "Online Co-op", "Cross-Platform Multiplayer", "Steam Achievements", "Steam Trading Cards", "Steam Workshop", "In-App Purchases", "Valve Anti-Cheat enabled", "Stats", "Remote Play on Tablet", "Multi-player", "Co-op", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=False, online_multiplayer=True, release_date="2018-02-08", last_update= "2024-04-04", user_rating=8.6, multiplatform=False,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=False, remote_play=True,
        developer="Facepunch Studios", publisher="Facepunch Studios", age_rating=False, age_rating_score=0, dlc=True, dlc_count=5, award_steam=0,
        languages=["English", "French", "Italian", "German", "Spanish", "Japanese", "Korean", "Russian", "Simplified Chinese", "Ukrainian", "Polish", "Portuguese", "Turkish", "Arabic", "Czech", "Danish", "Dutch", "Finnish", "Greek", "Norwegian", "Portuguese", "Spanish - Latin America", "Swedish", "Traditional Chinese", "Vietnamese"],
        steam_trading_cards=True, min_ram="10GB", min_storage="25GB", controller_support=True)

        yield Juego(name="Grand Theft Auto V", price_range=150.0, discount=True, percentage_discount=63,
        genres=["Open World", "Action", "Multiplayer", "Crime", "Automobile Sim", "Third Person", "First-Person", "Mature", "Shooter", "Adventure", "Singleplayer", "Third-Person Shooter", "Racing", "Co-op", "Sandbox", "Atmospheric", "Funny", "Great Soundtrack", "Comedy", "Moddable"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Achievements", "Remote Play on Phone", "Remote Play on Tablet", "Remote Play on TV", "Multi-player", "Full Controller Support", "PvP", "Co-op"],
        singleplayer=True, online_multiplayer=True, release_date="2015-04-13", last_update= "2024-01-01", user_rating=8.6, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=False, remote_play=True,
        developer="Rockstar", publisher="Rockstar", age_rating=True, age_rating_score=17, dlc=True, dlc_count=6, award_steam=2,
        languages=["English", "French", "Italian", "German", "Spanish", "Korean", "Polish", "Portuguese", "Russian", "Traditional Chinese", "Japanese", "Simplified Chinese", "Spanish - Latin America"],
        steam_trading_cards=True, min_ram="4GB", min_storage="110GB", controller_support=True)

        yield Juego(name="Crab Game", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Psychological Horror", "Multiplayer", "Free to Play", "Battle Royale", "PvP", "Action", "First-Person", "Parkour", "3D", "Nudity", "FPS", "Platformer", "Physics", "Arcade", "Combat", "Casual", "Runner", "Racing", "3D Platformer", "Sci-fi"],
        categories=["Online PvP", "Online Co-op", "Multi-player", "PvP", "Co-op"],
        singleplayer=False, online_multiplayer=True, release_date="2021-10-28", last_update= "2024-03-15", user_rating=9.1, multiplatform=False,
        achievements=False, steam_workshop=False, in_app_purchases=False, active_community_market=True, remote_play=True,
        languages=["English"],
        developer="Dani", publisher="Dani", age_rating=False, age_rating_score=0, dlc=False, dlc_count=0, award_steam=0,
        steam_trading_cards=True, min_ram="2GB", min_storage="0.2GB", controller_support=False)

        yield Juego(name="NARAKA: BLADEPOINT", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Battle Royale", "Multiplayer", "Martial Arts", "PvP", "Action", "Female Protagonist", "Fighting", "Massively Multiplayer", "Third Person", "Survival", "Character Customization", "Hack and Slash", "Swordplay", "Anime", "Parkour", "Adventure", "Mature", "Free to Play", "Violent", "Gore"],
        categories=["Online PvP", "In-App Purchases", "Multi-player", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Partial Controller Support"],
        singleplayer=False, online_multiplayer=True, release_date="2021-05-12", last_update= "2024-04-10", user_rating=6.9, multiplatform=False,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=True, remote_play=True,
        developer="24 Entertainment", publisher="NetEase Games Global", age_rating=True, age_rating_score=13, dlc=True, dlc_count=9, award_steam=0,
        languages=["English", "Simplified Chinese", "Traditional Chinese", "Japanese", "Korean", "French", "German", "Spanish", "Russian", "Turkish", "Portuguese", "Vietnamese", "Thai", "Arabic", "Portuguese", "Spanish - Latin America"],
        steam_trading_cards=True, min_ram="8GB", min_storage="35GB", controller_support=True)

        yield Juego(name="Destiny 2", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Free to Play", "Open World", "FPS", "Looter Shooter", "MMORPG", "Co-op", "Multiplayer", "PvE", "PvP", "Shooter", "Massively Multiplayer", "Loot", "First-Person", "Sci-fi", "Action", "Lore-Rich", "Adventure", "Space", "Competitive", "Atmospheric"],
        categories=["Single-player", "Online PvP", "Online Co-op", "Steam Achievements", "In-App Purchases", "Multi-player", "PvP", "Co-op", "Native Steam Controller", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Partial Controller Support", "DualShock Controllers (USB Only)", "DualSense Controllers (USB Only)"],
        singleplayer=True, online_multiplayer=True, release_date="2019-10-01", last_update= "2024-04-09", user_rating=9.0, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=False, remote_play=False,
        developer="Bungie", publisher="Bungie", age_rating=True, age_rating_score=13, dlc=True, dlc_count=14, award_steam=0,
        languages=["English", "French", "Italian", "German", "Spanish", "Japanese", "Korean", "Polish", "Portuguese", "Russian", "Simplified Chinese", "Spanish - Latin America", "Traditional Chinese"],
        steam_trading_cards=False, min_ram="6GB", min_storage="105GB", controller_support=True)

        yield Juego(name="Path of Exile", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Free to Play", "Dark Fantasy", "Action RPG", "Hack and Slash", "Loot", "Multiplayer", "MMORPG", "Dungeon Crawler", "Character Customization", "Isometric", "Online Co-Op", "Inventory Management", "RPG", "Singleplayer", "Action", "PvP", "Horror", "Massively Multiplayer", "Fantasy", "Adventure"],
        categories=["Single-player", "MMO", "Online PvP", "Online Co-op", "Steam Achievements", "Steam Trading Cards", "In-App Purchases", "Remote Play on Tablet", "Multi-player", "Co-op", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Full Controller Support", "DualShock Controllers (USB Only)", "DualShock Controllers", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=True, online_multiplayer=True, release_date="2013-10-23", last_update= "2024-04-02", user_rating=8.8, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=False, remote_play=True,
        developer="Grinding Gear Games", publisher="Grinding Gear Games", age_rating=False, age_rating_score=0, dlc=False, dlc_count=0, award_steam=1,
        languages=["English", "Portuguese", "Russian", "Thai", "French", "German", "Spanish", "Japanese", "Korean"],
        steam_trading_cards=False, min_ram="8GB", min_storage="40GB", controller_support=True)

        yield Juego(name="War Thunder", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Free to Play", "Vehicular Combat", "Combat", "World War II", "VR", "Flight", "War", "Military", "Tanks", "Naval Combat", "Simulation", "Modern", "Massively Multiplayer", "Cold War", "Action", "Realistic", "Shooter", "Multiplayer", "Third-Person Shooter", "Third Person"],
        categories=["Single-player", "MMO", "Online PvP", "Online Co-op", "Cross-Platform Multiplayer", "Steam Achievements", "In-App Purchases", "Remote Play on Phone", "Remote Play on Tablet", "VR Supported", "Co-op", "HDR rendering", "Native Steam Controller", "Multi-player", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "PvP", "Full Controller Support", "DualShock Controllers (USB Only)", "DualSense Controllers (USB Only)", "Steam Input API Supported"],
        singleplayer=True, online_multiplayer=True, release_date="2013-08-15", last_update= "2024-04-10", user_rating=6.2, multiplatform=False,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=False, remote_play=True,
        developer="Gaijin Entertainment", publisher="Gaijin Entertainment", age_rating=True, age_rating_score=13, dlc=True, dlc_count=67, award_steam=1,
        languages=["English", "German", "French", "Italian", "Spanish", "Simplified Chinese", "Russian", "Japanese", "Polish", "Czech", "Turkish", "Portuguese - Portugal", "Korean", "Portuguese", "Hungarian", "Ukrainian", "Traditional Chinese", "Romanian"],
        steam_trading_cards=True, min_ram="4GB", min_storage="17GB", controller_support=True)

        yield Juego(name="Football Manager 2024", price_range=159.0, discount=True, percentage_discount=33,
        genres=["Simulation", "Sports", "Strategy", "Football (Soccer)", "Management", "eSports", "Real Time Tactics", "Multiplayer", "3D", "Economy", "2D", "Text-Based", "Singleplayer", "Games Workshop"],
        categories=["Single-player", "Steam Achievements", "Steam Cloud", "Family Sharing", "Multi-player"],
        singleplayer=True, online_multiplayer=True, release_date="2023-11-06", last_update= "2024-04-09", user_rating=8.7, multiplatform=False,
        achievements=True, steam_workshop=False, in_app_purchases=False, active_community_market=False, remote_play=True,
        developer="Sports Interactive", publisher="SEGA", age_rating=False, age_rating_score=0, dlc=True, dlc_count=1, award_steam=0,
        languages=["English", "French", "Italian", "German", "Spanish", "Danish", "Dutch", "Greek", "Japanese", "Korean", "Norwegian", "Polish", "Portuguese", "Russian", "Simplified Chinese", "Swedish", "Turkish"],
        steam_trading_cards=False, min_ram="4GB", min_storage="7GB", controller_support=False)

        yield Juego(name="Lost Ark", price_range=0.0, discount=False, percentage_discount=0,
        genres=["MMORPG", "Free to Play", "Action RPG", "Multiplayer", "Hack and Slash", "RPG", "Character Customization", "Massively Multiplayer", "Action", "Sexual Content", "Adventure", "Fantasy", "PvE", "PvP", "Isometric", "Online Co-Op", "Class-Based", "Singleplayer", "Violent", "Gore"],
        categories=["Singleplayer", "MMO", "Online PvP", "Online Co-op", "Steam Achievements", "In-App Purchases", "Multiplayer", "PvP", "Co-op", "Partial Controller Support", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2022-02-11", last_update= "2024-04-02", user_rating=7.1, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=False, remote_play=False,
        developer="Smilegate RPG", publisher="Amazon Games", age_rating=True, age_rating_score=17, dlc=True, dlc_count=18, award_steam=0,
        languages=["English", "French", "German", "Spanish"],
        steam_trading_cards=False, min_ram="8GB", min_storage="60GB", controller_support=True)

        yield Juego(name="EA SPORTS FC™ 24", price_range=259.0, discount=False, percentage_discount=0,
        genres=["Football (Soccer)", "Sports", "Controller", "Multiplayer", "PvP", "eSports", "Competitive", "3D", "Local Multiplayer", "Simulation", "Co-op", "Online Co-Op", "First-Person", "Realistic", "Singleplayer", "Local Co-Op", "Action", "Family Friendly", "Early Access"],
        categories=["Single-player", "Online PvP", "Shared/Split Screen PvP", "Online Co-op", "Shared/Split Screen Co-op", "Cross-Platform Multiplayer", "Steam Achievements", "In-App Purchases", "Remote Play Together", "HDR Supported", "Multiplayer", "PvP", "Co-op", "Shared/Split Screen", "Full Controller Support", "DualSense Controllers (USB Only)", "DualSense Controllers"],
        singleplayer=True, online_multiplayer=True, release_date="2023-09-29", last_update= "2024-04-09", user_rating=5.5, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=False, remote_play=True,
        developer="Electronic Arts", publisher="Electronic Arts", age_rating=True, age_rating_score=13, dlc=True, dlc_count=8, award_steam=0,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Japanese", "Korean", "Polish", "Portuguese - Brazil", "Simplified Chinese", "Spanish - Latin America", "Traditional Chinese", "Arabic", "Czech", "Danish", "Dutch", "Norwegian", "Portuguese - Portugal", "Russian", "Swedish", "Turkish"],
        steam_trading_cards=False, min_ram="8GB", min_storage="100GB", controller_support=True)

        yield Juego(name="Unturned", price_range=0.0, discount=False, percentage_discount=0,
        genres=["Free to Play", "Survival", "Zombies", "Multiplayer", "Open World", "Co-op", "Crafting", "Sandbox", "Shooter", "Adventure", "Post-apocalyptic", "First-Person", "Singleplayer", "Looter Shooter", "FPS", "Action", "Massively Multiplayer", "Indie", "Atmospheric", "Casual"],
        categories=["Single-player", "Online PvP", "LAN PvP", "Online Co-op", "LAN Co-op", "Steam Achievements", "Steam Trading Cards", "Steam Workshop", "In-App Purchases", "Steam Cloud", "Valve Anti-Cheat enabled", "Stats", "Includes level editor", "Remote Play on Tablet", "Multiplayer", "PvP", "Co-op", "Cloud Gaming", "Cloud Gaming (NVIDIA)"],
        singleplayer=True, online_multiplayer=True, release_date="2017-07-07", last_update= "2024-04-08", user_rating=8.8, multiplatform=False,
        achievements=True, steam_workshop=True, in_app_purchases=True, active_community_market=True, remote_play=True,
        developer="Smartly Dressed Games", publisher="Smartly Dressed Games", age_rating=False, age_rating_score=0, dlc=True, dlc_count=8, award_steam=0,
        languages=["English"],
        steam_trading_cards=True, min_ram="8GB", min_storage="4GB", controller_support=False)

        yield Juego(name="DayZ", price_range=138.0, discount=False, percentage_discount=0,
        genres=["Survival", "Multiplayer", "Zombies", "Open World", "Action", "PvP", "Shooter", "Massively Multiplayer", "Horror", "Post-apocalyptic", "Simulation", "FPS", "Early Access", "First-Person", "Survival Horror", "Sandbox", "Adventure", "Co-op", "Atmospheric", "Indie"],
        categories=["MMO", "Online PvP", "Online Co-op", "Steam Achievements", "Steam Workshop", "Steam Cloud", "Valve Anti-Cheat enabled", "Multiplayer", "PvP", "Cloud Gaming", "Cloud Gaming (NVIDIA)", "Co-op"],
        singleplayer=True, online_multiplayer=True, release_date="2018-12-13", last_update= "2024-02-20", user_rating=7.5, multiplatform=False,
        achievements=True, steam_workshop=True, in_app_purchases=False, active_community_market=False, remote_play=False,
        developer="Bohemia Interactive", publisher="Bohemia Interactive", age_rating=True, age_rating_score=17, dlc=True, dlc_count=2, award_steam=1,
        languages=["English", "French", "Italian", "German", "Spanish - Spain", "Japanese", "Korean", "Polish", "Portuguese - Brazil", "Simplified Chinese", "Spanish - Latin America", "Traditional Chinese", "Arabic", "Czech", "Danish", "Dutch", "Norwegian", "Portuguese - Portugal", "Russian", "Swedish", "Turkish"],
        steam_trading_cards=True, min_ram="8GB", min_storage="25GB", controller_support=False)
    
        yield Juego(name="DayZ", price_range=0.0, discount=False, percentage_discount=0,
        genres=[],
        categories=[],
        singleplayer=True, online_multiplayer=True, release_date="2013-10-23", last_update= "2024-04-08", user_rating=8.8, multiplatform=True,
        achievements=True, steam_workshop=False, in_app_purchases=True, active_community_market=False, remote_play=True,
        developer="", publisher="", age_rating=False, age_rating_score=0, dlc=False, dlc_count=0, award_steam=0,
        languages=[],
        steam_trading_cards=False, min_ram="8GB", min_storage="25GB", controller_support=True)

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

    
sistema = SistemaRecomendacion()
sistema.reset()
sistema.declare(Fact(price_range=50))  
sistema.declare(Fact(genres=["Single-player","Multiplayer"]))
sistema.declare(Fact(languages=["Spanish","Italian"]))
sistema.declare(Fact(singleplayer=False))
sistema.declare(Fact(online_multiplayer=True))
sistema.declare(Fact(release_date="2015-05-10"))
sistema.run()
