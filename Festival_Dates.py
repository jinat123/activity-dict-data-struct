festivalsdates = {
    "Christmas": "December 25",
    "New Year's Day": "January 1",
    "Diwali": "November 12",
    "Eid al-Fitr": "April 21",
    "Hanukkah": "December 18",
    "Halloween": "October 31",
    "Thanksgiving": "November 24",
    "Chinese New Year": "February 10",
    "Easter": "April 9",
    "Holi": "March 8"
}

entire_dict_festivals = festivalsdates

third_festival = list(festivalsdates.keys())[2]
third_festival_date = festivalsdates[third_festival]

seventh_festival = list(festivalsdates.keys())[6]
festivalsdates[seventh_festival] = "Updated Date"

fifth_festival = list(festivalsdates.keys())[4]
del festivalsdates[fifth_festival]

last_key_value_pair_festivals = list(festivalsdates.items())[-1]