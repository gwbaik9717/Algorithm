// Time Complexity: O(n)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map(Number);
const arr = inputs[1].split(" ").map(Number);

let i = 0;
let j = m - 1;
let sum = arr.slice(0, j + 1).reduce((a, c) => a + c, 0);
let answer = sum;

while (j < n - 1) {
  sum -= arr[i++];
  sum += arr[++j];

  answer = Math.max(answer, sum);
}

console.log(answer);
