planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#mercury_index = planets.index("Mercury")
#print(planets)
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12];
bus_weight = 124054 # in Newtons, on Earth

#Devuelve el indice 
for i in range(len(planets)):
        print(f"On {planets[i]}, a double-decker bus weighs {int((bus_weight * gravity_on_planets[i])/9.81)}kg")


print("On Earth, a double-decker bus weighs", int(bus_weight/9.81), "kg")
#print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")