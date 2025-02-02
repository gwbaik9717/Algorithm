function solution(n, m, x, y, r, c, k) {
  const manhattan = Math.abs(r - x) + Math.abs(c - y);

  if (k < manhattan) {
    return "impossible";
  }

  if ((k - manhattan) % 2 !== 0) {
    return "impossible";
  }

  let down = Math.max(r - x, 0);
  let left = Math.max(y - c, 0);
  let right = Math.max(c - y, 0);
  let up = Math.max(x - r, 0);

  let pair = Math.floor((k - manhattan) / 2);
  let answer = "";

  let cx = x;
  let cy = y;

  for (let i = 0; i < k; i++) {
    // Down
    if (down || pair) {
      if (cx < n) {
        if (down) {
          down -= 1;
        } else if (pair) {
          up += 1;
          pair -= 1;
        }

        answer += "d";
        cx += 1;
        continue;
      }
    }

    // Left
    if (left || pair) {
      if (cy > 1) {
        if (left) {
          left -= 1;
        } else if (pair) {
          right += 1;
          pair -= 1;
        }

        answer += "l";
        cy -= 1;
        continue;
      }
    }

    // Right
    if (right || pair) {
      if (cy < m) {
        if (right) {
          right -= 1;
        } else if (pair) {
          left += 1;
          pair -= 1;
        }

        answer += "r";
        cy += 1;
        continue;
      }
    }

    // Up
    if (up || pair) {
      if (cx > 1) {
        if (up) {
          up -= 1;
        } else if (pair) {
          down += 1;
          pair -= 1;
        }

        answer += "u";
        cx -= 1;
        continue;
      }
    }
  }

  return answer;
}
