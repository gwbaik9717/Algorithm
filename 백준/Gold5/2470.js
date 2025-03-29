// Time Complexity: O(nlogn)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const arr = inputs[1].split(" ").map(Number);

arr.sort((a, b) => a - b);

let answer = [arr[0], arr[n - 1]];

let i = 0;
let j = n - 1;

while (i < j) {
  const sum = arr[i] + arr[j];

  if (Math.abs(sum) < Math.abs(answer[0] + answer[1])) {
    answer = [arr[i], arr[j]];
  }

  if (sum < 0) {
    i++;
  } else {
    j--;
  }
}

console.log(answer.join(" "));
