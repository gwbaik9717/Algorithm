const sample = `4
868 4096 8976 499`;

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const arr = inputs[1].split(" ").map(Number);

const sum = Array.from({ length: n }, () => 0);
sum[0] = arr[0];

for (let i = 1; i < n; i++) {
  sum[i] = sum[i - 1] + arr[i];
}

const reversed_sum = Array.from({ length: n }, () => 0);
reversed_sum[n - 1] = arr[n - 1];
for (let i = n - 2; i >= 0; i--) {
  reversed_sum[i] = reversed_sum[i + 1] + arr[i];
}

let answer = Number.MIN_SAFE_INTEGER;

for (let i = 1; i < n - 1; i++) {
  // case 1
  answer = Math.max(answer, sum[n - 1] - sum[0] + sum[n - 1] - sum[i] - arr[i]);

  // case 2
  answer = Math.max(
    answer,
    sum[i] - sum[0] + sum[n - 1] - sum[i - 1] - arr[n - 1]
  );

  // case 3
  answer = Math.max(
    answer,
    reversed_sum[0] -
      reversed_sum[n - 1] +
      reversed_sum[0] -
      reversed_sum[i] -
      arr[i]
  );
}

console.log(answer);
