function solution(scores) {
  const wanho = scores[0];
  const sortedScores = scores.slice(1);
  sortedScores.sort((a, b) => b[0] + b[1] - (a[0] + a[1]));

  const candidates = [];

  for (let i = 0; i < sortedScores.length; i++) {
    const score = sortedScores[i];

    if (score[0] > wanho[0] && score[1] > wanho[1]) {
      return -1;
    }

    if (score[0] + score[1] <= wanho[0] + wanho[1]) {
      break;
    }

    let found = false;
    for (const candidate of candidates) {
      if (score[0] < candidate[0] && score[1] < candidate[1]) {
        found = true;
        break;
      }
    }

    if (!found) {
      candidates.push(score);
    }
  }

  return candidates.length + 1;
}
