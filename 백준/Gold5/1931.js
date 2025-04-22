// Time Complexity: O(nlogn)

const sample = `5
3 3
1 2
2 3
3 4
4 5`;
const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
candidates = inputs.slice(1).map((input) => input.split(" ").map(Number));

candidates.sort((a, b) => {
  if (a[1] === b[1]) {
    return a[0] - b[0];
  }

  return a[1] - b[1];
});

let answer = 1;
let current = candidates[0];

for (let i = 1; i < n; i++) {
  const [ns, ne] = candidates[i];

  if (ns >= current[1]) {
    current = [ns, ne];
    answer++;
    continue;
  }
}

console.log(answer);
