import csv
from datetime import datetime

import matplotlib.pyplot as plt  

filename = '/home/riya/Documents/Python/Python_projects/DataViz/csv_data_plot/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    

    # Get precepation and dates from the file.
    dates, preps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prep = float(row[3])
        dates.append(current_date)
        preps.append(prep)

    # Plot the rainfall.
    # plt.style.use('')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, preps, c='green')

    # Format the plot.
    plt.title('Daily Rainfall - 2018, Sitka')
    plt.xlabel('', fontsize=10)
    fig.autofmt_xdate()
    plt.ylabel('Rainfall', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()