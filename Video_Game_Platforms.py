videogamesplatforms = {
    "The Legend of Zelda: Breath of the Wild": "Nintendo Switch",
    "God of War": "PlayStation",
    "Minecraft": "Multiple Platforms",
    "Halo: Infinite": "Xbox",
    "Cyberpunk 2077": "Multiple Platforms",
    "Fortnite": "Multiple Platforms",
    "The Witcher 3": "Multiple Platforms",
    "Super Mario Odyssey": "Nintendo Switch"
}

entire_dict_games = videogamesplatforms

second_game = list(videogamesplatforms.keys())[1]
second_game_platform = videogamesplatforms[second_game]

sixth_game = list(videogamesplatforms.keys())[5]
videogamesplatforms[sixth_game] = "Updated Platform"

fourth_game = list(videogamesplatforms.keys())[3]
del videogamesplatforms[fourth_game]

last_key_value_pair_games = list(videogamesplatforms.items())[-1]