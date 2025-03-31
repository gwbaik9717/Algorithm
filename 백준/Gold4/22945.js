// Time Complexity: O(n)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = inputs[0].split(" ").map(Number);
const arr = inputs[1].split(" ").map(Number);

let answer = Number.MAX_SAFE_INTEGER;
let sum = arr[0];

let i = 0;
let j = 0;

while (i <= j && j < n) {
  if (sum >= k) {
    answer = Math.min(answer, j - i + 1);
    sum -= arr[i];
    i++;
  } else {
    j++;
    sum += arr[j];
  }
}

if (answer === Number.MAX_SAFE_INTEGER) {
  console.log(0);
  return;
}

console.log(answer);
