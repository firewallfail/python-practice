def series_sum(n):
  final = 0
  denom = 1
  for x in range(n):
    final += 1/denom
    denom += 3
  return '{:.2f}'.format(final)

print(series_sum(3))

print(1/7)