new_planet = ''
planets = []

while new_planet != "done":
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Enter a new planet name, or done if you just finished: ")

print(planets)