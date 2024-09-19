carbrands = { "Toyota": "Japan", "Ford": "USA", "BMW": "Germany", "Ferrari": "Italy", "Hyundai": "South Korea", "Volvo": "Sweden", "Renault": "France", "Tata": "India", "Nissan": "Japan", "Chevrolet": "USA"}

entire_dict = carbrands

thirdcarbrand = list(carbrands.keys())[2]
thirdcarorigin = carbrands[thirdcarbrand]

seventhcarbrand = list(carbrands.keys())[6]
carbrands[seventhcarbrand] = "Updated Country"

eighthcarbrand = list(carbrands.keys())[7]
del carbrands[eighthcarbrand]

lastkeyvaluepair = list(carbrands.items())[-1]