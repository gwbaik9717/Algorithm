// TC: O(nlogn)
// SC: O(1)

/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function (citations) {
  let answer = 0;

  citations.sort((a, b) => b - a);

  for (let i = 0; i < citations.length; i++) {
    const val = Math.min(i + 1, citations[i]);

    if (val <= answer) {
      break;
    }

    answer = val;
  }

  return answer;
};
