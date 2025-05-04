const sample = `4 7
6 13
4 8
3 6
5 12`;

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = inputs[0].split(" ").map(Number);
const arr = inputs.slice(1).map((input) => input.split(" ").map(Number));

const dp = Array.from({ length: k + 1 }, () =>
  Array.from({ length: n + 1 }, () => 0)
);

for (let i = 1; i <= k; i++) {
  for (let j = 1; j <= n; j++) {
    dp[i][j] = Math.max(dp[i][j], dp[i][j - 1]);

    const [w, v] = arr[j - 1];

    if (i < w) {
      continue;
    }

    dp[i][j] = Math.max(dp[i][j], dp[i - w][j - 1] + v);
  }
}

console.log(dp.at(-1).at(-1));
