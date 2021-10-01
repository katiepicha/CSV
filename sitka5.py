import csv
import matplotlib.pyplot as plt
from datetime import datetime

# -------------------------------------------------------------------

open_dv_file = open("death_valley_2018_simple.csv", "r")

csv_dv_file = csv.reader(open_dv_file, delimiter=",")

header_dv_row = next(csv_dv_file)

for index, column_header in enumerate(header_dv_row):
    print(index, column_header)
    if column_header == 'TMAX':
        max_index = index
    elif column_header == 'TMIN':
        min_index = index
    elif column_header == 'DATE':
        date_index = index
    elif column_header == 'NAME':
        name_index = index

dv_highs = []
dv_dates = []
dv_lows = []

for row in csv_dv_file:
    # try and except allows us to specify which errors we want to skip and continue on
    try:
        the_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        high = int(row[max_index])
        low = int(row[min_index])
        dv_name = row[name_index]
    except ValueError:
        # f string method allows us to incorporate variables directly into a string
        print(f"Missing data for {the_date}")
    else:
        dv_highs.append(int(row[max_index]))
        dv_lows.append(int(row[min_index]))
        dv_dates.append(the_date)


# -------------------------------------------------------------------

open_s_file = open("sitka_weather_2018_simple.csv", "r")

csv_s_file = csv.reader(open_s_file, delimiter=",")

header_s_row = next(csv_s_file)

for index, column_header in enumerate(header_s_row):
    print(index, column_header)
    if column_header == 'TMAX':
        max_index = index
    elif column_header == 'TMIN':
        min_index = index
    elif column_header == 'DATE':
        date_index = index
    elif column_header == 'NAME':
        name_index = index

s_highs = []
s_dates = []
s_lows = []

for row in csv_s_file:
    # try and except allows us to specify which errors we want to skip and continue on
    try:
        the_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        high = int(row[max_index])
        low = int(row[min_index])
        s_name = row[name_index]
    except ValueError:
        # f string method allows us to incorporate variables directly into a string
        print(f"Missing data for {the_date}")
    else:
        s_highs.append(int(row[max_index]))
        s_lows.append(int(row[min_index]))
        s_dates.append(the_date)

# -----------------------------------------------------------------

fig = plt.figure()

plt.subplot(2,1,1) 
plt.plot(s_dates, s_highs, c = 'red')
plt.plot(s_dates, s_lows, c = 'blue')
plt.fill_between(s_dates, s_highs, s_lows, facecolor = 'blue', alpha = 0.1)
plt.title(s_name)

plt.subplot(2,1,2)
plt.plot(dv_dates, dv_highs, c = 'red')
plt.plot(dv_dates, dv_lows, c = 'blue')
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor = 'blue', alpha = 0.1)
plt.title(dv_name)

#super title is the title of the whole image/page
plt.suptitle(f"Temperature comparison between {s_name} and {dv_name}")

plt.tick_params(axis="both", which="major", labelsize=12)
fig.autofmt_xdate()

plt.show()
