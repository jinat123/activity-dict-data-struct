appsratings = {
    "WhatsApp": 4.5,
    "Instagram": 4.3,
    "Facebook": 4.1,
    "TikTok": 4.4,
    "Spotify": 4.6,
    "Snapchat": 4.2,
    "YouTube": 4.7,
    "Twitter": 4.0,
    "Zoom": 4.4,
    "Pinterest": 4.5
}

entire_dict_apps = appsratings

sixth_app = list(appsratings.keys())[5]
sixth_app_rating = appsratings[sixth_app]

eighth_app = list(appsratings.keys())[7]
appsratings[eighth_app] = 4.2  # Updated rating

ninth_app = list(appsratings.keys())[8]
del appsratings[ninth_app]

last_key_value_pair_apps = list(appsratings.items())[-1]