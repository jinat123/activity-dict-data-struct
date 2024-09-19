statescapitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Illinois": "Springfield",
    "Pennsylvania": "Harrisburg",
    "Ohio": "Columbus",
    "Michigan": "Lansing",
    "Georgia": "Atlanta",
    "North Carolina": "Raleigh"
}

entire_dict_states = statescapitals

fourth_state = list(statescapitals.keys())[3]
fourth_state_capital = statescapitals[fourth_state]

ninth_state = list(statescapitals.keys())[8]
statescapitals[ninth_state] = "Updated Capital"

seventh_state = list(statescapitals.keys())[6]
del statescapitals[seventh_state]

last_key_value_pair_states = list(statescapitals.items())[-1]