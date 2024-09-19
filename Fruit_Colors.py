fruitcolor = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Grape": "Purple",
    "Orange": "Orange",
    "Kiwi": "Green",
    "Blueberry": "Blue",
    "Strawberry": "Red",
    "Lemon": "Yellow"
}

entire_dict_fruits = fruitcolor

sixth_fruit = list(fruitcolor.keys())[5]
sixth_fruit_color = fruitcolor[sixth_fruit]

fourth_fruit = list(fruitcolor.keys())[3]
fruitcolor[fourth_fruit] = "Updated Color"

seventh_fruit = list(fruitcolor.keys())[6]
del fruitcolor[seventh_fruit]

last_key_value_pair_fruits = list(fruitcolor.items())[-1]