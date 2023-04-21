#All about Files..
'''
#the with keykeyword actaully opens and closes the file as well.
from math import pi
with open('python_example_files/pi_digits.txt') as fileObj:
    content=fileObj.read()
    print(content.strip())
i=0
with open('python_example_files/pi_digits.txt') as fileObj:
    for line in fileObj:
        print(f'For line {i} the content is {line.rstrip()}  ')
        i+=1
#Making a list out of the line and try to write the value of PI together
lines_list=[]
str=''
with open('python_example_files/pi_digits.txt') as fileObj:
    for line in fileObj:
        stripped_line = line.strip() #strip does rstriip and lstrip
        print(stripped_line)
        lines_list.append(stripped_line)
        str =str+stripped_line
print(lines_list)
print(str)
print(pi)

#write to a fil
with open('python_example_files/text_file.txt','w') as fileObj:
    fileObj.write('To be is not to be!')
lov =[]
with open('python_example_files/text_file.txt') as fileObj:
    lov =fileObj.readlines()
    print(f'Reading after writing : {lov}')
#Exception Handling

try:
    9/0
except ZeroDivisionError:
    print('Bad division make sure you are not dividing by zero')
except FileExistsError:
    print('Fake exception handling should not even come here..')
#Count the number of works in a file 'python_example_files/pi_digits.txt')

class FileExample:
    def __init__(self, filenameWithPath,whatYouWantToFind):
        self.filename = filenameWithPath
        self.searchString= whatYouWantToFind

    def count_words_in_whole_file(self):
        try:
            with open(self.filename) as fileObj:
                file_content = fileObj.read()
                print(f'File name {self.filename} has  {len(file_content.split())} , words')
        except FileExistsError:
            print(f'File Name {self.filename} does not exist')
        except FileNotFoundError:
            print(f'File Name {self.filename} not found')

    def num_of_occurances(self):
        try:
            with open(self.filename) as fileObj:
                file_content = fileObj.read()
                count=0
                if self.searchString in file_content:
                    count = file_content.count(self.searchString)
                else:
                    print(f'Search string {self.searchString[0:2]} does not exist')
                print(f'File name {self.filename} has  {len(file_content.split())} , words and the number of times {self.searchString} occurs in {count}')

        except FileExistsError:
            print(f'File Name {self.filename} does not exist')
        except FileNotFoundError:
            print(f'File Name {self.filename} not found')

file = FileExample('python_example_files/devil_tales.txt','the ')
file.num_of_occurances()


10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message,
 “I know your favorite number! It’s _____.”

10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number 
and store it in a file. Run the program twice to see that it works.

10-13. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not 
the person who last used the program.

Before printing a welcome back message in greet_user(), ask the user if this is the correct username. If it’s not, call get_new_username() to get the correct username.
'''




import json
#JSON magic
class FavNumberCollector:
    def findNumber(self,numberTofind):
        numbers ={}
        with open('../python_example_files/fav_number.json') as f:
            numbers = json.load(f)
            if numberTofind in numbers:
                print('FOund !!!')
            else:
                print(list(numbers.values()))
                if numberTofind in  numbers.values():
                        print('FOund in value !!!')

    def addNumberTofile(self, name, number):
        numbers ={}
        with open('../python_example_files/fav_number.json') as f:
            numbers = json.load(f)
            numbers[name] = number
            print(numbers)
        with open('../python_example_files/fav_number.json', 'w') as f:
            json.dump(numbers, f)

    def collectNumber9999(self):
        with open('../python_example_files/fav_number.json', 'w') as f:
            lov = {}
            print('Will be collecting names and fav numbers...')
            while 'Y' != input('Do you want to quit Y/N ? '):
                name = input('What is your name ?')
                fav_number = input('What is your fav number ?')
                lov[name] = fav_number
            json.dump(lov, f)


ref = FavNumberCollector()
ref.addNumberTofile('sam',14)
ref.addNumberTofile('ddd',16)
ref.findNumber(16)
'''

with open('python_example_files/jsont_file.txt','w') as f:
    lov = {'Sam':'M', 'Nikki':'Mu', 'Swa' : 'Mukherjee'}
    json.dump(lov,f)

with open('python_example_files/jsont_file.txt','r') as fileObj:
    str = json.load(fileObj)
    print(str)
'''