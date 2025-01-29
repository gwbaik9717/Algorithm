function solution(N, number) {
  const dp = Array.from({ length: 9 }, () => new Set());

  for (let i = 1; i < dp.length; i++) {
    dp[i].add(Number(String(N).repeat(i)));

    for (let j = 1; j < i; j++) {
      for (const left of dp[j]) {
        for (const right of dp[i - j]) {
          dp[i].add(left + right);
          dp[i].add(left - right);
          dp[i].add(left * right);
          dp[i].add(Math.floor(left / right));
        }
      }
    }

    if (dp[i].has(number)) {
      return i;
    }
  }

  return -1;
}
