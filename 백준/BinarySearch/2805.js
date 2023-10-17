const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map((e) => Number(e));
const trees = inputs[1].split(" ").map((e) => Number(e));

let left = 0;
let right = Math.max(...trees);
let mid = Math.floor((left + right) / 2);

while (left <= right) {
  const cutted = trees.reduce((a, c) => {
    return a + Math.max(0, c - mid);
  }, 0);

  if (cutted >= m) {
    left = mid + 1;
  } else {
    right = mid - 1;
  }

  mid = Math.floor((left + right) / 2);
}

console.log(right);
