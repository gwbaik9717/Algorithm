const sample = `100 6
4 9
9 11
3 4
8 7
1 2
9 8`;

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [c, n] = inputs[0].split(" ").map(Number);
const arr = inputs.slice(1).map((input) => input.split(" ").map(Number));

const dp = Array.from({ length: c + 1 }, () => Number.MAX_SAFE_INTEGER);

for (let i = 1; i <= c; i++) {
  for (let j = 0; j < n; j++) {
    const [cost, ppl] = arr[j];

    if (i <= ppl) {
      dp[i] = Math.min(dp[i], cost);
      continue;
    }

    for (let k = 1; k <= ppl; k++) {
      dp[i] = Math.min(dp[i], dp[i - k] + cost);
    }
  }
}

console.log(dp.at(-1));
