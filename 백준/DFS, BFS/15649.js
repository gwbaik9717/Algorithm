const fs = require("fs");
const sample = `
3 1
`;
const [n, m] = sample
  .toString()
  .trim()
  .split(" ")
  .map((e) => Number(e));

const perm = (arr, m) => {
  if (m === 1) {
    return arr.map((e) => [e]);
  }

  let rv = [];

  arr.forEach((fixed, i) => {
    const filtered = arr.filter((_, j) => i !== j);

    rv.push(...perm(filtered, m - 1).map((e) => [fixed, ...e]));
  });

  return rv;
};

const arr = Array.from({ length: n }, (_, i) => i + 1);

perm(arr, m).forEach((e) => {
  console.log(e.join(" "));
});
