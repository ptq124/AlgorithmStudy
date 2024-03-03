const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();
const [n, ...wine] = input.split("\n").map(Number);
//console.log(n, wine);

let dp = Array(n + 1).fill(0);

dp[1] = wine[0];
if (n >= 2) {
  dp[2] = wine[1] + wine[0];
}
if (n >= 3) {
  dp[3] = Math.max(wine[1] + wine[2], wine[2] + wine[0], wine[0] + wine[1]);
}

for (let i = 4; i < n + 1; i++) {
  dp[i] = Math.max(
    wine[i - 1] + dp[i - 2],
    wine[i - 1] + dp[i - 3] + wine[i - 2],
    dp[i - 1]
  );
  console.log(wine[i - 1], dp);
}
console.log(dp[n]);
