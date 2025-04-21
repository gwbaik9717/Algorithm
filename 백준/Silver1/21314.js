// Time Complexity: O(n)
const sample = "MMM";
const fs = require("fs");
const inputs = sample.toString().trim().split("\n");

const splitted = inputs[0].split("");

// 1. 최솟값 구하기
const minVal = [];
{
  let countM = 0;
  for (let i = 0; i < splitted.length; i++) {
    if (splitted[i] === "M") {
      countM++;
    } else {
      if (countM > 0) {
        minVal.push(Math.pow(10, countM - 1));
        countM = 0;
      }

      minVal.push(5);
    }
  }

  if (countM > 0) {
    minVal.push(Math.pow(10, countM - 1));
    countM = 0;
  }
}

// 2. 최댓값 구하기
const maxVal = [];
{
  let countM = 0;
  for (let i = 0; i < splitted.length; i++) {
    if (splitted[i] === "M") {
      countM++;
    } else {
      maxVal.push(5 * Math.pow(10, countM));
      countM = 0;
    }
  }

  for (let i = 0; i < countM; i++) {
    maxVal.push(1);
  }
}

console.log(maxVal.join(""));
console.log(minVal.join(""));
