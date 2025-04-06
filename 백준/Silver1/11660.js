// Time Complexity: O(n^2 + m)

const sample = `4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4`;
const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, k] = inputs[0].split(" ").map(Number);

const arr = inputs.slice(1, 1 + n).map((input) => input.split(" ").map(Number));
const tcs = inputs.slice(n + 1).map((input) => input.split(" ").map(Number));

const sum = Array.from({ length: n + 1 }, () =>
  Array.from({ length: n + 1 }, () => 0)
);

for (let i = 1; i < n + 1; i++) {
  for (let j = 1; j < n + 1; j++) {
    sum[i][j] =
      sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + arr[i - 1][j - 1];
  }
}

const answer = [];
for (const [x1, y1, x2, y2] of tcs) {
  answer.push(
    sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1]
  );
}

console.log(answer.join("\n"));
