'''
@author Sam Mukherjee
'''
'''
#Plots
#At heart, a Matplotlib visualization is built from two main types of objects: a Figure object and one or more Axes objects
from matplotlib import pyplot as plt

days = ['2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08']
prices = [729.77, 735.11, 755.98, 816.04, 880.02]

plt.plot(days, prices)
plt.title('NASDAQ: TSLA')
plt.xlabel('Date')
plt.ylabel('USD')
#plt.show()

import matplotlib.pyplot as plt
regions = ['New England', 'Mid-Atlantic', 'Midwest']
sales = [882703, 532648, 714406]

plt.bar(regions, sales)
plt.xlabel("Regions")
plt.ylabel("Sales")
plt.title("Annual Sales Aggregated on a Regional Basis")
#plt.show()
'''

# importing modules
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
'''
# data to plot
salaries = [1215, 1221, 1263, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324,
            1326, 1337, 1346, 1354, 1355, 1364, 1367, 1372, 1375, 1376, 1378,
            1378, 1410, 1415, 1415, 1418, 1420, 1422, 1426, 1430, 1434, 1437,
            1451, 1454, 1467, 1470, 1473, 1477, 1479, 1480, 1514, 1516, 1522,
            1529, 1544, 1547, 1554, 1562, 1584, 1595, 1616, 1626, 1717]

# preparing a histogram
fig, ax = plt.subplots()
fig.set_size_inches(5.6, 4.2)
ax.hist(salaries, bins=np.arange(1100, 1900 , 50), edgecolor='red',linewidth=1.2)
formatter = ticker.FormatStrFormatter('$%1. 0f')
ax.xaxis.set_major_formatter(formatter)
plt.title('Monthly Salaries in the Sales Department')
plt.xlabel('Salary (bin size = $50)')
plt.ylabel('Frequency')
# showing the histogram plt.show()


#pie chart
import numpy as np
count, labels = np.histogram(salaries, bins=np.arange(1100, 1900, 50))
labels = ['$'+str(labels[i])+'-'+str(labels[i+1]) for i, j in enumerate(labels[1:])]
print(count)
print(labels)
non_zero_pos = [i for i, x in enumerate(count) if x != 0]
#Fitler zeros out
labels = [e for i, e in enumerate(labels) if i in non_zero_pos]
count = [e for i, e in enumerate(count) if i in non_zero_pos]

from matplotlib import pyplot as plt
plt.pie(count, labels=labels, autopct='%1.1f%%')
plt.title('Monthly Salaries in the Sales Department')
#plt.show()

#Thats how you return multiple values from a mehtod
class Test:
    def justTying(self):
        return [1,2,3]
test  = Test()
a,b ,c = test.justTying()



'''
# preparing the DataFrame
#Plotting with pandas
import pandas as pd
import matplotlib.pyplot as plt

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
state_fl =us_cities[us_cities.City.eq('Orlando')]
print(state_fl)
top_us_cities = us_cities[us_cities.Population.ge(1000000)]
print(top_us_cities)
top_cities_count = top_us_cities.groupby(['State'], as_index = False).count().rename(columns={'City': 'cities_count'}) [['State','cities_count']]

# drawing the chart
top_cities_count.plot.bar('State', 'cities_count', rot=0)
plt.xlabel("States")
plt.ylabel("Top cities count")
plt.title("Number of Megacities per US State")
plt.yticks(range(min(top_cities_count['cities_count']),
                 max(top_cities_count['cities_count'])+1))
plt.show()