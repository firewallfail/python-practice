def square_digits(num):
  returnValue = ""
  for i in str(num):
    returnValue += str(int(i) * int(i))
  return int(returnValue)

print(square_digits(9119))
print(square_digits(0))