// Time Complexity: O(n)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const arr = inputs[1].split(" ").map(Number);

let answer = 0;

let i = 0;
let j = n - 1;

while (i < j) {
  answer = Math.max(answer, (j - i - 1) * Math.min(arr[i], arr[j]));

  if (arr[i] < arr[j]) {
    i++;
  } else {
    j--;
  }
}

console.log(answer);
