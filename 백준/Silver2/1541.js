// Time Complexity: O(n)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let splitted = inputs[0].split("-");

splitted = splitted.map((s) =>
  s.split("+").reduce((a, c) => {
    return a + Number(c);
  }, 0)
);

if (splitted.length === 1) {
  console.log(splitted[0]);

  return;
}

const answer = splitted.slice(1).reduce((a, c) => {
  return a - c;
}, splitted[0]);

console.log(answer);
