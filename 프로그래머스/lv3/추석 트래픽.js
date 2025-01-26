const convertTimeToTimestamp = (time) => {
    const [hh, mm, ss] = time.split(":").map(Number);
    return ss * 1000 + mm * 60 * 1000 + hh * 60 * 60 * 1000;
};

const convertDurationToTimestamp = (duration) => {
    return Number(duration.slice(0, -1)) * 1000;
};

function solution(lines) {
    const timestamps = [];

    // 로그의 시작 시간과 종료 시간을 계산
    lines.forEach(line => {
        const [time, duration] = line.split(" ").slice(1);
        const end = convertTimeToTimestamp(time);
        const start = end - convertDurationToTimestamp(duration) + 1;
        timestamps.push([start, end]);
    });

    let maxCount = 0;

    // 종료 시간을 기준으로 1초 범위를 계산
    timestamps.forEach(([start, end]) => {
        const startRange = end;          // 1초 범위 시작
        const endRange = end + 1000;    // 1초 범위 끝

        let count = 0;

        // 1초 범위 내에 겹치는 로그를 모두 확인
        timestamps.forEach(([logStart, logEnd]) => {
            if (logStart < endRange && logEnd >= startRange) {
                count++;
            }
        });

        maxCount = Math.max(maxCount, count);
    });

    return maxCount;
}