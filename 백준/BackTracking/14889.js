const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = Number(inputs[0]);
const graph = inputs.slice(1).map((e) => e.split(" ").map((e) => Number(e)));
let answer = Number.MAX_SAFE_INTEGER;

const combi = (arr, n) => {
  if (n === 1) {
    return arr.map((e) => [e]);
  }

  let rv = [];

  arr.forEach((fixed, i) => {
    const sliced = arr.slice(i + 1);

    rv.push(...combi(sliced, n - 1).map((e) => [fixed, ...e]));
  });

  return rv;
};

const dfs = (arr, checked, index) => {
  if (arr.length === n / 2) {
    const t1 = combi(arr, 2);
    const t2 = combi(
      checked
        .map((e, i) => [e, i])
        .filter((e) => e[0] === 0)
        .map((e) => e[1]),
      2
    );

    const sum1 = t1.reduce((a, c) => {
      const [x, y] = c;

      return a + graph[x][y] + graph[y][x];
    }, 0);

    const sum2 = t2.reduce((a, c) => {
      const [x, y] = c;

      return a + graph[x][y] + graph[y][x];
    }, 0);

    answer = Math.min(answer, Math.abs(sum1 - sum2));
  } else {
    for (let i = index; i < n; i++) {
      if (!checked[i]) {
        const cloned = [...checked];
        cloned[i] = 1;
        dfs([...arr, i], cloned, i + 1);
      }
    }
  }
};

dfs(
  [],
  Array.from({ length: n }, () => 0),
  0
);

console.log(answer);
