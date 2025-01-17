class Node {
  constructor(value, coord) {
    this.value = value;
    this.coord = coord;
    this.left = null;
    this.right = null;
  }
}

class Tree {
  constructor() {
    this.root = null;
  }

  preorder() {
    const path = [];
    const dfs = (current) => {
      if (!current) {
        return;
      }

      path.push(current.value);

      dfs(current.left);
      dfs(current.right);
    };

    dfs(this.root);

    return path;
  }

  postorder() {
    const path = [];
    const dfs = (current) => {
      if (!current) {
        return;
      }

      dfs(current.left);
      dfs(current.right);
      path.push(current.value);
    };

    dfs(this.root);

    return path;
  }

  add(node) {
    if (!this.root) {
      this.root = node;
      return;
    }

    let current = this.root;

    const [nx, ny] = node.coord;

    while (true) {
      const [cx, cy] = current.coord;

      // left
      if (nx < cx) {
        if (!current.left) {
          current.left = node;
          break;
        }

        current = current.left;
        continue;
      }

      // right
      if (nx > cx) {
        if (!current.right) {
          current.right = node;
          break;
        }

        current = current.right;
        continue;
      }
    }
  }
}

function solution(nodeinfos) {
  const answer = [];

  const mapped = nodeinfos.map((nodeinfo, i) => [...nodeinfo, i + 1]);

  mapped.sort((a, b) => {
    // y 를 기준으로 내림차순
    if (a[1] !== b[1]) {
      return b[1] - a[1];
    }

    // y 가 동일할 때, x 를 기준으로 오름차순
    return a[0] - b[0];
  });

  const tree = new Tree();

  mapped.forEach((nodeinfo) => {
    const node = new Node(nodeinfo[2], nodeinfo.slice(0, 2));
    tree.add(node);
  });

  answer.push(tree.preorder());
  answer.push(tree.postorder());

  return answer;
}
