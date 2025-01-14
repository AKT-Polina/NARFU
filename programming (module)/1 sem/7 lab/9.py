passengers = [('Иванов Сергей', 1, 5),
              ('Сергеев Петр', 3, 5),
              ('Петров Кирилл', 1, 2)]
station_count = 5
 
at_every_station = [0 for _ in range(station_count)]
for name, start_station, end_station in passengers:
    for station in range(start_station - 1, end_station - 1):
        at_every_station[station] += 1
 
max_passengers = max(at_every_station)
 
for station, count in enumerate(at_every_station, start=1):
    if count == max_passengers:
        print(f'{station} - {station + 1}')
