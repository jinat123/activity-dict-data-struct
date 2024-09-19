studentgrades = {'Freddy': 'A', 'Alice': 'B', 'Lawrence': 'C', 'Kevin': 'D', 'Joseph': 'F'}

print(studentgrades)

print("grade of 1st student:", dict['Freddy'])

studentgrades['Freddy'] = 'A'

del studentgrades['Joseph']

laststudent = list(studentgrades.items())[-1]
print("last key value of studentgrade:", laststudent)