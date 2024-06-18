import matplotlib.pyplot as plt

input_values = range (1, 1001)
squares = [x**2 for x in input_values]

fig, ax = plt.subplots()
#ax.plot(input_values, squares, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
#ax.scatter(input_values, squares, c=(0, 0.8, 0), s=1)
ax.scatter(input_values, squares, cmap=plt.cm.Blues, s=1)
ax.axis([0, 1100, 0, 1100000])

#'seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight'
#plt.style.use('seaborn-darkgrid')
plt.show()
#Save it auto
#plt.savefig('squares_plot.png', bbox_inches='tight')