sportseventsyears = {
    "FIFA World Cup": 2022,
    "Olympic Games": 2021,
    "Super Bowl": 2023,
    "Wimbledon": 2022,
    "Tour de France": 2022,
    "NBA Finals": 2023,
    "Cricket World Cup": 2019
}

entire_dict_sports = sportseventsyears

third_event = list(sportseventsyears.keys())[2]
third_event_year = sportseventsyears[third_event]

sixth_event = list(sportseventsyears.keys())[5]
sportseventsyears[sixth_event] = 2024  # Updated year

fifth_event = list(sportseventsyears.keys())[4]
del sportseventsyears[fifth_event]

last_key_value_pair_sports = list(sportseventsyears.items())[-1]