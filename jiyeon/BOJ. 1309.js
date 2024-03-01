//2024-3-1

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();
const n = Number(input);

dp = [1];
dp.push(3);
//console.log(dp);
for (i = 0; i < n - 1; i++) {
  a = (dp[i] + dp[i + 1] * 2) % 9901;
  dp.push(a);
}
console.log(dp[n]);
