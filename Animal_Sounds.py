animalsounds = {'lion': 'roar', 'bee': 'buzz', 'camel': 'grunt', 'cicada': 'chirp', 'crane': 'clang', 'crow': 'caw', 'dog': 'bark', 'elephant': 'trumpet'}

print(animalsounds)

print("4th sound of animal:", dict['chirp'])

animalsounds['elephant'] = 'trumpet'

del animalsounds['crane']

lastanimalsound = list(animalsounds.items())[-1]
print("last key value of animalsound:", lastanimalsound)