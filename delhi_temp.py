import csv
from datetime import datetime

import matplotlib.pyplot as plt 

filename = '/home/riya/Documents/Python/Python_projects/DataViz/Git_Project/Data/DailyDelhiClimateTrain.csv'

#Open the file and parse it using csv module
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    
    #Check for header_row
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    #Get mean temperatures and dates from this file.
    mean_temps, dates = [], []
    for row in reader:
        mean_temp_C = round(float(row[1]), 2)
        mean_temp_F = (9/5)* mean_temp_C + 32
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)
        mean_temps.append(mean_temp_F)

    #Plot the mean temperatures .
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15,6))
    ax.scatter(dates, mean_temps, c=mean_temps, cmap=plt.cm.YlOrRd, s=5)

    #Format plot.
    plt.title('Daily mean temperatures, 2013 - 2017, Delhi(India)', fontsize=14)
    plt.xlabel('', fontsize=8)
    fig.autofmt_xdate()
    plt.ylabel('Tempertures(F)', fontsize=8)
    plt.tick_params(axis='both', which='major', labelsize=8)

    plt.show()