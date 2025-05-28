// TC: O(n)
// SC: O(1)

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  let maxValue = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (i > maxValue) {
      return false;
    }

    maxValue = Math.max(maxValue, i + nums[i]);
  }

  return true;
};
