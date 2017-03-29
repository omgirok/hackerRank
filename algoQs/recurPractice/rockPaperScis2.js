/* jshint esversion: 6*/
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
*
*/

// it's trinary
var rockPaperScissors = function(num) {
  let rounds = num || 3;
  var results = [];
  var current = Array(rounds).fill(0);

  while (current[rounds - 1] !== 3) {
    results.push(current.map(item => {
      if (item === 0)
        return 'rock';
      else if (item === 1)
        return 'paper';
      else if (item === 2)
        return 'scissors';
    }));  
    
    ++current[0];
    let j = 0;
    while (current[j] === 3 && j < rounds) {
      if (j === rounds - 1)
        break; 
      else {
        current[j] = 0;
        ++current[j + 1];
      }
      ++j;
    }
  }

  return results;
};