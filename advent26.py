bus = '13,x,x,41,x,x,x,x,x,x,x,x,x,467,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,353,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23'
bus_list1 = list(bus.split(','))
bus_list2 = []

for i in bus_list1:
    if i =='x':
        bus_list2.append(i)
    else:
        bus_list2.append(int(i))


step = bus_list2[0]
total = bus_list2[0]
for i in range(1,len(bus_list2)):
    if bus_list2[i] != 'x':
        while True:
            if ((total + i) % bus_list2[i]) == 0:
                print(total)
                step *= bus_list2[i]
                break
            else:
                total += step
