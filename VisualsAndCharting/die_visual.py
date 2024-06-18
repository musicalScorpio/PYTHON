from plotly.graph_objs import Bar, Layout
from plotly import offline
from Die import Die

#Now write a program that we can use to roll any number of die
number_of_die =int (input('How many numner of Die you want to roll ? '))

# Analyze the results.
frequencies = []
results = []
num_sides = number_of_die * 10
frequency_map = {}

for roll_num in range(100):
   count_after_roll = 0
   for var in range(number_of_die):
      die = Die(num_sides)
      count_after_roll += die.roll()
   results.append(count_after_roll)

for value in range(number_of_die, num_sides+1):
   frequency = results.count(value)
   frequencies.append(frequency)
   frequency_map [value] = frequency
size = len(frequencies)
#print (f' The frequency map dump is {frequency_map}')
# Visualize the results.
x_values = list(range(number_of_die, num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')














