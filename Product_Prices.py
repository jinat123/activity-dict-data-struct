productsprices = {
    "Laptop": 1200,
    "Smartphone": 800,
    "Tablet": 400,
    "Headphones": 150,
    "Smartwatch": 250,
    "Camera": 900,
    "Monitor": 300,
    "Keyboard": 100,
    "Mouse": 50,
    "Printer": 200
}

entire_dict_products = productsprices

fourth_product = list(productsprices.keys())[3]
fourth_product_price = productsprices[fourth_product]

ninth_product = list(productsprices.keys())[8]
productsprices[ninth_product] = 55  # Updated price

sixth_product = list(productsprices.keys())[5]
del productsprices[sixth_product]

last_key_value_pair_products = list(productsprices.items())[-1]