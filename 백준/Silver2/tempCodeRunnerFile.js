for (let i = 1; i <= n + 2; i++) {
  arr[i] += arr[i - 1];
}

for (const tc of tcs) {
  const [s, e] = tc;

  console.log(e - s + 1 - (arr[e] - arr[s - 1]));
}
