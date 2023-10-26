const fs = require("fs");
const sample = `
6
573 33283 5572 346 906 567
5
5 6
1 3
2 2
1 6
3 6
`;

const inputs = sample.toString().trim().split("\n");
const musics = inputs[1].split(" ").map((e) => Number(e));
const tcs = inputs.slice(3).map((e) => e.split(" ").map((e) => Number(e)));
const n = musics.length;
const psum = Array.from({ length: n }, () => 0);

for (let i = 0; i < n; i++) {
  psum[i] = (psum[i - 1] || 0) + (musics[i] > musics[i + 1] ? 1 : 0);
}

let answer = [];
for (let tc of tcs) {
  const [s, e] = tc;

  answer.push((psum[e - 2] || 0) - (psum[s - 2] || 0));
}

console.log(answer.join("\n"));
