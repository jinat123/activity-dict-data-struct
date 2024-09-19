holidaysdates = {
    "New Year's Day": "January 1",
    "Valentine's Day": "February 14",
    "Easter": "April 17",   
    "Independence Day": "July 4",
    "Halloween": "October 31",
    "Thanksgiving": "November 24",
    "Christmas": "December 25",
    "Labor Day": "September 5",
    "Memorial Day": "May 30",
    "Mother's Day": "May 8"
}

entire_dict_holidays = holidaysdates

fourth_holiday = list(holidaysdates.keys())[3]
fourth_holiday_date = holidaysdates[fourth_holiday]

ninth_holiday = list(holidaysdates.keys())[8]
holidaysdates[ninth_holiday] = "Updated Date"

second_holiday = list(holidaysdates.keys())[1]
del holidaysdates[second_holiday]

last_key_value_pair_holidays = list(holidaysdates.items())[-1]