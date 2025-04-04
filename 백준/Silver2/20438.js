// Time Complexity: O(n + m)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k, q, m] = inputs[0].split(" ").map(Number);
const ss = inputs[1].split(" ").map(Number);
const qrs = inputs[2].split(" ").map(Number);
const tcs = inputs.slice(3).map((input) => input.split(" ").map(Number));

const arr = Array.from({ length: n + 3 }, () => 0);

for (const qr of qrs) {
  let current = qr;
  let i = 1;
  if (ss.includes(qr)) {
    continue;
  }

  while (current <= n + 2) {
    arr[current] = 1;
    i++;
    current = qr * i;
  }
}

for (const s of ss) {
  arr[s] = 0;
}

for (let i = 1; i <= n + 2; i++) {
  arr[i] += arr[i - 1];
}

const answer = [];

for (const tc of tcs) {
  const [s, e] = tc;

  answer.push(e - s + 1 - (arr[e] - arr[s - 1]));
}

console.log(answer.join("\n"));
