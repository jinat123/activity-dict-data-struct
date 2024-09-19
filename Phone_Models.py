phonesmanufacturers = {
    "iPhone 13": "Apple",
    "Galaxy S21": "Samsung",
    "Pixel 6": "Google",
    "Xperia 1 III": "Sony",
    "OnePlus 9": "OnePlus",
    "Mi 11": "Xiaomi",
    "P40 Pro": "Huawei",
    "Moto G Power": "Motorola",
    "Oppo Find X3": "Oppo",
    "Nokia 8.3": "Nokia"
}

entire_dict_phones = phonesmanufacturers

second_phone = list(phonesmanufacturers.keys())[1]
second_phone_manufacturer = phonesmanufacturers[second_phone]

eighth_phone = list(phonesmanufacturers.keys())[7]
phonesmanufacturers[eighth_phone] = "Updated Manufacturer"

sixth_phone = list(phonesmanufacturers.keys())[5]
del phonesmanufacturers[sixth_phone]

last_key_value_pair_phones = list(phonesmanufacturers.items())[-1]