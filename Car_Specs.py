carmodelsengines = {
    "Tesla Model S": "Electric, Dual Motor",
    "Ford Mustang": "5.0L V8",
    "Chevrolet Camaro": "6.2L V8",
    "BMW M3": "3.0L Twin-Turbo Inline-6",
    "Audi A4": "2.0L Turbocharged Inline-4",
    "Mercedes-Benz C-Class": "2.0L Turbocharged Inline-4",
    "Honda Civic": "1.5L Turbocharged Inline-4",
    "Toyota Camry": "2.5L Inline-4",
    "Porsche 911": "3.0L Twin-Turbo Flat-6",
    "Nissan GT-R": "3.8L Twin-Turbo V6"
}

entire_dict_cars = carmodelsengines

fourth_car_model = list(carmodelsengines.keys())[3]
fourth_car_specifications = carmodelsengines[fourth_car_model]

ninth_car_model = list(carmodelsengines.keys())[8]
carmodelsengines[ninth_car_model] = "Updated Engine Specifications"

fifth_car_model = list(carmodelsengines.keys())[4]
del carmodelsengines[fifth_car_model]

last_key_value_pair_cars = list(carmodelsengines.items())[-1]