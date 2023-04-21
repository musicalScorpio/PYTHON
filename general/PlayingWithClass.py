#Chapter 8 Functions of the oriely book Python crash course


'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a
cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant()
that prints a message indicating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant()
for each instance.

9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are
typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called
greet_user() that prints a personalized greeting to the user.

'''
class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.resturant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f'The restaurant {self.resturant_name} is of type {self.cuisine_type}')
    def open_restaurant(self):
        print('Resturant is open !!')

res = Restaurant('A','B')
res.describe_restaurant()


class User:
    def __init__ (self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')

usr = User('Sam','Mukherjee')
usr.greet_user()
