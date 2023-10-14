const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, e] = inputs[0].split(" ").map((e) => Number(e));
const lines = inputs
  .slice(1, -1)
  .map((e) => e.split(" ").map((e) => Number(e)));

const graph = Array.from({ length: n + 1 }, () => []);
const [x, y] = inputs
  .slice(-1)[0]
  .split(" ")
  .map((e) => Number(e));

lines.forEach((line) => {
  const [start, end, weight] = line;
  graph[start].push([end, weight]);
  graph[end].push([start, weight]);
});

class MinHeap {
  constructor() {
    this.heap = [null];
  }

  push(value) {
    this.heap.push(value);
    let current = this.heap.length - 1;
    let parent = Math.floor(current / 2);

    while (parent && this.heap[current][1] < this.heap[parent][1]) {
      [this.heap[current], this.heap[parent]] = [
        this.heap[parent],
        this.heap[current],
      ];
      current = parent;
      parent = Math.floor(current / 2);
    }
  }

  pop() {
    if (this.heap.length === 1) return;
    if (this.heap.length === 2) return this.heap.pop();

    let current = 1;
    let left = 2;
    let right = 3;

    let rv = this.heap[current];

    this.heap[current] = this.heap.pop();

    while (
      (this.heap[left] && this.heap[current][1] > this.heap[left][1]) ||
      (this.heap[right] && this.heap[current][1] > this.heap[right][1])
    ) {
      if (this.heap[right] && this.heap[left][1] > this.heap[right][1]) {
        [this.heap[right], this.heap[current]] = [
          this.heap[current],
          this.heap[right],
        ];
        current = right;
      } else {
        [this.heap[left], this.heap[current]] = [
          this.heap[current],
          this.heap[left],
        ];
        current = left;
      }

      left = current * 2;
      right = left + 1;
    }

    return rv;
  }

  isEmpty() {
    return this.heap.length === 1;
  }
}

const getMinDist = (start, end) => {
  const heap = new MinHeap();
  const dist = Array.from({ length: n + 1 }, () => Infinity);
  dist[start] = 0;
  heap.push([start, 0]);

  while (!heap.isEmpty()) {
    const [cn, cw] = heap.pop();

    if (cn === end) {
      return cw;
    }

    graph[cn].forEach((e) => {
      const [nn, nw] = e;

      if (cw + nw < dist[nn]) {
        dist[nn] = cw + nw;
        heap.push([nn, cw + nw]);
      }
    });
  }

  return Infinity;
};

const paths = [
  [1, x, y, n],
  [1, y, x, n],
];

let answer = paths.reduce((a, c) => {
  let sum = 0;
  for (let i = 0; i < c.length - 1; i++) {
    sum += getMinDist(c[i], c[i + 1]);
  }

  return Math.min(a, sum);
}, Infinity);

console.log(answer === Infinity ? -1 : answer);
