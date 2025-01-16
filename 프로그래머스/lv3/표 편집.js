class LinkedList {
  constructor(n, k) {
    this.answer = Array.from({ length: n }, () => "O");

    // history stack of deleted items
    this.deleted = [];

    this.list = Array.from({ length: n }, (_, i) => new Item(i));

    // init list
    for (let i = 1; i < n; i++) {
      const currItem = this.list[i];
      const prevItem = this.list[i - 1];
      currItem.prev = prevItem;
      prevItem.next = currItem;
    }

    this.pointer = this.list[k];
  }

  move(dir, dist) {
    let current = this.pointer;

    for (let i = 0; i < dist; i++) {
      if (dir === "D") {
        current = current.next;
      } else {
        current = current.prev;
      }
    }

    this.pointer = current;
  }

  delete() {
    this.deleted.push(this.pointer);
    this.answer[this.pointer.value] = "X";

    this.list[this.pointer.value] = null;

    if (this.pointer.prev) {
      this.pointer.prev.next = this.pointer.next;
    }

    if (this.pointer.next) {
      this.pointer.next.prev = this.pointer.prev;
      this.pointer = this.pointer.next;
      return;
    }

    this.pointer = this.pointer.prev;
  }

  undo() {
    const restored = this.deleted.pop();
    this.answer[restored.value] = "O";

    if (restored.prev) {
      const prevIndex = restored.prev.value;
      this.list[prevIndex].next = restored;
    }

    if (restored.next) {
      const nextIndex = restored.next.value;
      this.list[nextIndex].prev = restored;
    }

    this.list[restored.value] = restored;
  }
}

class Item {
  constructor(value) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

function solution(n, k, cmds) {
  const linkedList = new LinkedList(n, k);

  for (const cmd of cmds) {
    const [type, x] = cmd.split(" ");

    if (type === "U" || type === "D") {
      linkedList.move(type, Number(x));
      continue;
    }

    if (type === "C") {
      linkedList.delete();
      continue;
    }

    linkedList.undo();
  }

  return linkedList.answer.join("");
}
