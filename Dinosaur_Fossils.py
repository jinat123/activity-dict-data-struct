dinosaursfossils = {
    "Tyrannosaurus Rex": "North America",
    "Stegosaurus": "Western USA",
    "Velociraptor": "Mongolia",
    "Triceratops": "North America",
    "Brachiosaurus": "North America",
    "Spinosaurus": "North Africa",
    "Allosaurus": "North America"
}

entire_dict_dinosaurs = dinosaursfossils

fourth_dinosaur = list(dinosaursfossils.keys())[3]
fourth_dinosaur_location = dinosaursfossils[fourth_dinosaur]

second_dinosaur = list(dinosaursfossils.keys())[1]
dinosaursfossils[second_dinosaur] = "Updated Location"

sixth_dinosaur = list(dinosaursfossils.keys())[5]
del dinosaursfossils[sixth_dinosaur]

last_key_value_pair_dinosaurs = list(dinosaursfossils.items())[-1]