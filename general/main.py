#@author Sam Mukherjee
# This is a helper class that can call any REST APIs under the sun.

#moving lists from one to another


listexample = ['Orange' ,'Apple','Guava']
listexample001 =[]

i=0
while (len(listexample001) != len (listexample)):
    listexample001.append(listexample[i])
    i=i+1

#print ('My list is  : ' + str(listexample001))

#Or another way of doing this

while (listexample):
    listexample001.append(listexample.pop())

#print ('My list is 1 : ' + str(listexample001))

#Now removing an items from a list until it is not present

listofitems =['A', "A", 'B','A', "A", 'B','A', "A", 'B']

while 'A' in listofitems:
    listofitems.remove('A')

#print(listofitems)

'''

7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message 
for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished 
sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

'''
'''
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of 
your program to print a message saying the deli has run out of pastrami, 
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
'''

sandwich_orders=['BLT', 'Tuna Sandwitch Pastrami','Fish Sandwitch', 'Burger- Chicken Pastrami', 'Burger - Beef Pastrami']
finished_sandwiches=[]

print('Sandwitch store ran out of  Pastrami')
while (sandwich_orders):
    item = sandwich_orders.pop()
    if not item.endswith('Pastrami'):
        finished_sandwiches.append('I made your '+str(item))

print('All sandwitches are made now '+str(finished_sandwiches))

'''
7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could 
visit one place in the world, where would you go? Include a block of code that prints the results of the poll.


mapOfNameAndPlace ={}


done=''
while done !='Y':
    name = input("Hi there what is your name ? ")
    place = input("Where would you love to go for your vacation ? ")
    done = input("Are you done say Y or N ?")
    mapOfNameAndPlace[name]=place

for x,y in mapOfNameAndPlace.items():
    print (f'{x} wants to go to dream vaca at {y}')

'''



















#takign inputs
'''
age = input("How old are you? ")
print (f"Your age is {age}")

if int(age)<18:
    print('You are not old enough')
else:
    print ('You are good to go')
'''
#Loops
'''
current_number =1
while current_number <=10:
    current_number+=1
    print(current_number)
'''

'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = "Hello !!"
while message != 'quit':
    message = input(prompt)
    if(message!='quit'):
        print(message)
'''



items = ['Orange' ,'Apple','Guava']

#Making it capital case first letter
#print (items[0].title())
#print (items[-1].title())
#print (items[-3].title())

message = f"My first fruit was a {items[0].title()}."
#print (message)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles_copy = motorcycles.copy()

motorcycles.sort()

#print("Sorted : " + str(motorcycles) + " and size is " + str(len(motorcycles)))
#print('Original : ' + str(motorcycles_copy))

motorcycles.append('abc')
motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.pop()
#print(motorcycles)

motorcycles.remove('ducati')
#print(motorcycles)

'''    
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(1+2+3)

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
'''