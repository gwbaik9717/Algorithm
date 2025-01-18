class Node {
  constructor(value) {
    this.value = value;
    this.visited = false;
  }
}

function solution(infos, edges) {
  let answer = 1;
  const tree = infos.map((info) => new Node(info));

  const dfs = (wolves, sheeps) => {
    if (wolves >= sheeps) {
      return;
    }

    for (const [parent, child] of edges) {
      if (tree[parent].visited && !tree[child].visited) {
        tree[child].visited = true;

        if (tree[child].value === 0) {
          dfs(wolves, sheeps + 1);
          answer = Math.max(answer, sheeps + 1);
        } else {
          dfs(wolves + 1, sheeps);
        }

        tree[child].visited = false;
      }
    }
  };

  tree[0].visited = true;
  dfs(0, 1);

  return answer;
}
