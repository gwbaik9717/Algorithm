const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = inputs[0].split(" ").map((e) => Number(e));
const graph = inputs.slice(1).map((e) => e.split(" ").map((e) => Number(e)));
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

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

const bfs = (start, checked) => {
  const q = new Queue();
  q.push(start);

  checked[start[0]][start[1]] = 1;

  while (!q.isEmpty()) {
    const [cy, cx] = q.shift();

    dx.forEach((e, i) => {
      let nx = cx + e;
      let ny = cy + dy[i];

      if (
        nx >= 0 &&
        nx < m &&
        ny >= 0 &&
        ny < n &&
        !checked[ny][nx] &&
        graph[ny][nx]
      ) {
        checked[ny][nx] = 1;
        q.push([ny, nx]);
      }
    });
  }
};

const melt = (graph) => {
  const dh = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => 0)
  );
  let isMelted = true;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (graph[i][j]) {
        dx.forEach((e, index) => {
          let nx = j + e;
          let ny = i + dy[index];

          if (nx >= 0 && nx < m && ny >= 0 && ny < n && !graph[ny][nx]) {
            dh[i][j]++;
          }
        });
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      graph[i][j] -= dh[i][j];
      graph[i][j] = Math.max(0, graph[i][j]);

      if (graph[i][j]) {
        isMelted = false;
      }
    }
  }

  return isMelted;
};

let flag = false;
let answer = 0;
while (!melt(graph)) {
  let cnt = 0;
  const checked = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => 0)
  );
  answer++;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (graph[i][j] && !checked[i][j]) {
        bfs([i, j], checked);
        cnt++;
      }
    }
  }

  if (cnt > 1) {
    flag = true;
    break;
  }
}

if (flag) {
  console.log(answer);
} else {
  console.log(0);
}
