// Time Complexity: O(n)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const arr = inputs[1].split(" ").map(Number);
let answer = arr[0];

for (let i = 1; i < n; i++) {
  arr[i] = Math.max(arr[i], arr[i] + arr[i - 1]);
  answer = Math.max(answer, arr[i]);
}

console.log(answer);
