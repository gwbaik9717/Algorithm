// Time Complexity: O(n)

const sample = `6
6
10
13
9
8
1`;

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const arr = inputs.slice(1).map(Number);
const dp = Array.from({ length: n + 1 }, () =>
  Array.from({ length: 2 }, () => 0)
);

dp[1][1] = arr[0];

for (let i = 2; i <= n; i++) {
  // 마지막을 포함하지 않을 때
  dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);

  // 마지막을 포함할 때
  dp[i][1] = Math.max(
    dp[i - 2][0] + arr[i - 2] + arr[i - 1],
    dp[i - 1][0] + arr[i - 1]
  );
}

console.log(Math.max(...dp.at(-1)));
