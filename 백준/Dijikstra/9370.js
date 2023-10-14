const fs = require("fs");
const sample = `
2
5 4 2
1 2 3
1 2 6
2 3 2
3 4 4
3 5 3
5
4
6 9 2
2 3 1
1 2 1
1 3 3
2 4 4
2 5 5
3 4 3
3 6 2
4 5 4
4 6 3
5 6 7
5
6
`;

const inputs = sample.toString().trim().split("\n");
const n = Number(inputs[0]);

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

const getMinDist = (n, graph, start) => {
  const heap = new MinHeap();
  const dist = Array.from({ length: n + 1 }, () => Infinity);
  dist[start] = 0;
  heap.push([start, 0]);

  while (!heap.isEmpty()) {
    const [cn, cw] = heap.pop();

    graph[cn].forEach((e) => {
      const [nn, nw] = e;

      if (cw + nw < dist[nn]) {
        dist[nn] = cw + nw;
        heap.push([nn, cw + nw]);
      }
    });
  }

  return dist;
};
let currentIndex = 1;
for (let i = 0; i < n; i++) {
  const [n, m, t] = inputs[currentIndex].split(" ").map((e) => Number(e));
  const [s, g, h] = inputs[currentIndex + 1].split(" ").map((e) => Number(e));
  const lines = inputs
    .slice(currentIndex + 2, currentIndex + 2 + m)
    .map((e) => e.split(" ").map((e) => Number(e)));
  const candidates = inputs
    .slice(currentIndex + 2 + m, currentIndex + 2 + m + t)
    .map((e) => Number(e));

  const graph = Array.from({ length: n + 1 }, () => []);

  lines.forEach((line) => {
    const [start, end, weight] = line;
    graph[start].push([end, weight]);
    graph[end].push([start, weight]);
  });

  const distS = getMinDist(n, graph, s);
  const distG = getMinDist(n, graph, g);
  const distH = getMinDist(n, graph, h);

  let answer = candidates.filter((candidate) => {
    const minDist = distS[candidate];

    if (
      minDist !== Infinity &&
      (minDist === distS[g] + distG[h] + distH[candidate] ||
        minDist === distS[h] + distH[g] + distG[candidate])
    ) {
      return true;
    }
    return false;
  });

  console.log(answer.sort((a, b) => a - b).join(" "));

  currentIndex += 2 + m + t;
}
