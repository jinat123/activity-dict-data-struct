universitiescourses = {
    "Harvard University": "Law",
    "Stanford University": "Computer Science",
    "MIT": "Engineering",
    "Oxford University": "Philosophy",
    "University of Cambridge": "Mathematics",
    "Princeton University": "Economics",
    "Yale University": "Political Science",
    "University of Chicago": "Sociology"
}

entire_dict_universities = universitiescourses

third_university = list(universitiescourses.keys())[2]
third_university_course = universitiescourses[third_university]

fifth_university = list(universitiescourses.keys())[4]
universitiescourses[fifth_university] = "Updated Course"

seventh_university = list(universitiescourses.keys())[6]
del universitiescourses[seventh_university]

last_key_value_pair_universities = list(universitiescourses.items())[-1]