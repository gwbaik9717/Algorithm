const fs = require("fs");
const sample = `
2
6
12
`;

const inputs = sample.toString().trim().split("\n");
const n = Number(inputs[0]);
const max = Math.max(...inputs.slice(1).map((e) => Number(e)));
const memo = Array.from({ length: max + 1 }, () => 0);

memo[1] = 1;
memo[2] = 1;
memo[3] = 1;
memo[4] = 2;

for (let i = 5; i <= max; i++) {
  memo[i] = memo[i - 1] + memo[i - 5];
}

const answer = [];

inputs
  .slice(1)
  .map((e) => Number(e))
  .forEach((e) => {
    answer.push(memo[e]);
  });

console.log(answer.join("\n"));
