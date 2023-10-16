const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map((e) => Number(e));
const lines = inputs.slice(1).map((e) => e.split(" ").map((f) => Number(f)));

const graph = Array.from({ length: n + 1 }, () =>
  Array.from({ length: n + 1 }, () => Infinity)
);

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

let answer = Math.min(...graph.map((e, i) => e[i]));

console.log(answer === Infinity ? -1 : answer);
