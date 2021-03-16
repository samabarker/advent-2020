def find_neighbours(initial):
  neighbours = []
  for l in range(-1,2,1):
    new_i = initial[0] + l
    for l in range(-1,2,1):
      new_j = initial[1] + l
      for l in range(-1,2,1):
        new_k = initial[2] + l
        if (new_i, new_j, new_k) != initial:
          neighbours.append((new_i, new_j, new_k))
  return neighbours


puzzle_input = '''.#.
..#
###'''

puzzle_input = '''####.#..
.......#
#..#####
.....##.
##...###
#..#.#.#
.##...#.
#...##..'''

puzzle_input_list = list(puzzle_input.split('\n'))
current_situation = dict()

for i in range(-20,20):
  for j in range(-20,20):
    for k in range(-20,20):
      current_situation[i,j,k] = '.'

for i in range(len(puzzle_input_list) - 1,-1,-1):
  for j in range(0, len(puzzle_input_list[i])):
    current_situation[(len(puzzle_input_list) - 1 - i,j,0)] = puzzle_input_list[i][j]

for i in range(0,6):
  update = []
  for key in current_situation:
    current_location = key
    current_status = current_situation[key]
    neighbours = find_neighbours(key)
    counter = 0
    for i in neighbours:
      try:
        if current_situation[i] == "#":
          counter += 1
      except:
        continue
    if counter == 3 and current_status == '.':
      update.append([current_location, '#'])
    elif counter != 2 and counter != 3 and current_status == '#':
      update.append([current_location, '.'])

  for i in update:
    current_situation[i[0]] = i[1]


counter = 0
for key in current_situation:
  if current_situation[key] == '#':
    counter +=1

print(counter)