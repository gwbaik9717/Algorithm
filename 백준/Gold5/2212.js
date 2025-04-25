// Time Complexity: O(nlogn)

const sample = `10
5
20 3 14 6 7 8 18 10 12 15`;
const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const k = Number(inputs[1]);
const sensors = inputs[2].split(" ").map(Number);

sensors.sort((a, b) => a - b);

const diffs = [];

for (let i = 1; i < n; i++) {
  diffs.push(sensors[i] - sensors[i - 1]);
}

diffs.sort((a, b) => b - a);

console.log(diffs.slice(k - 1).reduce((a, c) => a + c, 0));
