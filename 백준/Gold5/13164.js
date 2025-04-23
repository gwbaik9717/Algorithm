// Time Complexity: O(nlogn)

const sample = `8 4
1 2 3 5 7 12 15 16`;
const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = inputs[0].split(" ").map(Number);
const heights = inputs[1].split(" ").map(Number);

const diffs = [];

if (n === k) {
  console.log(0);
  return;
}

for (let i = 1; i < n; i++) {
  diffs.push(heights[i] - heights[i - 1]);
}

diffs.sort((a, b) => a - b);

console.log(diffs.slice(0, n - k).reduce((a, c) => a + c, 0));
