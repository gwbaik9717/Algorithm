const fs = require("fs");

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

const [s, k] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((e) => Number(e));
const dx = [-1, 1, 2];
const checked = Array.from({ length: 100001 }, () => 0);
const q = new Queue();
q.push([s, 0]);

while (!q.isEmpty()) {
  const [cx, cnt] = q.shift();

  if (cx === k) {
    console.log(cnt);
    break;
  }

  dx.forEach((e) => {
    let nx;
    if (e === 2) {
      nx = cx * 2;
    } else {
      nx = cx + e;
    }

    if (nx >= 0 && nx <= 100000 && !checked[nx]) {
      checked[nx] = 1;
      q.push([nx, cnt + 1]);
    }
  });
}
