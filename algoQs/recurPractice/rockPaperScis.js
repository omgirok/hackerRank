/*
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
*/

function generateMoves(n) {
  if (n < 1) {
    return [];
  }
  if (n === 1) {
    return [["rock"],["paper"],["scissors"]];
  }

  var n_0 = generateMoves(n-1);
  var n_1 = generateMoves(n-1);
  var n_2 = generateMoves(n-1);

  for (var x in n_0) {
    n_0[x].push("rock");
  }  
  for (var y in n_1) {
    n_1[y].push("paper");
  }
  for (var z in n_2) {
    n_2[z].push("scissors");
  }

  result = n_0.concat(n_1).concat(n_2);
  return result;
}

console.log(generateMoves(2))
