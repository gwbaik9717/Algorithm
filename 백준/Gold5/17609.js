// Time Complexity: O(n)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);

const answer = inputs
  .slice(1)
  .map((input) => {
    const m = input.length;

    let cnt = 0;

    const check = (start, end) => {
      let i = start;
      let j = end;

      while (i < j) {
        if (input[i] !== input[j]) {
          if (cnt === 1) {
            return 2;
          }

          cnt++;

          if (check(i + 1, j) <= 1) {
            return cnt;
          }

          if (check(i, j - 1) <= 1) {
            return cnt;
          }

          return 2;
        }

        i++;
        j--;
      }

      return cnt;
    };

    return check(0, input.length - 1);
  })
  .join("\n");

console.log(answer);
