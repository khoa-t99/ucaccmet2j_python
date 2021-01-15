import json

#Opening the json file
with open('precipitation.json') as file:
    precipitation = json.load(file)

#Assigning the station and name list to variables
STATIONS = ['GHCND:USW00093814', 'GHCND:US1WAKG0038', 'GHCND:USC00513317', 'GHCND:US1CASD0032']

NAME = ['Cincinatti','Seattle','Maui','San Diego']

#Part 1 & 3
# for each station code
for station_code,name in zip(STATIONS,NAME):
    measurement_sum_year = 0
    sum_month_measure = [0]*12
    #splitting the date column for each measurement
    for measurement in precipitation:
        station = measurement['station']
        measure_date = measurement['date'].split('-')
        # Doing an if loop that matches the station with station_code
        if station == station_code:
            month = int(measure_date[1])-1
            #summing up the precipitation value for each month
            sum_month_measure[month] += measurement['value']
            #summing up the precipitation value for the whole year
            measurement_sum_year += measurement['value']

    #Part 2 - Calculating the relative percentage of each month throughout the whole year
    month_percent = []
    for month in sum_month_measure:
        percent = (month / measurement_sum_year) * 100
        month_percent.append(percent)


#Printing out the results
    print(f'The value of station in {name}')

    print(f'The value of precipitation for each months are: {sum_month_measure} ')

    print(f'The value of precipitation for the whole year is: {measurement_sum_year}')

    print(f'The percentage of precipation for each month is: {month_percent}\n')



