// TC: O(n)
// SC: O(1)

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let i = 0;
  let j = 1;

  let answer = 0;

  while (j < prices.length) {
    if (prices[i] > prices[j]) {
      i = j;
    } else {
      answer = Math.max(answer, prices[j] - prices[i]);
    }

    j++;
  }

  return answer;
};
