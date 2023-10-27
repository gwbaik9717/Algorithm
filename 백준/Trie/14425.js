const fs = require("fs");
const sample = `
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
`;

const inputs = sample.toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map((e) => Number(e));
const samples = inputs.slice(1, 1 + n);
const tcs = inputs.slice(1 + n);
let answer = 0;

const set = new Set();

for (let sample of samples) {
  set.add(sample);
}

for (let tc of tcs) {
  if (set.has(tc)) {
    answer++;
  }
}

console.log(answer);
