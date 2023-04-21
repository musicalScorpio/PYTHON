from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die:
    def __init__(self, num_of_sides=6):
        self.num_sides = num_of_sides
    def roll(self):
        return randint(1, self.num_sides)

die = Die()
results = []

for n in range(100):
    number = die.roll()
    results.append(number)

#Now calculate the number of times each side was thrown
'''
frequencies = {}
for num_of_sides in range (1, die.num_of_sides + 1):
    frequencies [num_of_sides] = (list.count(num_of_sides))
print(frequencies)

values =[]
values = frequencies.values()

print(values)
'''

'''
# Visualize the results.
x_values = [1,2,3,4,5,6]
data = [Bar(x=x_values, y=frequencies.values())]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
'''