// Time Complexity: O(n)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [s, p] = inputs[0].split(" ").map(Number);
const arr = inputs[1].split("");
const target = inputs[2].split(" ").map(Number);

let i = 0;
let j = p - 1;
const status = [0, 0, 0, 0];

const mapping = {
  A: 0,
  C: 1,
  G: 2,
  T: 3,
};

arr.slice(i, j + 1).forEach((c) => {
  if (mapping[c] !== undefined) {
    status[mapping[c]]++;
  }
});

const check = (status) => {
  for (let i = 0; i < target.length; i++) {
    if (status[i] < target[i]) {
      return false;
    }
  }

  return true;
};

let answer = 0;

while (j < s) {
  if (check(status)) {
    answer++;
  }

  if (j === s - 1) {
    break;
  }

  if (mapping[arr[i]] !== undefined) {
    status[mapping[arr[i]]]--;
    i++;
  }

  if (mapping[arr[++j]] !== undefined) {
    status[mapping[arr[j]]]++;
  }
}

console.log(answer);
