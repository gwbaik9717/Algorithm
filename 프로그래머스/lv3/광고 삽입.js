const convertToTimestamp = (time) => {
  const [hh, mm, ss] = time.split(":").map(Number);
  return hh * 3600 + mm * 60 + ss;
};

const convertToHHMMSS = (timestamp) => {
  const hh = String(Math.floor(timestamp / 3600));
  const mm = String(Math.floor((timestamp % 3600) / 60));
  const ss = String(Math.floor(timestamp % 60));

  return `${hh.padStart(2, "0")}:${mm.padStart(2, "0")}:${ss.padStart(2, "0")}`;
};

function solution(play_time, adv_time, logs) {
  const at = convertToTimestamp(adv_time);
  const pt = convertToTimestamp(play_time);
  const times = Array.from({ length: pt + 1 }, () => 0);

  logs.forEach((log) => {
    const [start, end] = log.split("-");

    const startTimestamp = convertToTimestamp(start);
    const endTimestamp = convertToTimestamp(end);

    times[startTimestamp]++;
    times[endTimestamp]--;
  });

  for (let i = 1; i <= pt; i++) {
    times[i] += times[i - 1];
  }

  for (let i = 1; i <= pt; i++) {
    times[i] += times[i - 1];
  }

  let sum = times[at - 1];
  let idx = 0;

  for (let i = at; i <= pt; i++) {
    if (sum < times[i] - times[i - at]) {
      sum = times[i] - times[i - at];
      idx = i - at + 1;
    }
  }

  return convertToHHMMSS(idx);
}
