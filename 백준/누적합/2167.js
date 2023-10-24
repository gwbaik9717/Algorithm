const fs = require("fs");
const sample = `
3 1
1
1
1
3
2 1 3 1
`;
const inputs = sample.toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map((e) => Number(e));
const psum = inputs
  .slice(1, n + 1)
  .map((e) => e.split(" ").map((e) => Number(e)));
const cs = inputs.slice(n + 2).map((e) => e.split(" ").map((e) => Number(e)));
let answer = [];

// row
for (let i = 0; i < n; i++) {
  for (let j = 1; j < m; j++) {
    psum[i][j] += psum[i][j - 1];
  }
}

// col
for (let j = 0; j < m; j++) {
  for (let i = 1; i < n; i++) {
    psum[i][j] += psum[i - 1][j];
  }
}

for (let c of cs) {
  const [i, j, x, y] = c.map((e) => e - 1);

  const sum =
    psum[x][y] -
    (psum[x][j - 1] || 0) -
    (i >= 1 ? psum[i - 1][y] || 0 : 0) +
    (i >= 1 ? psum[i - 1][j - 1] || 0 : 0);
  answer.push(sum);
}

console.log(answer.join("\n"));
