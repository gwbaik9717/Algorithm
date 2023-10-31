const fs = require("fs");
const sample = `
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
`;

class Queue {
  constructor() {
    this.q = [];
    this.head = 0;
    this.rear = 0;
  }

  isEmpty() {
    return this.head === this.rear;
  }

  push(value) {
    this.q.push(value);
    this.rear++;
  }

  shift() {
    let rv = this.q[this.head];
    delete this.q[this.head++];
    return rv;
  }
}

const inputs = sample.toString().trim().split("\n");
const k = Number(inputs[0]);
const [w, h] = inputs[1].split(" ").map((e) => Number(e));
const graph = inputs.slice(2).map((e) => e.split(" ").map((e) => Number(e)));
const checked = Array.from({ length: k + 1 }, () =>
  Array.from({ length: h }, () => Array.from({ length: w }, () => 0))
);

const dx = [1, 1, 2, 2, -1, -1, -2, -2, 1, -1, 0, 0];
const dy = [2, -2, 1, -1, 2, -2, 1, -1, 0, 0, 1, -1];

const q = new Queue();

q.push([0, 0, 0, 0]);

checked[0][0][0] = 1;

let answer = -1;

while (!q.isEmpty()) {
  const [cy, cx, cnt, dist] = q.shift();

  if (cy === h - 1 && cx === w - 1) {
    answer = dist;
    break;
  }

  for (let i = 0; i < dx.length; i++) {
    let nx = cx + dx[i];
    let ny = cy + dy[i];
    let nc = cnt;

    if (Math.abs(dx[i] * dy[i]) === 2) {
      if (nc < k) {
        nc++;
      } else {
        continue;
      }
    }

    if (
      nx >= 0 &&
      nx < w &&
      ny >= 0 &&
      ny < h &&
      graph[ny][nx] === 0 &&
      !checked[nc][ny][nx]
    ) {
      checked[nc][ny][nx] = 1;
      q.push([ny, nx, nc, dist + 1]);
    }
  }
}

console.log(answer);
