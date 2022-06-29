# return masked string
def maskify(cc):
  x = (len(cc))
  if x < 4: return cc
  return '#' * (x - 4) + cc[x - 4:x]

print(maskify("4556364607935616"))
print(maskify("64607935616"))
print(maskify("1"))
print(maskify(""))