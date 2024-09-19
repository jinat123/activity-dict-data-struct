sportsplayers = {
    "Soccer": "Lionel Messi",
    "Basketball": "Michael Jordan",
    "Tennis": "Roger Federer",
    "Cricket": "Sachin Tendulkar",
    "Golf": "Tiger Woods",
    "Boxing": "Muhammad Ali",
    "Swimming": "Michael Phelps",
    "Baseball": "Babe Ruth",
    "Formula 1": "Lewis Hamilton",
    "Rugby": "Jonah Lomu"
}

entire_dict_sports = sportsplayers

fourth_sport = list(sportsplayers.keys())[3]
fourth_sport_player = sportsplayers[fourth_sport]

sixth_sport = list(sportsplayers.keys())[5]
sportsplayers[sixth_sport] = "Updated Player"

tenth_sport = list(sportsplayers.keys())[9]
del sportsplayers[tenth_sport]

last_key_value_pair_sports = list(sportsplayers.items())[-1]