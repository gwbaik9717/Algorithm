const fs = require("fs");
const sample = `
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
`;

const inputs = sample.toString().trim().split("\n");
const n = Number(inputs[0]);

const graph = inputs.slice(1).map((e) => e.split(" ").map((e) => Number(e)));
const dp = Array.from({ length: n }, () =>
  Array.from({ length: n }, () => BigInt(0))
);

dp[0][0] = BigInt(1);

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (i === n - 1 && j === n - 1) {
      break;
    }

    let ny = i;
    let nx = j;

    // 오른쪽
    nx += graph[i][j];

    if (nx >= 0 && nx < n) {
      dp[i][nx] += BigInt(dp[i][j]);
    }

    // 아래
    ny += graph[i][j];

    if (ny >= 0 && ny < n) {
      dp[ny][j] += BigInt(dp[i][j]);
    }
  }
}

console.log(dp[n - 1][n - 1].toString());
