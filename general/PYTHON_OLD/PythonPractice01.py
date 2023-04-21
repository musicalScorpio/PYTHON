
# Online Python - IDE, Editor, Compiler, Interpreter

#Tuple Example

tuple_example = (1,2,3,4)
print (tuple_example[3])
print (tuple_example)
print (tuple_example[-2])

#Find all the divisors of a number
divisors=()
x=24
for i in range(1,x):
    if x%i==0:
        divisors =divisors+(i,)
print (divisors)
print (divisors [1:3])

#=================

#Lists
people =['Sam','Nikki']

print (people)
people[1] ='Maa'
print (people)
people.append('Sammy')
people.sort()
print (people)

#=================

#Dictionary
map_example = {'1-1':"One", 2:"Two"}
print (map_example['1-1'])
#print (map_example[1])

for c in map_example.keys():
    print("######")
    print(c)
    print("######")

for c in map_example.values():
    print("######")
    print(c)
    print("######")
 
print ('Hello World!')

#Do a translation

map_of_words = {'sam':'mas', 'nikki':'ikkin' , 'is':'si' ,'awesome':'emosrwa'}

def translatedWord (word):
    print('calling method for-> ' +word)
    if word in map_of_words:
        return map_of_words[word]
    else:
        return word

def translateSentence (sentence):
    word =""
    translatedSentenceVar =""
    sentence = sentence 
    for c in sentence:
        if c !=' ':
            word = word +c
        else:
            translatedSentenceVar = translatedSentenceVar + ' ' + translatedWord(word) 
            word =""
    return translatedSentenceVar[1:] + ' '+translatedWord(word)

print (translateSentence('nikki is awesome'))

##Recursion
#Calculate b to the power of nikki

def calculatePower( num, power):
    if power == 0:
        return 1 
    else :
        num = num * calculatePower(num,power -1)
        return num
print ('Calculating power ' + str(calculatePower (2,3)))
    
def towerOfHahoi (numberOfDisks, fr, to, spare):
    if numberOfDisks ==1:
        print ( ' from '+str(fr) + ' to '+str(to))
    else:
        towerOfHahoi(numberOfDisks-1,'fr','sp','to')
        towerOfHahoi(1,'fr','to','sp')
        towerOfHahoi(numberOfDisks-1,'sp','to','fr')
    
print ('Hanoi ' + str(towerOfHahoi (2,'From','To','Spare')))


#Find palindrone in a word

def isPalidrome (word, position1, position2):
    i=position1=0
    j=len(word)-1
    if(word[position1] == word[position2]):
        return True
    if (word[position1] != word[position2]):
        assert False
    else :
        if(position1 != position2):
            print ("!!!!!")
            isPalidrome(word,i+1,j-1)
        else:
            return True
        
isPalidrome('SONOS',0,5)




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






