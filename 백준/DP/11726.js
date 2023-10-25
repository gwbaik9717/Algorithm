const fs = require("fs");
const sample = `
100
`;
const inputs = sample.toString().trim().split("\n");
const n = Number(inputs[0]);

const dp = Array.from({ length: n + 1 }, () => 0);

dp[1] = 1;
dp[2] = 2;

for (let i = 3; i <= n; i++) {
  dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
}

console.log(dp[n]);
