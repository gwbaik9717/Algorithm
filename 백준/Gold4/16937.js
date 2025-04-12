// Time Complexity: O(n * k)

const sample = `6 7
0 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
0 0 0 0 0 0 0
2 3 1 1 5 5`;

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
    const rv = this.q[this.head];
    delete this.q[this.head++];
    return rv;
  }
}

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, k] = inputs[0].split(" ").map(Number);
const graph = inputs.slice(1, 1 + n).map((row) => row.split(" ").map(Number));
const [h, w, sr, sc, fr, fc] = inputs[1 + n].split(" ").map(Number);

const dy = [1, 0, -1, 0];
const dx = [0, 1, 0, -1];

// 누적합
const dp = Array.from({ length: n + 1 }, () =>
  Array.from({ length: k + 1 }, () => 0)
);

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= k; j++) {
    dp[i][j] =
      dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + graph[i - 1][j - 1];
  }
}

const checked = Array.from({ length: n + 1 }, () =>
  Array.from({ length: k + 1 }, () => false)
);
checked[sr][sc] = true;

const q = new Queue();
q.push([sr, sc, 0]);

let answer = -1;

const hasWall = (sy, sx) => {
  const [ey, ex] = [sy + h - 1, sx + w - 1];

  return dp[ey][ex] - dp[sy - 1][ex] - dp[ey][sx - 1] + dp[sy - 1][sx - 1] > 0;
};

while (!q.isEmpty()) {
  const [cy, cx, cc] = q.shift();

  checked[cy][cx] = true;

  if (cy === fr && cx === fc) {
    answer = cc;
    break;
  }

  for (let i = 0; i < 4; i++) {
    const [ny, nx] = [cy + dy[i], cx + dx[i]];

    if (
      ny >= 1 &&
      ny + h - 1 <= n &&
      nx >= 1 &&
      nx + w - 1 <= k &&
      !hasWall(ny, nx) &&
      !checked[ny][nx]
    ) {
      q.push([ny, nx, cc + 1]);
    }
  }
}

console.log(answer);
