const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const t = Number(inputs[0]);

const getParent = (a, parent) => {
  if (a === parent[a]) {
    return a;
  }

  return (parent[a] = getParent(parent[a], parent));
};

const union = (a, b, parent) => {
  let x = getParent(a, parent);
  let y = getParent(b, parent);

  if (x < y) {
    parent[y] = x;
  } else {
    parent[x] = y;
  }
};

const answer = [];

for (let i = 0; i < t; i++) {
  let startIndex = i * 2 + 1;

  const n = Number(inputs[startIndex]);
  const graph = inputs[startIndex + 1].split(" ").map((e) => Number(e));
  const checked = Array.from({ length: n + 1 }, () => 0);
  let cnt = 0;

  const bfs = (start) => {
    const q = [start];
    const visited = [];

    while (q.length) {
      const current = q.shift();
      visited.push(current);

      let nv = graph[current - 1];

      if (visited.includes(nv)) {
        cnt++;
        break;
      }

      if (!checked[nv]) {
        checked[nv] = 1;
        q.push(nv);
      }
    }
  };

  for (let i = 1; i <= n; i++) {
    if (!checked[i]) {
      checked[i] = 1;
      bfs(i);
    }
  }

  answer.push(cnt);
}

console.log(answer.join("\n"));
