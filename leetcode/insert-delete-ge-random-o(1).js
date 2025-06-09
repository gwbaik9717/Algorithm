// TC: O(1)
// SC: O(n)

var RandomizedSet = function () {
  this.map = new Map();
  this.arr = new Array();
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function (val) {
  if (this.map.has(val)) {
    return false;
  }

  this.arr.push(val);
  this.map.set(val, this.arr.length - 1);

  return true;
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function (val) {
  if (!this.map.has(val)) {
    return false;
  }

  const index = this.map.get(val);
  this.arr[index] = this.arr[this.arr.length - 1];
  this.map.set(this.arr[this.arr.length - 1], index);
  this.map.delete(val);
  this.arr.splice(this.arr.length - 1, 1);

  return true;
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function () {
  const index = Math.floor(Math.random() * this.arr.length);
  return this.arr[index];
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
