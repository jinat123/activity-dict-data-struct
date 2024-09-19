athletesachievements = {
    "Michael Jordan": "6 NBA Championships",
    "Serena Williams": "23 Grand Slam Titles",
    "Usain Bolt": "8 Olympic Gold Medals",
    "Muhammad Ali": "3-time World Heavyweight Champion",
    "Lionel Messi": "7 Ballon d'Or Awards",
    "Michael Phelps": "23 Olympic Gold Medals",
    "Roger Federer": "20 Grand Slam Titles",
    "Tiger Woods": "15 Major Golf Championships"
}

entire_dict_athletes = athletesachievements

fifth_athlete = list(athletesachievements.keys())[4]
fifth_athlete_achievement = athletesachievements[fifth_athlete]

third_athlete = list(athletesachievements.keys())[2]
athletesachievements[third_athlete] = "Updated Achievement"

seventh_athlete = list(athletesachievements.keys())[6]
del athletesachievements[seventh_athlete]

last_key_value_pair_athletes = list(athletesachievements.items())[-1]