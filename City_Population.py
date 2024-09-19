citypopulation = {'citypop1': 'tokyo', 'citypop2': 'delhi', 'citypop3': 'shanghai', 'citypop4': 'dhaka', 'citypop5': 'saopaulo', 'citypop6': 'mexicocity', 'citypop7': 'cairo', 'citypop8': 'beijing', 'citypop9': 'mumbai', 'citypop10': 'osaka'}

print(citypopulation)

print("6th population city:", dict['dhaka'])

citypopulation['citypop3'] = 'dhaka'

del citypopulation['citypop9']

lastcitypopulation = list(citypopulation.items())[-1]
print("last key value of city population:", lastcitypopulation)