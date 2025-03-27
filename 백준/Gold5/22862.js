// Time Complexity: O(n)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = inputs[0].split(" ").map(Number);
const arr = inputs[1].split(" ").map(Number);

let answer = 0;
let cnt = 0;
let i = 0;
let j = 0;

while (j < n) {
  if (arr[j] % 2 !== 0) {
    if (cnt < k) {
      cnt++;
    } else {
      if (arr[i] % 2 !== 0) {
        cnt = Math.max(0, cnt - 1);
      }

      i++;
      continue;
    }
  }

  answer = Math.max(answer, j - i + 1 - cnt);
  j++;
}

console.log(answer);
