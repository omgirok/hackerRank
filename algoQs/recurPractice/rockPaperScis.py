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
import copy
def generateMoves(n):
  if n < 1:
    return []

  if (n == 1):
    return [["rock"], ["paper"], ["scissors"]]

  # array
  # moves = ("rock","paper","scissors")
  n_0 = generateMoves(n-1)
  # n_0 = [["rock"], ["paper"], ["scissors"]]

  n_1 = copy.deepcopy(n_0)
  # n_1 = [["rock"], ["paper"], ["scissors"]]
  
  n_2 = copy.deepcopy(n_0)
  # n_2 = [["rock"], ["paper"], ["scissors"]]

  for m in n_0:
    m.insert(0, "rock")
    # after this loop,
    # n_0 = [["rock","rock"], ["rock","paper"], ["rock","scissors"]]
  for m in n_1:
    m.insert(0, "paper")
    # after this loop,
    # n_1 = [["paper","rock"], ["paper","paper"], ["paper","scissors"]]
  for m in n_2:
    m.insert(0, "scissors")

  return n_0 + n_1 + n_2

print generateMoves(3)
# print generateMoves(5)