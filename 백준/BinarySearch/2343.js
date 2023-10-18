const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = inputs[0].split(" ").map((e) => Number(e));
const classes = inputs[1].split(" ").map((e) => Number(e));

let left = 0;
let right = classes.reduce((a, c) => a + c, 0);
let mid = Math.floor((left + right) / 2);

while (left <= right) {
  let cnt = 1;
  let sum = 0;

  let flag = false;

  for (let c of classes) {
    if (sum + c > mid) {
      if (c > mid) {
        flag = true;
        break;
      } else {
        sum = c;
        cnt++;
      }
    } else {
      sum += c;
    }
  }

  if (cnt <= m && !flag) {
    right = mid - 1;
  } else {
    left = mid + 1;
  }

  mid = Math.floor((left + right) / 2);
}

console.log(left);
