//
// Solution to Problem 5: Smallest Multiple
// by Bill Dybas
//

// See: https://en.wikipedia.org/wiki/Greatest_common_divisor#Using_Euclid.27s_algorithm
const gcd = function(a, b) {
  return !b ? a : gcd(b, a % b);
}

// See: https://en.wikipedia.org/wiki/Least_common_multiple#Reduction_by_the_greatest_common_divisor
const lcm = function(a, b) {
  return Math.abs(a) / gcd(a, b) * Math.abs(b);
}

const answer =
  Array(20)
    .fill() // Fill an Array w/ 0's
    .map((x, i) => i + 1) // Make the index + 1 the value at that index
    .reduce((previous, current) => lcm(previous, current)); // Find the LCM of all the numbers

console.log(answer);
