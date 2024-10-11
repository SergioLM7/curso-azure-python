def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(round(days_to_complete(43223, 13)));

def generate_report(main_tank,external_tank,hydrogen_tank):
    return f"Full Report:\n   Main Tank: {main_tank}\n   External Tank: {external_tank}\n   Hydrogen Tank: {hydrogen_tank}"

print(generate_report(78,89,98))

from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Earth"))

#kwargs argumentos de palabra clave variable
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")


#Ejercicio 
def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main = 50, external = 100, emergency = 60)