from os import system
import time


first_number = int(input('Type the first number: '));
second_number = int(input('Type the second number: ')); 
print("The sum is: ", first_number + second_number);

#Timeout 2s to clear the console
time.sleep(2);
system("cls");

first_number = int(input('Type the first number: '));
second_number = int(input('Type the second number: ')); 
print("The dif is: ", first_number - second_number);