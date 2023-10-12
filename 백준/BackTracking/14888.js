const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const operands = inputs[1].split(" ").map((e) => Number(e));
const operators = inputs[2].split(" ").map((e) => Number(e));
let max = Number.MIN_SAFE_INTEGER;
let min = Number.MAX_SAFE_INTEGER;

const dfs = (operators, sum, index) => {
  if (index >= operands.length) {
    sum = sum === 0 ? 0 : sum;
    max = Math.max(max, sum);
    min = Math.min(min, sum);
  } else {
    for (let i = 0; i < operators.length; i++) {
      if (operators[i]) {
        const cloned = [...operators];
        cloned[i]--;
        let current = operands[index];
        let temp = sum;

        switch (i) {
          case 0:
            temp += current;
            break;
          case 1:
            temp -= current;
            break;
          case 2:
            temp *= current;
            break;
          case 3:
            if (temp * current < 0) {
              temp = Math.floor(Math.abs(temp / current)) * -1;
            } else {
              temp = Math.floor(temp / current);
            }
            break;
          default:
            break;
        }

        dfs(cloned, temp, index + 1);
      }
    }
  }
};

dfs([...operators], operands[0], 1);

console.log(max);
console.log(min);
