
# Online Python - IDE, Editor, Compiler, Interpreter

#Implement binary search
sorted_array_as_input = input('Enter a sorted list')
search_string= int(input('Enter search string'))

sorted_array = list (sorted_array_as_input)
print (len(sorted_array))
upper =len(sorted_array)-1
lower = 0
middle= 0
while (lower<upper):
    if search_string == sorted_array[middle]:
        print (f'Found It !!{search_string}')
        break;
    middle = int((lower+upper)/2)
    if int(search_string) < int(sorted_array[middle]) :
        print ("middle",middle )
        upper=middle-1
    elif int(search_string) > int(sorted_array[middle]):
        print ("middle",middle )
        lower =middle+1
    else:
        print (f'Found It !!{search_string}')
        break;


#print ('#######################')



#Print even number from 1 -100
for n in range (2,100,2):
    print (n)
def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))


print(f'Sum of {a} and {b} is {sum(a, b)}')

def withEpsilon(a, b, epsilon):
    assert type (a) ==int
    return abs(a - b)<=epsilon
print (withEpsilon(a, b,1))

def sumFoDigits (string01):
    sum01 =0
    for c in str(string01):
        sum01 +=  int(c)
    print (sum01)
    #Slicing (Slices from 1 to y-1)
    print (f'Slicing : {str(string01)[0:2]}')
    #Will find the posiiton of the match
    print (f'Finding : {str(string01).find("9")}')

sumFoDigits(a)






