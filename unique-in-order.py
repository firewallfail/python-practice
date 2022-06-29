def unique_in_order(iterable):
  if len(iterable) == 0:
    return []
  cleaned = [iterable[0]]
  for letter in iterable[1:]:
    if letter != cleaned[-1]:
      cleaned.append(letter)
  return cleaned

print(unique_in_order('AAAABBBCCDAABBB'))