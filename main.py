import numpy as np

planet_moons = {
"mercury": 0,
"venus": 0,
"earth": 1,
"mars": 2,
"jupiter": 79,
"saturn": 82,
"uranus": 27,
"neptune": 14,
"pluto": 5,
"haumea": 2,
"makemake": 1,
"eris": 1
}

total_moons = sum(planet_moons.values());
total_planets = len(planet_moons);
#Sin biblioteca
print(f'Each planet has an average of {total_moons / total_planets} moons')
#Usando bibliotecta y convirtendola en una list
print(f'Each planet has an average of {np.mean(list(planet_moons.values()))} moons')
