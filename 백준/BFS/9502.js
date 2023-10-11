const fs = require("fs");
const sample = `
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
`;
const inputs = sample.toString().trim().split("\n");
const num = Number(inputs[0]);
const cases = inputs.slice(1);

let currentCaseIndex = 0;
for (let i = 0; i < num; i++) {
  const numStore = Number(cases[currentCaseIndex]);
  let currentCase = cases
    .slice(currentCaseIndex + 1, currentCaseIndex + 3 + numStore)
    .map((e) => e.split(" ").map((e) => Number(e)));

  const stores = currentCase.slice(0, -1);
  const checked = stores.map((e) => 0);

  let flag = false;

  const dest = currentCase.slice(-1)[0];

  const q = [[...stores[0], 0]];
  checked[0] = 1;

  while (q.length) {
    const [x, y, index] = q.shift();

    if (Math.abs(x - dest[0]) + Math.abs(y - dest[1]) <= 1000) {
      flag = true;
      break;
    }

    stores.forEach((store, i) => {
      const dist = Math.abs(store[0] - x) + Math.abs(store[1] - y);
      if (dist <= 1000 && !checked[i]) {
        checked[i] = 1;
        q.push([...store, i]);
      }
    });
  }

  if (flag) {
    console.log("happy");
  } else {
    console.log("sad");
  }

  currentCaseIndex += 2 + numStore + 1;
}
