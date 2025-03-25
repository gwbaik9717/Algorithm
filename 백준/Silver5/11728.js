const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const arr1 = inputs[1].split(" ").map(Number);
const arr2 = inputs[2].split(" ").map(Number);

const n = Number(arr1.length);
const m = Number(arr2.length);

let i = 0;
let j = 0;

const answer = [];

while (i < n && j < m) {
  if (arr1[i] <= arr2[j]) {
    answer.push(arr1[i]);
    i++;
  } else {
    answer.push(arr2[j]);
    j++;
  }
}

while (i < n) {
  answer.push(arr1[i]);
  i++;
}

while (j < m) {
  answer.push(arr2[j]);
  j++;
}

console.log(answer.join(" "));
