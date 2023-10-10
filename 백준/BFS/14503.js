const fs = require("fs");
const sample = `
3 3
1 1 0
1 1 1
1 0 1
1 1 1
`;
const inputs = sample.toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map((e) => Number(e));
const [y, x, dir] = inputs[1].split(" ").map((e) => Number(e));
const graph = inputs.slice(2).map((e) => e.split(" ").map((e) => Number(e)));
const checked = Array.from({ length: n }, () =>
  Array.from({ length: m }, () => 0)
);

const dy = [-1, 0, 1, 0];
const dx = [0, 1, 0, -1];

const q = [[y, x, dir]];

while (q.length) {
  const [cy, cx, cd] = q.shift();

  if (graph[cy][cx] === 0 && !checked[cy][cx]) {
    checked[cy][cx] = 1;
  }

  let flag = false;

  for (let i = 0; i < dx.length; i++) {
    let nx = cx + dx[i];
    let ny = cy + dy[i];

    if (
      nx >= 0 &&
      nx < m &&
      ny >= 0 &&
      ny < n &&
      graph[ny][nx] === 0 &&
      !checked[ny][nx]
    ) {
      let nd = cd - 1;

      if (nd < 0) {
        nd = 3;
      }

      ny = cy + dy[nd];
      nx = cx + dx[nd];

      if (graph[ny][nx] === 0 && !checked[ny][nx]) {
        q.push([ny, nx, nd]);
      } else {
        q.push([cy, cx, nd]);
      }

      flag = true;
      break;
    }
  }

  if (!flag) {
    let nx = cx + -1 * dx[cd];
    let ny = cy + -1 * dy[cd];

    if (nx >= 0 && nx < m && ny >= 0 && ny < n && graph[ny][nx] === 0) {
      q.push([ny, nx, cd]);
    } else {
      break;
    }
  }
}

console.log(checked.flatMap((e) => e).filter((e) => e > 0).length);
