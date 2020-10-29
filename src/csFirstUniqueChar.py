def csFirstUniqueChar(input_str: str) -> int:
  # Given a string, write a function that return the index
  # of the first unique (non-repeating) character. if there
  # isn't a unique (non-repeating) character, return -1.
  
  # iterate through the string 
  for i in input_str:
    count = input_str.count(i)
    if count == 1:
      return input_str.index(i)
  return -1
print(csFirstUniqueChar(input_str = "lambdaschool"))
print(csFirstUniqueChar(input_str = "ilovelambdaschool"))
print(csFirstUniqueChar(input_str = "vvv"))
