softwareversions = {
    "Windows": "11",
    "macOS": "Ventura",
    "Ubuntu": "22.04",
    "Adobe Photoshop": "2024",
    "Microsoft Office": "365",
    "Visual Studio": "2022"
}

entire_dict_software = softwareversions

fourth_software = list(softwareversions.keys())[3]
fourth_software_version = softwareversions[fourth_software]

second_software = list(softwareversions.keys())[1]
softwareversions[second_software] = "Sonoma" # Updated version

fifth_software = list(softwareversions.keys())[4]
del softwareversions[fifth_software]

last_key_value_pair_software = list(softwareversions.items())[-1]