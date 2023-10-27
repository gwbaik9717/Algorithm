const fs = require("fs");
const sample = `
3 3 2
aaa
aba
aaa
aa
bb
`;
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

class Node {
  constructor(value = "") {
    this.value = value;
    this.next = new Map();
  }
}

class Trie {
  constructor() {
    this.head = new Node();
  }

  add(value) {
    let current = this.head;

    for (let char of value) {
      if (!current.next.has(char)) {
        current.next.set(char, new Node(current.value + char));
      }

      current = current.next.get(char);
    }
  }

  find(value) {
    let current = this.head;

    for (let char of value) {
      if (!current.next.has(char)) {
        return false;
      }

      current = current.next.get(char);
    }

    return true;
  }
}

const inputs = sample.toString().trim().split("\n");
const [n, m, k] = inputs[0].split(" ").map((e) => Number(e));
const graph = inputs.slice(1, 1 + n).map((e) => e.split(""));
const targets = inputs.slice(1 + n);
const trie = new Trie();
const dx = [1, 0, -1, 0, 1, 1, -1, -1];
const dy = [0, 1, 0, -1, 1, -1, -1, 1];
const map = new Map();

for (let target of targets) {
  trie.add(target);
  map.set(target, 0);
}

const bfs = (start) => {
  const q = new Queue();
  q.push(start);

  while (!q.isEmpty()) {
    const [cy, cx, current] = q.shift();

    if (map.has(current)) {
      map.set(current, map.get(current) + 1);
    }

    for (let i = 0; i < 8; i++) {
      let nx = cx + dx[i];
      let ny = cy + dy[i];

      ny = ny >= n ? 0 : ny < 0 ? n - 1 : ny;
      nx = nx >= m ? 0 : nx < 0 ? m - 1 : nx;

      let nv = graph[ny][nx];

      if (trie.find(current + nv)) {
        q.push([ny, nx, current + nv]);
      }
    }
  }
};

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    bfs([i, j, graph[i][j]]);
  }
}

console.log(targets.map((t) => map.get(t)).join("\n"));
