import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

# enumerate gives you the index and the object itself of that index (helps you know where each item is located)
for index, column_header in enumerate(header_row):
    print(index, column_header)

# -----------------------------------------------------

highs = []
dates = []
lows = []

for row in csv_file:
    # try and except allows us to specify which errors we want to skip and continue on
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        # f string method allows us to incorporate variables directly into a string
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(the_date)

# ----------------------------------------------------

fig = plt.figure()

plt.title("Daily High and Low Temperatures, 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

# giving the data for the plot
plt.plot(dates, highs, c = "red", alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)

# fill_between gives us one x value and two y values to fill between
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

fig.autofmt_xdate()

plt.show()


# subplots allow us to see multiple plots in the same figure
# 3 arguments: subplot(row, col, index) - starts at 1 for index (which plot are we working with)
plt.subplot(2,1,1) 
plt.plot(dates, highs, c = 'red')
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates, lows, c = 'blue')
plt.title("Lows")

#super title is the title of the whole image/page
plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()
