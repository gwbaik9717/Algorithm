const fs = require("fs");
const sample = `
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
`;
let answer = Number.MAX_SAFE_INTEGER;
const inputs = sample.toString().trim().split("\n");
const n = Number(inputs[0]);
const graph = inputs.slice(1).map((e) => e.split(" ").map((e) => Number(e)));

class Queue {
  constructor() {
    this.q = [];
    this.head = 0;
    this.rear = 0;
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

  isEmpty() {
    return this.head === this.rear;
  }
}

const bfs = (start) => {
  const q = new Queue();

  q.push([start, 0, [start]]);

  let ans = Number.MAX_SAFE_INTEGER;

  while (!q.isEmpty()) {
    const [current, cc, paths] = q.shift();

    if (cc >= answer) {
      continue;
    }

    if (paths.length === n) {
      if (graph[current][start]) {
        ans = Math.min(ans, graph[current][start] + cc);
      }
      continue;
    }

    graph[current].forEach((nc, i) => {
      if (nc && !paths.includes(i)) {
        q.push([i, cc + nc, [...paths, i]]);
      }
    });
  }

  return ans;
};

for (let i = 0; i < n; i++) {
  answer = Math.min(answer, bfs(i));
}

console.log(answer);
