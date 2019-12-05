def main():
  f= open("day1_data.txt","r")
  fl = f.readlines()
  total = 0
  for x in fl:
    calculation = (int(x)/3)-2
    total += calculation
  print total

if __name__== "__main__":
  main()
