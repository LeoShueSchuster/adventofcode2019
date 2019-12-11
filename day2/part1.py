f = open("day2_data.txt","r")
data = f.read()
intcode = data.split(',')
intcode = [int(x) for x in intcode]

position = 0
intcode[1] = 12
intcode[2] = 2

while intcode[position] != 99:
  if intcode[position] == 1:
    intcode[intcode[position+3]] = intcode[intcode[position+1]] + intcode[intcode[position+2]]
  elif intcode[position] == 2:
    intcode[intcode[position+3]] = intcode[intcode[position+1]] * intcode[intcode[position+2]]
  position += 4

print (intcode[0])
f.close()

''' Before I refactored, I had the following in each if statement:
    index1 = intcode[position+1]
    index2 = intcode[position+2]
    index3 = intcode[position+3]
    total = intcode[index1] + intcode[index2] # or *
    intcode[index3] = total
'''