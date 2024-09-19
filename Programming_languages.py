programlanguage = {'pgmlanguage1': 'sql', 'pgmlanguage2': 'java', 'pgamlanguage3': 'apl', 'pgmlanguage4': 'logo', 'pgmlanguage5': 'tex', 'pgmlanguage6': 'fortran', 'pgmlanguage7': 'basic'}

print(programlanguage)

print("4th programming language:", dict['pgmlanguage4'])

programlanguage['pgmlanguage6'] = 'fortran'

del programlanguage['pgmlanguage2']

lastprogramlanguage = list(programlanguage.items())[-1]
print("last key value of programlanguage:", lastprogramlanguage)