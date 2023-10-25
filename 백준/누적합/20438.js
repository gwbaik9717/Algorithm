const fs = require("fs");
const sample = `
50 4 5 1
24 15 27 43
3 4 6 20 25
3 52
`;
const inputs = sample.toString().trim().split("\n");
let answer = [];
const [n, k, q, m] = inputs[0].split(" ").map((e) => Number(e));
const sleep = inputs[1].split(" ").map((e) => Number(e));
const qs = inputs[2].split(" ").map((e) => Number(e));
const tcs = inputs.slice(3).map((e) => e.split(" ").map((e) => Number(e)));
const checked = Array.from({ length: n + 3 }, () => 0);

for (let q of qs) {
  let temp = q;
  let i = 1;

  if (sleep.includes(q)) {
    continue;
  }

  while (temp <= n + 2) {
    if (!sleep.includes(temp)) {
      checked[temp] = 1;
    }

    i++;
    temp = q * i;
  }
}

const mapped = checked.map((e) => (e === 0 ? 1 : 0));

for (let i = 1; i < mapped.length; i++) {
  mapped[i] += mapped[i - 1];
}

tcs.forEach((tc) => {
  const [start, end] = tc;
  answer.push(mapped[end] - mapped[start - 1]);
});

console.log(answer.join("\n"));
