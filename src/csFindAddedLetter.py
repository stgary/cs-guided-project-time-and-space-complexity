def csFindAddedLetter(str_1: str, str_2: str) -> str:
  # Given two strings, str_1 and str_2, where str_2 is generated
  # by randomly shuffling str_1 and then adding one letter
  # at a random position
  
  # write a function that returns the letter that was added to str_2
  result = ''

  for i in range(len(str_2)): 
    letter1 = str_1[i : i + 1]
    letter2 = str_2[i : i + 1]

    if letter1 != letter2:
      result += letter2
      break

  return result
    
print(csFindAddedLetter(str_1 = "bcde", str_2 = "bcdef"))
print(csFindAddedLetter(str_1 = "", str_2 = "z"))
print(csFindAddedLetter(str_1 = "b", str_2 = "bb"))
print(csFindAddedLetter(str_1 = "xqmxtheyvpdqounqmfyaqdqxwe", str_2 = "xqmxtheyvpdqounqmfyaqxdqxwe"))