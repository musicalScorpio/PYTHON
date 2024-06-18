
# list comprehensions in Python lets you split a line in one line code
txt = ''' Eight dollars a week or a million a year - what is the difference? A mathematician or a wit would give you
 the wrong answer. The magi brought valuable gifts, but that was not among them. - The Gift of the Magi, O'Henry'''

word_lists = [[w.replace(',','')  for w in line.split() if w not in ['-']]  for line in txt.replace('?','.').split('.')]
print(word_lists)
print(len(word_lists))

#Lists
my_list  = ['Pay bills', 'Tidy up', 'Walk the dog']
print(my_list[0:2])
print(my_list[-1])
print(my_list[:2])
print(my_list[:])
print(my_list[1:])

#DeQ
from collections import deque
queue = deque(my_list)
queue.append('Wash Car')
print(f'Q =  Q {queue}')
print(f'removing the lestmost item of the  Q {queue.popleft()}')
print(f'Printing the contents of the Q {queue}')

#Using a list as a stack
my_list = ['Pay bills', 'Tidy up', 'Walk the dog', 'Go to the pharmacy', 'Cook dinner']
print(f'\nThe stack is empty {my_list}')
stack = []
for task in my_list:
  stack.append(task)
while stack:
  print(stack.pop(), ' - Done!')
print('\nThe stack is empty')

#NLP with spacy
print('===============NLP with spacy==============')
import spacy
txt = 'List is a ubiquitous data structure in the Python programming language.'
nlp = spacy.load('en_core_web_sm')
doc = nlp(txt)
stk= []
for w in doc:
  if w.pos_ == 'NOUN' or w.pos_ == 'PROPN':
    stk.append(w.text)
  elif (w.head.pos_ == 'NOUN' or w.head.pos_ == 'PROPN') and (w in w.head.lefts):
    stk.append(w.text)
  elif stk:
    chunk = ''
    while stk:
      chunk = stk.pop() + ' ' + chunk
    print(chunk.strip())

import spacy
txt = 'List is a ubiquitous data structure in the Python programming language.'
nlp = spacy.load('en_core_web_sm')
doc = nlp(txt)
for t in doc:
  print(t.text, t.head.text)
#Combining 2 lists into a tuple list
task_list = ['Pay bills', 'Tidy up', 'Walk the dog', 'Go to the pharmacy', 'Cook dinner']
tm_list = ['8:00', '8:30', '9:30', '10:00', '10:30']
#Python's zip() function creates an iterator that will aggregate elements from two or more iterables.
# #You can use the resulting iterator to quickly and consistently solve common programming problems, like creating dictionaries.
tuple_list = [(tm, task) for tm, task in zip(tm_list, task_list)]
dict_list = [{tm, task} for tm, task in zip(tm_list, task_list)]
print(tuple_list)
print(dict_list)

print (tuple_list[0][0])

#Parse a sentence and count the number os words in it.
txt = 'Python is one of the most promising programming languages today. Due to the simplicity of Python syntax, many researchers and scientists prefer Python over many other languages.'
#replace comma and period
 
#txt = 'the the sam is is the best the'
word_count = {}
split_list = txt.replace('.',' ').replace(',',' ').split(' ')
 
print(split_list)
word_count = {}
for w in split_list:
  word = word_count.get(w)
  if (w in word_count):
    word_count[w] = word+1
  else:
    word_count[w] = 1

print(word_count)


#Another cool way to do this would be
for w in split_list:
  c = word_count.setdefault(w,0)
  word_count[w] += 1

print(word_count)

#Set - Does not allow dups
lst = ['John Silver', 'Maya Smith', 'Maya Smith', 'Tim Jemison', 'John Silver', 'Maya Smith']
lst = list(set(lst))
print(lst)

lst1 = ['John Silver', 'Maya Smith', 'Maya Smith', 'Tim Jemison', 'John Silver', 'Maya Smith']
#Set to keep the order
lst1 = list(sorted(set(lst1), key=lst1.index))
print(lst1)

photo1_tags = {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
photo2_tags = {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
intersection = photo1_tags.intersection(photo2_tags)
if len(intersection) >= 2:
  print("The photos contain similar objects.")

#Find all the common photos in the list

l = [
 {
  "name": "photo1.jpg",
  "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
 },
 {
  "name": "photo2.jpg",
  "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
 },
 {
  "name": "photo3.jpg",
  "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building',
           'travel'}
 },
 {
  "name": "photo4.jpg",
  "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
 }
]
for j in range(2, 5):
    print(j)
photo_groups = {}
for i in range(1, len(l)):
  for j in range(i+1,len(l)+1):
    print(f"Intersecting photo {i} with photo {j}")

    # Implement intersection here, saving results to photo_groups
    key1 = 'photo'+str(i)+'.jpg'
    key2 = 'photo'+str(j)+'.jpg'
    photo1_tags = l[i-1]['tags']
    photo2_tags = l[j-1]['tags']
    intersection = photo1_tags.intersection(photo2_tags)
    if len(intersection) >= 2:
        print("The photos contain similar objects.")
        lst = []
        lst.append(key1)
        lst.append(key2)
        keyofmap =tuple(intersection)

        photo_groups.setdefault(keyofmap, lst)
    else:
        print("The photos DOES NOT contain similar objects.")


print(photo_groups)