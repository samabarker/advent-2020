import math

landing_time = 1008713
bus_times_str = '13,x,x,41,x,x,x,x,x,x,x,x,x,467,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,353,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23'
bus_times_lst = list(bus_times_str.split(','))
bus_times_corrected = []
nearest_times = []

for i in bus_times_lst:
    if i != 'x':
        bus_times_corrected.append(int(i))

for i in bus_times_corrected:
    previous_time = math.floor(landing_time / i) * i
    if previous_time != landing_time:
        nearest_times.append(previous_time + i)
    else:
        nearest_times.append(previous_time)

earliest_departure = min(nearest_times)
difference = earliest_departure - landing_time
result = difference * bus_times_corrected[nearest_times.index(earliest_departure)]

print(result)