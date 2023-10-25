const fs = require("fs");
const sample = `
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
`;
const inputs = sample.toString().trim().split("\n");
const n = Number(inputs[0]);
const answer = [];

for (let i = 0; i < n; i++) {
  const m = Number(inputs[1 + 3 * i]);
  const stickers = inputs
    .slice(3 * i + 2)
    .map((e) => e.split(" ").map((e) => Number(e)));
  const dp = Array.from({ length: 2 }, () =>
    Array.from({ length: m }, () => 0)
  );

  dp[0][0] = stickers[0][0];
  dp[1][0] = stickers[1][0];
  dp[0][1] = dp[1][0] + stickers[0][1];
  dp[1][1] = dp[0][0] + stickers[1][1];

  for (let j = 2; j < m; j++) {
    for (let i = 0; i < 2; i++) {
      dp[i][j] = Math.max(
        dp[1 - i][j - 2] + stickers[i][j],
        dp[1 - i][j - 1] + stickers[i][j]
      );
    }
  }

  answer.push(Math.max(dp[0][m - 1], dp[1][m - 1]));
}

console.log(answer.join("\n"));
