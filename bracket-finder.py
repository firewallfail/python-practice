bracketPairs = {
  "(": ")",
  "{": "}",
  "[": "]",
  "<": ">",
}

closingBrackets = {
  "}": 0,
  "]": 0,
  ")": 0,
  ">": 0,
}

def matchingBrackets(str):
  foundBrackets = []
  for i in str:
    try:
      bracketPairs[i]
      foundBrackets.append(i)
    except:
      try:
        closingBrackets[i]
        if len(foundBrackets) == 0 or i != bracketPairs[foundBrackets.pop()]:
          return False
      except:
        continue
  if len(foundBrackets) > 0:
    return False
  return True

print(matchingBrackets("string()()("))
print(matchingBrackets('string[][<>{{}}]()(){}'))
