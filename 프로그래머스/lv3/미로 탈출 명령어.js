class Queue {
  constructor() {
    this.q = [];
    this.head = 0;
    this.tail = 0;
  }

  push(value) {
    this.q.push(value);
    this.tail++;
  }

  pop() {
    const rv = this.q[this.head];
    delete this.q[this.head++];
    return rv;
  }

  isEmpty() {
    return this.head === this.tail;
  }
}

function solution(n, m, x, y, r, c, k) {
  const dir = ["d", "l", "r", "u"];
  const dx = [1, 0, 0, -1];
  const dy = [0, -1, 1, 0];

  // Early return if impossible
  const distance = Math.abs(r - x) + Math.abs(c - y);
  if (distance > k || (k - distance) % 2 !== 0) return "impossible";

  const queue = new Queue();
  queue.push([x, y, ""]);
  const visited = new Set();
  visited.add(`${x},${y},0`);

  while (!queue.isEmpty()) {
    const [cx, cy, path] = queue.pop();

    if (path.length === k) {
      if (cx === r && cy === c) return path;
      continue;
    }

    for (let i = 0; i < 4; i++) {
      const nx = cx + dx[i];
      const ny = cy + dy[i];
      const newPath = path + dir[i];

      if (
        nx >= 1 &&
        nx <= n &&
        ny >= 1 &&
        ny <= m &&
        !visited.has(`${nx},${ny},${newPath.length}`)
      ) {
        queue.push([nx, ny, newPath]);
        visited.add(`${nx},${ny},${newPath.length}`);
      }
    }
  }

  return "impossible";
}
