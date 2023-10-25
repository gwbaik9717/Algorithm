const fs = require("fs");
const sample = `
6
10
20
15
25
10
20
`;
const inputs = sample.toString().trim().split("\n");
const n = Number(inputs[0]);
const stairs = inputs.slice(1).map((e) => Number(e));
stairs.unshift(0);

const dp = Array.from({ length: n + 1 }, () => 0);

dp[1] = stairs[1];
dp[2] = stairs[2] + stairs[1];

for (let i = 3; i <= n; i++) {
  dp[i] = Math.max(
    stairs[i] + dp[i - 2],
    stairs[i] + stairs[i - 1] + dp[i - 3]
  );
}
