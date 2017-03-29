"""
  Write a program that will read a list of numbers and a 
  desired sum, then determine the subset of numbers in 
  the list that yield that sum if such a subset exists.
"""

def sumSubset(arr, total):
  # set flag for if a set has been found
  winner = False
  numbers = []

  # start looping through passed in array to check
  # print "+ starting to loop through the array:", arr
  for index in range(len(arr)):  
    # print "+-- looking for values that match the sum:",total
    # print "+-- now checking value:",arr[index]
    if arr[index] == total:
      winner = True

    # this if statement only executes when value at index less than total
    # will try to find a subset within current array that adds up to total
    if arr[index] < total:
      # print "+-- ",arr[index],"is less than", total
      temp = arr.pop(index)
      new_total = total - temp
      value = sumSubset(arr, new_total)

      winner = value[0]
      numbers = value[1]
      arr.insert(index, temp)

    if winner:
      numbers.append(arr[index])
      break

  return [winner, numbers]

print sumSubset([2,3,4,51], 7)
"""
arr[0] == 2 runs on
([2,3,4,51],7)
which recursively calls 
--> ([3,4,51], 5)
--> this will fail all the way down.
--> break out to most outer loop
index+=1,

arr[1] == 3 runs on 
([2,3,4,51],7)
which recursively calls
([2,4,51],4)

"""
