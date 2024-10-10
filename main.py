#Exercise 4 inputs and conversions
first_planet_input = input('Enter the distance from the sun for the first planet in km: ')

while not first_planet_input.isnumeric():
    first_planet_input = input('Enter the distance from the sun for the first planet in km: ')

first_planet = int(first_planet_input);

second_planet_input = input('Enter the distance from the sun for the second planet in km: ')
while not second_planet_input.isnumeric():
    second_planet_input = input('Enter the distance from the sun for the second planet in km: ')

second_planet = int(second_planet_input);
distance_km = abs(first_planet - second_planet);
print(distance_km)