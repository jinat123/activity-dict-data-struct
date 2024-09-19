currenciessymbols = {
    "US Dollar": "$",
    "Euro": "€",
    "British Pound": "£",
    "Japanese Yen": "¥",
    "Indian Rupee": "₹",
    "Australian Dollar": "A$",
    "Canadian Dollar": "C$",
    "Swiss Franc": "CHF",
    "Chinese Yuan": "¥",
    "South Korean Won": "₩"
}

entire_dict_currencies = currenciessymbols

fifth_currency = list(currenciessymbols.keys())[4]
fifth_currency_symbol = currenciessymbols[fifth_currency]

ninth_currency = list(currenciessymbols.keys())[8]
currenciessymbols[ninth_currency] = "Updated Symbol"

third_currency = list(currenciessymbols.keys())[2]
del currenciessymbols[third_currency]

last_key_value_pair_currencies = list(currenciessymbols.items())[-1]