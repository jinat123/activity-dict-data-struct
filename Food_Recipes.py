foodsrecipes = {
    "Poutine": "Fries, cheese curds, and gravy",
    "Butter Chicken": "Chicken, tomato sauce, cream, and spices",
    "Sushi": "Vinegared rice, seafood, and vegetables",
    "Tacos": "Tortilla, meat, cheese, lettuce, and salsa",
    "Pancakes": "Flour, milk, eggs, and butter",
    "Caesar Salad": "Romaine lettuce, croutons, Caesar dressing",
    "Pasta Carbonara": "Pasta, eggs, pancetta, and cheese",
    "Ratatouille": "Eggplant, zucchini, tomatoes, and herbs"
}

entire_dict_foods = foodsrecipes

fifth_food = list(foodsrecipes.keys())[4]
fifth_food_recipe = foodsrecipes[fifth_food]

third_food = list(foodsrecipes.keys())[2]
foodsrecipes[third_food] = "Updated recipe with fresh seafood and vegetables"

seventh_food = list(foodsrecipes.keys())[6]
del foodsrecipes[seventh_food]

last_key_value_pair_foods = list(foodsrecipes.items())[-1]