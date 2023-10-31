const fs = require("fs");
const sample = `
6 5
1 2
2 5
5 1
3 4
4 6
`;

const inputs = sample.toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map((e) => Number(e));

const getParent = (a, parent) => {
  if (a === parent[a]) {
    return a;
  }

  return (parent[a] = getParent(parent[a], parent));
};

const union = (a, b, parent) => {
  const parentA = getParent(a, parent);
  const parentB = getParent(b, parent);

  if (parentA < parentB) {
    parent[parentB] = parentA;
  } else {
    parent[parentA] = parentB;
  }
};

const parent = Array.from({ length: n + 1 }, (_, i) => i);

inputs.slice(1).forEach((e) => {
  const [start, end] = e.split(" ").map((e) => Number(e));

  union(start, end, parent);
});

for (let i = 1; i <= n; i++) {
  getParent(i, parent);
}

console.log(new Set(parent.slice(1)).size);
