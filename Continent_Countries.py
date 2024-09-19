continentscountries = {
    "Africa": ["Nigeria", "South Africa", "Egypt"],
    "Asia": ["China", "India", "Japan"],
    "Europe": ["Germany", "France", "Italy"],
    "North America": ["United States", "Canada", "Mexico"],
    "South America": ["Brazil", "Argentina", "Chile"],
    "Australia": ["Australia", "New Zealand", "Fiji"]
}

entire_dict_continents = continentscountries

fourth_continent = list(continentscountries.keys())[3]
fourth_continent_countries = continentscountries[fourth_continent]

fifth_continent = list(continentscountries.keys())[4]
continentscountries[fifth_continent] = ["Updated Country1", "Updated Country2", "Updated Country3"]

sixth_continent = list(continentscountries.keys())[5]
del continentscountries[sixth_continent]

last_key_value_pair_continents = list(continentscountries.items())[-1]