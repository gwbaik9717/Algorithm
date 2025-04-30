const sample = `10
11 17 5 2 20 7 5 5 20 7
5
18 18 15 15 17`;

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(inputs[0]);
const crains = inputs[1].split(" ").map(Number);

const m = Number(inputs[2]);
let boxes = inputs[3].split(" ").map(Number);

crains.sort((a, b) => b - a);
boxes.sort((a, b) => b - a);

let cnt = 0;

let prevBoxesLength = boxes.length;

while (boxes.length > 0) {
  for (const crain of crains) {
    if (crain >= boxes[0]) {
      boxes.shift();
      continue;
    }

    if (boxes.at(-1) > crain) {
      break;
    }

    for (let i = 0; i < boxes.length; i++) {
      const box = boxes[i];

      if (crain >= box) {
        boxes = boxes.slice(0, i).concat(boxes.slice(i + 1));
        break;
      }
    }
  }

  if (boxes.length === prevBoxesLength) {
    console.log(-1);
    return;
  }

  prevBoxesLength = boxes.length;
  cnt++;
}

console.log(cnt);
