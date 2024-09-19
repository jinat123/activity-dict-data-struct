coffeetypesdescriptions = {
    "Espresso": "A strong coffee brewed by forcing hot water under pressure through finely ground coffee beans.",
    "Latte": "A creamy coffee made with espresso and steamed milk.",
    "Cappuccino": "A balanced combination of espresso, steamed milk, and foam.",
    "Americano": "Espresso diluted with hot water for a smoother taste.",
    "Macchiato": "Espresso with a small amount of steamed milk, often just a dash.",
    "Mocha": "A blend of espresso, chocolate, and steamed milk, topped with whipped cream.",
    "Flat White": "An espresso-based coffee with microfoam milk.",
    "Ristretto": "A short shot of espresso, more concentrated than a regular espresso.",
    "Affogato": "Espresso poured over a scoop of vanilla ice cream.",
    "Iced Coffee": "Chilled coffee served over ice, sometimes with milk or flavorings."
}

entire_dict_coffee = coffeetypesdescriptions

fourth_coffee = list(coffeetypesdescriptions.keys())[3]
fourth_coffee_description = coffeetypesdescriptions[fourth_coffee]

eighth_coffee = list(coffeetypesdescriptions.keys())[7]
coffeetypesdescriptions[eighth_coffee] = "Updated description for a short, concentrated espresso."

fifth_coffee = list(coffeetypesdescriptions.keys())[4]
del coffeetypesdescriptions[fifth_coffee]

last_key_value_pair_coffee = list(coffeetypesdescriptions.items())[-1]