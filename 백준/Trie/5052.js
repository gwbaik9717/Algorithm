const fs = require("fs");
const sample = `
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
`;

class Node {
  constructor(value = "") {
    this.value = value;
    this.next = new Map();
    this.cnt = 0;
  }
}

class Trie {
  constructor() {
    this.head = new Node();
  }

  add(str) {
    let current = this.head;

    for (let char of str) {
      if (!current.next.has(char)) {
        current.next.set(char, new Node(current.value + char));
      }

      current = current.next.get(char);
      current.cnt++;
    }
  }

  find(str) {
    let current = this.head;

    for (let char of str) {
      current = current.next.get(char);
      if (current.cnt === 1) {
        return false;
      }
    }

    return true;
  }
}

const inputs = sample.toString().trim().split("\n");
const t = Number(inputs[0]);
let j = 1;
const ans = [];

for (let i = 0; i < t; i++) {
  let n = Number(inputs[j]);

  const tels = inputs.slice(j + 1, j + 1 + n);
  const trie = new Trie();

  for (let tel of tels) {
    trie.add(tel);
  }

  let flag = false;

  for (let tel of tels) {
    if (trie.find(tel)) {
      flag = true;
      ans.push("NO");
      break;
    }
  }

  if (!flag) {
    ans.push("YES");
  }

  j += n + 1;
}

console.log(ans.join("\n"));
