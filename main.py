from datetime import date

print(date.today())
print("Today's date is: " + str(date.today().min))

parsecs = 11
lightyears = parsecs * 3.26
print(F"{str(parsecs)} parsecs is {str(lightyears)} lightyears")