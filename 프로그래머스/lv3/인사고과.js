function solution(scores) {
  let answer = 0;
  const wanho = scores[0];
  const sortedScores = scores.slice();
  sortedScores.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]));

  let maxValue = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < sortedScores.length; i++) {
    const score = sortedScores[i];

    if (score[1] >= maxValue) {
      maxValue = score[1];

      if (score[0] + score[1] > wanho[0] + wanho[1]) {
        answer++;
      }

      continue;
    }

    if (wanho[0] === score[0] && wanho[1] === score[1]) {
      return -1;
    }
  }

  return answer + 1;
}
