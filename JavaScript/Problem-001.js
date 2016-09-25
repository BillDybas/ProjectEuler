//
// Solution to Problem 1: Multiples of 3 and 5
// by Bill Dybas
//

const isMultipleOf = function(x) {
  return function(y) {
    return y % x === 0;
  }
}

const answer =
  Array(1000)
    .fill() // Fill an Array w/ 0's
    .map((x, i) => i) // Make the index the value at that index
    .filter(val => isMultipleOf(3)(val) || isMultipleOf(5)(val)) // Filter values that are multiples of 3 or 5
    .reduce((previous, current) => previous + current); // Sum them up

console.log(answer);
