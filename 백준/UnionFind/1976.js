const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const graph = inputs
  .slice(2, -1)
  .map((e) => e.split(" ").map((e) => Number(e)));
const plan = inputs
  .slice(-1)[0]
  .split(" ")
  .map((e) => Number(e));

const parent = Array.from({ length: n + 1 }, (_, i) => i);

const getParent = (a, parent) => {
  if (a === parent[a]) {
    return a;
  }

  return (parent[a] = getParent(parent[a], parent));
};

const union = (a, b, parent) => {
  let x = getParent(a, parent);
  let y = getParent(b, parent);

  if (x < y) {
    parent[y] = x;
  } else {
    parent[x] = y;
  }
};

graph.forEach((row, i) => {
  row.forEach((col, j) => {
    if (col) {
      union(i + 1, j + 1, parent);
    }
  });
});

for (let i = 1; i <= n; i++) {
  getParent(i, parent);
}

let num = new Set(plan.map((p) => parent[p])).size;

console.log(num === 1 ? "YES" : "NO");
