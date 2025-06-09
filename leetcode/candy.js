// TC: O(n)
// SC: O(n)

/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function (ratings) {
  const result = Array.from({ length: ratings.length }, () => 1);

  for (let i = 1; i < ratings.length; i++) {
    if (ratings[i] > ratings[i - 1]) {
      result[i] = result[i - 1] + 1;
      continue;
    }
  }

  for (let i = ratings.length - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1] && result[i] <= result[i + 1]) {
      result[i] = result[i + 1] + 1;
      continue;
    }
  }

  return result.reduce((a, c) => a + c, 0);
};
