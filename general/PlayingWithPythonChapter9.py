from Car import Car
#What we are saying here is import Car.py and then import the Car class from it
from Car import ElectricCar
from random import randint as r
from random import choice
from  Car import Battery
'''

9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a
default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served,
and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number
nd print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you
like that could represent how many customers were served in, say, a day of business.

9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts()
that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

'''
class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type,no_of_cust=0):
        self.resturant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.no_of_cust=0
    def describe_restaurant(self):
        print(f'The restaurant {self.resturant_name} is of type {self.cuisine_type} and number of customers served is {self.no_of_cust}')
    def open_restaurant(self):
        print('Resturant is open !!')
    def set_number_served(self):
        self.no_of_cust+=1

res = Restaurant('A','B')
res.describe_restaurant()

for var in range(15):
    res.set_number_served()
res.describe_restaurant()



class User:
    def __init__ (self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.increment_login_attempt=0
    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name} and your login attempt is {self.increment_login_attempt}')

    def increment_login_attempts(self):
        self.increment_login_attempt +=1
    def reset_login_attempts(self):
        self.increment_login_attempt=0

usr = User('Sam','Mukherjee')
usr.greet_user()

for var in range(15):
    usr.increment_login_attempts()
usr.greet_user()
usr.reset_login_attempts()
usr.greet_user()


#Notice the imported classes at the Top
car = Car('Ford','Explorer',2017)
car.fill_gas_tank()

my_tesla = ElectricCar('Ford', 'Mustang', 2019)
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
print(my_tesla.get_descriptive_name())

#See the line a the top where I am importing random
print(r(1,51))
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f'First up is {choice(players)}')

#=========
'''
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 
and the number of sides the die has. Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.

9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four numbers or letters from the list and print a message saying that any ticket 
matching these four numbers or letters wins a prize.

9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers 
until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.

9-16. Python Module of the Week: One excellent resource for exploring the Python standard library is a site called Python Module of the Week. Go to https://pymotw.com/ and look at the table of contents. 
Find a module that looks interesting to you and read about it, perhaps starting with the random module.

'''
class Dice:
    def __init__(self, sides):
        self.sides=sides
    def roll_dice(self):
        print(f'Number rolled is {r(1,self.sides)} with sides {self.sides}')

dice = Dice(6)
dice.roll_dice()

dice = Dice(10)
for var in range(10):
    dice.roll_dice()

dice = Dice(20)
for var in range(10):
    dice.roll_dice()

tuple001 = ('31', '52', '74', '67', '55')
tuple002 = ('Z', 'F', 'R', 'G', 'A')
randomLetter = []

for var in range(4):
    randomLetter.append(choice(tuple001))
    randomLetter.append(choice(tuple002))

print(f'Any ticket matching these {randomLetter} wins!')
lott_tckt = input('Type in your lottery ticket please ?')

for var in range(1000):
    match = (lott_tckt == choice(tuple001))
    if match:
        print(f'We got LUCKY today, you win, your ticket is  {lott_tckt} and number of try is {var}')
        break
    elif (lott_tckt == choice(tuple002)):
        print(f'We got LUCKYYY today, you win, your ticket is  {lott_tckt} and number of try is {var}')
        break



