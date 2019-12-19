f = open("day3_data.txt","r")
#f = open("test1.txt","r")
#f = open("test2.txt","r")
#f = open("test3.txt","r")
wire1 = f.readline().strip().split(',')
wire2 = f.readline().strip().split(',')
f.close()

central_port = [0, 0]
coordinates = central_port
wiring = []
first_wire = []  # must be empty or else the Manhattan distance will include the central port
second_wire = [] # same as above

for m in range(len(wire1)):
    direction = wire1[m][0]
    length = int(wire1[m][1:])
    wiring = list(coordinates)
    if direction == 'U':
        coordinates[0] += length
        for p in range(wiring[0]+1, coordinates[0]+1):
            first_wire.append("{},{}".format(p, coordinates[1]))
    elif direction == 'D':
        coordinates[0] -= length
        for p in range(coordinates[0], wiring[0]-1):
            first_wire.append("{},{}".format(p, coordinates[1]))
    elif direction == 'R':
        coordinates[1] += length
        for p in range(wiring[1]+1, coordinates[1]+1):
            first_wire.append("{},{}".format(coordinates[0], p))
    elif direction == 'L':
        coordinates[1] -= length
        for p in range(coordinates[1], wiring[1]-1):
            first_wire.append("{},{}".format(coordinates[0], p))
    else:
      print("Invalid direction detected")

coordinates = [0, 0] # need to reset for second wire

for m in range(len(wire2)):
    direction = wire2[m][0]
    length = int(wire2[m][1:])
    wiring = list(coordinates)
    if direction == 'U':
        coordinates[0] += length
        for p in range(wiring[0]+1, coordinates[0]+1):
            second_wire.append("{},{}".format(p, coordinates[1]))
    elif direction == 'D':
        coordinates[0] -= length
        for p in range(coordinates[0], wiring[0]-1):
            second_wire.append("{},{}".format(p, coordinates[1]))
    elif direction == 'R':
        coordinates[1] += length
        for p in range(wiring[1]+1, coordinates[1]+1):
            second_wire.append("{},{}".format(coordinates[0], p))
    elif direction == 'L':
        coordinates[1] -= length
        for p in range(coordinates[1], wiring[1]-1):
            second_wire.append("{},{}".format(coordinates[0], p))
    else:
      print("Invalid direction detected")

contactPoints = set(first_wire).intersection(set(second_wire))
manhattan_distance = []
for i in contactPoints:
  i1, i2 = i.split(',')
  x = int(i1)
  y = int(i2)
  manhattan_distance.append(abs(x) + abs(y))

print(min(manhattan_distance))
