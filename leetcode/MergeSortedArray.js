// TC: O(n + m)
// SC: O(m)

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  if (n === 0) {
    return;
  }

  const cloned = nums1.slice(0, m);

  let i = 0;
  let j = 0;

  for (let k = 0; k < m + n; k++) {
    if (j >= n || cloned[i] < nums2[j]) {
      nums1[k] = cloned[i];
      i++;
    } else {
      nums1[k] = nums2[j];
      j++;
    }
  }
};
