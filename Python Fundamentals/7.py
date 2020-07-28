for j in range(10,99,1):
  for i in range (2,x//2,1):
    if(j%i == 0):
      break
  else:
    print(j)
