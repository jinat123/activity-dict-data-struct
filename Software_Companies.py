softwarecompany = {
    "Microsoft": "Redmond, Washington, USA",
    "Apple": "Cupertino, California, USA",
    "Google": "Mountain View, California, USA",
    "Amazon": "Seattle, Washington, USA",
    "Facebook": "Men lo Park, California, USA",
    "Oracle": "Austin, Texas, USA",
    "Salesforce": "San Francisco, California, USA",
    "Adobe": "San Jose, California, USA",
    "Intel": "Santa Clara, California, USA",
    "IBM": "Armonk, New York, USA"
}

entire_dict_software = softwarecompany

third_company = list(softwarecompany.keys())[2]
third_company_headquarters = softwarecompany[third_company]


eighth_company = list(softwarecompany.keys())[7]
softwarecompany[eighth_company] = "Updated Headquarters"


ninth_company = list(softwarecompany.keys())[8]
del softwarecompany[ninth_company]

last_key_value_pair_software = list(softwarecompany.items())[-1]