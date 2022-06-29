def find_it(seq):
  totals = {}
  for x in seq:
    try:
      totals[x] += 1
    except:
      totals[x] = 1
  for key in totals:
    if totals[key] % 2 == 1:
      return int(key)
  return None

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))