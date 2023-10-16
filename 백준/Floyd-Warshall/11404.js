const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = Number(inputs[0]);
const m = Number(inputs[1]);
const lines = inputs.slice(2).map((e) => e.split(" ").map((f) => Number(f)));

const graph = Array.from({ length: n + 1 }, () =>
  Array.from({ length: n + 1 }, () => Infinity)
);

for (let i = 1; i <= n; i++) {
  graph[i][i] = 0;
}

lines.forEach((line) => {
  const [a, b, c] = line;
  graph[a][b] = Math.min(graph[a][b], c);
});

for (let i = 1; i <= n; i++) {
  // i 노드를 지나칠 때
  for (let j = 1; j <= n; j++) {
    for (let k = 1; k <= n; k++) {
      graph[j][k] = Math.min(graph[j][k], graph[j][i] + graph[i][k]);
    }
  }
}

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= n; j++) {
    if (graph[i][j] === Infinity) {
      graph[i][j] = 0;
    }
  }
}

console.log(
  graph
    .slice(1)
    .map((e) => e.slice(1).join(" "))
    .join("\n")
);
