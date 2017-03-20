"""
* Write a function that generates every sequence of throws a single
* player could throw over a three-round game of rock-paper-scissors.
*
* Your output should look something like:
*   [["rock", "rock", "rock"],
*    ["rock", "rock", "paper"],
*    ["rock", "rock", "scissors"],
*    ["rock", "paper", "rock"],
             ...etc...
     ]
*
* Extra credit:
*   - Make your function return answers for any number of rounds.
* Example:
* rockPaperScissors(5); // => [['rock', 'rock', 'rock', 'rock', 'rock'], etc...]
"""

from random import randint
def generateMoves(n):
  if n == 0:
    return
  moves = ("rock","paper","scissors")

  # for n = 1; we can only pick one
  allPoss = []
  x = 0
  while x < 3**n:
    # print "back to top"
    combinations = []
    # build a set of combinations
    while len(combinations) < n:
      move = moves[randint(0,2)]
      # print "inserting", move
      combinations.append(move)
      
      # y+=1
    if combinations in allPoss:
      # print "already exists"
      continue
    else:
      # print "didn't exist, adding " + str(combinations) + " to allPoss"
      allPoss.append(combinations)
      x+=1
  return allPoss

print generateMoves(1)
print generateMoves(3)



# Given n as length of string, generate all possible binary numbers of length n
def generateBinary(n):
  return