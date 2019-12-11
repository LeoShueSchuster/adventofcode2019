f = open("day1_data.txt","r")
total = 0
for x in f:
  total += (int(x)//3)-2
print (total)
f.close()