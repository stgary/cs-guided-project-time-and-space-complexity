from typing import List

def csSortedTwoSum(numbers: List[int], target: int) -> List[int]:
  # Given a sorted array (in ascending order) of integers and
  # a target, write a function that finds the two integers that
  # add up to the target
  
  # iterate through the numbers list using a for loop (i)
  for i in range(len(numbers)):
  
    # use another for loop to check each number against eachother(j)
    for j in range(i+1, len(numbers)):
      
      # an if statement adding the current value of i 
      # to the value of j
      if numbers[i] + numbers[j] == target:
        
        # return i and j if they add up to the target
        return [i, j]
    
    return "No solution found"
  
print(csSortedTwoSum([3, 8, 12, 19, 16], 11))