const fs = require("fs");
const sample = `
3 10
1
2
5
`;

const inputs = sample.toString().trim().split("\n");
const [n, k] = inputs[0].split(" ").map((e) => Number(e));
const kinds = inputs
  .slice(1)
  .map((e) => Number(e))
  .sort((a, b) => a - b);

const temp = Array.from({ length: 2 }, () =>
  Array.from({ length: k + 1 }, () => 0)
);
let answer;

for (let i = 0; i < n; i++) {
  let ck = kinds[i];

  for (let j = 1; j <= k; j++) {
    temp[1][j] = temp[0][j] + (temp[1][j - ck] || 0) + (j === ck ? 1 : 0);
  }

  answer = temp[1][k];

  temp[0] = [...temp[1]];
  temp[1] = Array.from({ length: k + 1 }, () => 0);
}

console.log(answer);
