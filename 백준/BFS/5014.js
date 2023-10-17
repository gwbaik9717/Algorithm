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

const [f, s, g, u, d] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((e) => Number(e));
const options = [u, d * -1];

const q = new Queue();
q.push([s, 0]);
const checked = Array.from({ length: f + 1 }, () => 0);
let answer = "use the stairs";

while (!q.isEmpty()) {
  const [cy, cnt] = q.shift();

  if (cy === g) {
    answer = cnt;
    break;
  }

  options.forEach((dy) => {
    let ny = cy + dy;

    if (ny >= 1 && ny <= f && !checked[ny]) {
      checked[ny] = 1;
      q.push([ny, cnt + 1]);
    }
  });
}

console.log(answer);
