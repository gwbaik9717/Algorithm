// Time Complexity: O(n^2)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map(Number);

const table = [];

for (let i = 1; i <= n; i++) {
  table.push(inputs[i].split(" ").map(Number));
}

const sum = Array.from({ length: n }, () => Array.from({ length: m }, () => 0));

sum[0][0] = table[0][0];

for (let i = 1; i < n; i++) {
  sum[i][0] = sum[i - 1][0] + table[i][0];
}

for (let j = 1; j < m; j++) {
  sum[0][j] = sum[0][j - 1] + table[0][j];
}

for (let i = 1; i < n; i++) {
  for (let j = 1; j < m; j++) {
    sum[i][j] = sum[i][j - 1] + sum[i - 1][j] + table[i][j] - sum[i - 1][j - 1];
  }
}

const k = Number(inputs[n + 1]);
const answer = [];

for (let m = 0; m < k; m++) {
  const [i, j, x, y] = inputs[n + 2 + m].split(" ").map((e) => Number(e) - 1);

  answer.push(
    sum[x][y] -
      (j >= 1 ? sum[x][j - 1] : 0) -
      (i >= 1 ? sum[i - 1][y] : 0) +
      (i >= 1 && j >= 1 ? sum[i - 1][j - 1] : 0)
  );
}

console.log(answer.join("\n"));
