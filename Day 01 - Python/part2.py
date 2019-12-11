f = open("day1_data.txt","r")
total = 0
for x in f:
  calculation = int(x)
  while calculation > 6:
    calculation = (calculation//3)-2
    total += calculation
print (total)