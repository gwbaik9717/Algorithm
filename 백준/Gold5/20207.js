const sample = `1
1 365`;

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const schedules = inputs.slice(1).map((input) => input.split(" ").map(Number));

const calendar = Array.from({ length: 366 }, () =>
  Array.from({ length: n }, () => false)
);

// 최대 높이 기록
const heights = Array.from({ length: 366 }, () => -1);

schedules.sort((a, b) => {
  if (a[0] === b[0]) {
    const durationA = a[1] - a[0];
    const durationB = b[1] - b[0];

    return durationB - durationA;
  }

  return a[0] - b[0];
});

for (const [start, end] of schedules) {
  let h = null;

  for (let i = 0; i < n; i++) {
    if (calendar[start][i] === false) {
      h = i;

      break;
    }
  }

  for (let i = start; i <= end; i++) {
    calendar[i][h] = true;

    heights[i] = Math.max(heights[i], h);
  }
}

let answer = 0;
let current = null;

for (let i = 0; i <= 365; i++) {
  if (heights[i] === -1) {
    if (current) {
      answer += current[0] * current[1];
      current = null;
    }

    continue;
  }

  if (!current) {
    current = [1, heights[i] + 1];
    continue;
  }

  current = [current[0] + 1, Math.max(current[1], heights[i] + 1)];
}

if (current) {
  answer += current[0] * current[1];
}

console.log(answer);
