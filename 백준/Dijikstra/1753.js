const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [v, e] = inputs[0].split(" ").map((e) => Number(e));
const start = Number(inputs[1]);
const nodes = inputs.slice(2).map((e) => e.split(" ").map((e) => Number(e)));

const graph = Array.from({ length: v + 1 }, () => []);
const dist = Array.from({ length: v + 1 }, () => Infinity);

nodes.forEach((node) => {
  const [st, end, weight] = node;
  graph[st].push([end, weight]);
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

const heap = new MinHeap();

heap.push([start, 0]);

dist[start] = 0;

while (!heap.isEmpty()) {
  const [start, weight] = heap.pop();

  graph[start].forEach((v) => {
    const [end, nw] = v;
    if (weight + nw < dist[end]) {
      dist[end] = Math.min(dist[end], weight + nw);
      heap.push([end, weight + nw]);
    }
  });
}

console.log(
  dist
    .slice(1)
    .map((e) => (e === Infinity ? "INF" : e))
    .join("\n")
);
