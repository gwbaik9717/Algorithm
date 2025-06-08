// TC: O(n)
// SC: O(1)

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const products = Array.from({ length: nums.length }, () => 1);

  // left to right
  for (let i = 1; i < nums.length; i++) {
    products[i] = products[i - 1] * nums[i - 1];
  }

  let acc = 1;

  // right to left
  for (let i = nums.length - 2; i >= 0; i--) {
    acc *= nums[i + 1];
    products[i] *= acc;
  }

  return products;
};
