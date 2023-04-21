
# Online Python - IDE, Editor, Compiler, Interpreter
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






