const fs = require("fs");
const [n, m] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((e) => Number(e));
let result = "";

const perm = (arr, m) => {
  if (m === 1) {
    return arr.map((e) => [e]);
  }

  let rv = [];

  arr.forEach((fixed, i) => {
    rv.push(...perm(arr, m - 1).map((e) => [fixed, ...e]));
  });

  return rv;
};

const arr = Array.from({ length: n }, (_, i) => i + 1);

perm(arr, m).forEach((e) => {
  result += `${e.join(" ")}\n`;
});

console.log(result.trim());
