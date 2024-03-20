const fs = require("fs");
const sample = `
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
`;

const inputs = sample.toString().trim().split("\n");
const [m, n] = inputs[0].split(" ").map((e) => Number(e));
const graph = inputs.slice(1).map((e) => e.split(""));

const dy = [1, 0, -1, 0];
const dx = [0, 1, 0, -1];
let answer = 0;

const dfs = (cy, cx, count, visited) => {
  let maxCount = count;

  visited[graph[cy][cx].charCodeAt() - 65] = true;

  dx.forEach((x, i) => {
    const nx = x + cx;
    const ny = dy[i] + cy;

    if (
      nx >= 0 &&
      nx < n &&
      ny >= 0 &&
      ny < m &&
      !visited[graph[ny][nx].charCodeAt() - 65]
    ) {
      maxCount = Math.max(maxCount, dfs(ny, nx, count + 1, visited));
    }
  });

  visited[graph[cy][cx].charCodeAt() - 65] = false;

  return maxCount;
};

const visited = Array(26).fill(false);

console.log(dfs(0, 0, 1, visited));
