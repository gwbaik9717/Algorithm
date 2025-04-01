// Time Complexity: O(n^2)

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const arr = inputs[1].split(" ").map(Number);

arr.sort((a, b) => a - b);

let answer = 0;

for (let i = 0; i <= n - 3; i++) {
  const target = 0 - arr[i];

  let j = i + 1;
  let k = n - 1;

  while (j < k) {
    if (arr[j] + arr[k] > target) {
      k--;
    } else if (arr[j] + arr[k] < target) {
      j++;
    } else {
      if (arr[j] === arr[k]) {
        answer += k - j;
        j++;
      } else {
        let start = j;
        let end = k;

        while (arr[start] === arr[j]) {
          start++;
        }

        while (arr[end] === arr[k]) {
          end--;
        }

        answer += (start - j) * (k - end);
        j = start;
        k = end;
      }
    }
  }
}

console.log(answer);
