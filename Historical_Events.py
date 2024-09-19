historicaleventsyears = {
    "Moon Landing": 1969,
    "World War II Ends": 1945,
    "Fall of the Berlin Wall": 1989,
    "American Revolution": 1776,
    "French Revolution": 1789,
    "Civil Rights Act": 1964,
    "First Industrial Revolution": 1760,
    "Declaration of Independence": 1776
}

entire_dict_events = historicaleventsyears

second_event = list(historicaleventsyears.keys())[1]
second_event_year = historicaleventsyears[second_event]

seventh_event = list(historicaleventsyears.keys())[6]
historicaleventsyears[seventh_event] = 1775  # Updated year

fifth_event = list(historicaleventsyears.keys())[4]
del historicaleventsyears[fifth_event]

last_key_value_pair_events = list(historicaleventsyears.items())[-1]