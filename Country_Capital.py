countrycapital = {'capital1': 'kabu', 'capital2': 'minsk', 'capital3': 'kingstown', 'capital4': 'singapore', 'capital5': 'seoul', 'capital6': 'budapest', 'capital7': 'berlin', 'capital8': 'bishkek', 'capital9': 'riga', 'capital10': 'london', 'capital11': 'taipei', 'capital12': 'suva'}

print(countrycapital)

print("5th capital country:", dict['seoul'])

countrycapital['capital8'] = 'bishkek'

del countrycapital['capital11']

lastcountry = list(countrycapital.items())[-1]
print("Last key value of country capital:", lastcountry)