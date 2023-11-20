const fs = require("fs");

const sample = `5 4
.D.*
....
..X.
S.*.
....`;

// const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const inputs = sample.toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map((e) => Number(e));
const graph = inputs.slice(1).map((e) => e.split(""));
const checked = Array.from({ length: n }, () =>
  Array.from({ length: m }, () => 0)
);
const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

let water = 0;

// start
const sy = graph.findIndex((row) => row.includes("S"));
const sx = graph[sy].findIndex((col) => col === "S");
checked[sy][sx] = 1;

const q = [[sy, sx, 0]];

let answer;

while (q.length > 0) {
  const [cy, cx, dist] = q.shift();

  if (graph[cy][cx] === "D") {
    answer = dist;
    break;
  }

  if (dist + 1 > water) {
    const temp = [];
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < m; j++) {
        if (graph[i][j] === "*") {
          for (let k = 0; k < 4; k++) {
            let ny = i + dy[k];
            let nx = j + dx[k];

            if (
              nx >= 0 &&
              nx < m &&
              ny >= 0 &&
              ny < n &&
              [".", "S"].includes(graph[ny][nx])
            ) {
              temp.push([ny, nx]);
            }
          }
        }
      }
    }

    for (let [ny, nx] of temp) {
      graph[ny][nx] = "*";
    }

    water = dist + 1;
  }

  for (let i = 0; i < 4; i++) {
    let ny = cy + dy[i];
    let nx = cx + dx[i];

    if (
      nx >= 0 &&
      nx < m &&
      ny >= 0 &&
      ny < n &&
      graph[ny][nx] !== "*" &&
      graph[ny][nx] !== "X" &&
      !checked[ny][nx]
    ) {
      checked[ny][nx] = 1;
      q.push([ny, nx, dist + 1]);
    }
  }
}

console.log(answer ? answer : "KAKTUS");
