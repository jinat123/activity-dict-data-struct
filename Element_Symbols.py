elementssymbols = {
    "Hydrogen": "H",
    "Helium": "He",
    "Lithium": "Li",
    "Beryllium": "Be",
    "Boron": "B",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne"
}

entire_dict_elements = elementssymbols

sixth_element = list(elementssymbols.keys())[5]
sixth_element_symbol = elementssymbols[sixth_element]

eighth_element = list(elementssymbols.keys())[7]
elementssymbols[eighth_element] = "Updated Symbol"

ninth_element = list(elementssymbols.keys())[8]
del elementssymbols[ninth_element]

last_key_value_pair_elements = list(elementssymbols.items())[-1]