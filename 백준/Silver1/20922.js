// Time Complexity: O(n)

const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = inputs[0].split(" ").map(Number);
const arr = inputs[1].split(" ").map(Number);

let answer = 0;

let i = 0;
let j = 0;

const map = new Map();

while (j < n) {
  if (map.get(arr[j]) >= k) {
    map.set(arr[i], map.get(arr[i]) - 1);
    i++;
  } else {
    map.set(arr[j], (map.get(arr[j]) ?? 0) + 1);
    answer = Math.max(answer, j - i + 1);
    j++;
  }
}

console.log(answer);
