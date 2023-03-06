def fact(number):
  s = 1
  for x in range(1,number+1):
    s = s*x
  return s
print("Factorial is : ",fact(5))
