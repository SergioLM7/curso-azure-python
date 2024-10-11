rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

if 'december' in rainfall:
    rainfall['december'] += 1
else:
    rainfall['december'] = 1

for key, value in rainfall.items():
    print(f'{key}: {value}cm')

print(f'There was {sum(rainfall.values())}cm in the last quarter.')