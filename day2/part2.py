computing = True
output = 19690720
noun = -1
verb = 0

while computing:
  f = open("day2_data.txt","r")
  data = f.read()
  f.close()
  intcode = data.split(',')
  intcode = [int(x) for x in intcode]
  address = 0

  if noun != 100:
    noun += 1
  if noun == 100:
    noun = 0
    verb += 1

  intcode[1] = noun
  intcode[2] = verb

  while intcode[address] != 99:
    if intcode[address] == 1:
      intcode[intcode[address+3]] = intcode[intcode[address+1]] + intcode[intcode[address+2]]
    elif intcode[address] == 2:
      intcode[intcode[address+3]] = intcode[intcode[address+1]] * intcode[intcode[address+2]]
    address += 4

  if intcode[0] == output:
    computing = False
    print (100 * noun + verb)
