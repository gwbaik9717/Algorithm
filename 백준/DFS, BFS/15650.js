const fs = require("fs");
const [n, m] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((e) => Number(e));

const combi = (arr, m) => {
  if (m === 1) {
    return arr.map((e) => [e]);
  }

  let rv = [];

  arr.forEach((fixed, i) => {
    const sliced = arr.slice(i + 1);

    rv.push(...combi(sliced, m - 1).map((e) => [fixed, ...e]));
  });

  return rv;
};

const arr = Array.from({ length: n }, (_, i) => i + 1);

combi(arr, m).forEach((e) => {
  console.log(e.join(" "));
});
