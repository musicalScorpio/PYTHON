import csv
import matplotlib.pyplot as plt
from datetime import datetime

class TempPrinter:
    def __init__(self, filename='weather_data/sitka_weather_2021_simple.csv'):
        self.filename = filename


    def draw_max_temp_plots (self, maxTemp_pos = 4,minTemp_pos =5 ,date_pos =2):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header = next(reader)
            print(f'{header}')
            for index, value in enumerate(header):
                print(f'{index} - {value}')
            highs =[]
            dates = []
            lows = []
            for row in reader:
                try:
                    maxTemp = int(row[maxTemp_pos])
                    minTemp = int (row[minTemp_pos])
                    highs.append(maxTemp)
                    lows.append(minTemp)
                    first_date = datetime.strptime(row[date_pos], '%Y-%m-%d')
                    dates.append(first_date)
                except Exception:
                    print(f'Exception happened for {row}')
                #print(f'{highs}')

            #Plot the points
            plt.style.use('seaborn')
            fig, ax = plt.subplots()
            max_temp = int(max(highs))
            ax.set_ylim([0 ,120 ])
            ax.plot(dates, highs, c='red')
            ax.plot(dates, lows, c='blue')
            ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)
            ax.set_title("Daily high temperatures : 2021", fontsize=24)
            #ax.set_xlabel('Day of 2021', fontsize=16)
            #ax.get_xaxis().set_visible(False)
            ax.set_ylabel("Temperature (F)", fontsize=16)
            #ax.tick_params(axis='both', which='major', labelsize=16)
            plt.show()

temp = TempPrinter()
temp.draw_max_temp_plots()
temp = TempPrinter('weather_data/death_valley_2021_simple.csv')
temp.draw_max_temp_plots(3,4)