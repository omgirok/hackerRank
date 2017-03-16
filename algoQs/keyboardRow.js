/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(words) {
  // need to check that each letter exists within same row for each word 
  toRemove = [];
  for (var x of words) {
    console.log("current word:", x);
    y = x.toLowerCase();
    // check all letters are in the same row
    rowToCheck = getRow(y[0]);
    for (var letter of y) {
      if (getRow(letter) != rowToCheck) {
        toRemove.push(x);
        //console.log("removing word from answer set:", words.splice(words.indexOf(x), 1));
        break;
      }
    }
  }
  for (var r of toRemove) {
      words.splice(words.indexOf(r), 1);
  }
  console.log(words);
  return words;
}
var getRow = function(char) { 
  row1 = 'qwertyuiop';
  row2 = 'asdfghjkl';
  row3 = 'zxcvbnm';
  var curr = char.toLowerCase();
  if (row1.includes(curr)) { 
    return '1';
  }
  if (row2.includes(curr)) {
    return '2';
  }
  if (row3.includes(curr)) {
    return '3';
  }
  return 'fail';
}
