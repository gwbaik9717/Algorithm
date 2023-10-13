const fs = require("fs");
const [n, m] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((e) => Number(e));

const dfs = (arr, start) => {
  if (arr.length === m) {
    console.log(arr.join(" "));
  } else {
    for (let i = start; i <= n; i++) {
      dfs([...arr, i], i);
    }
  }
};

dfs([], 1);
