//2024-2-28
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, ...input] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let dp = [1, 2, 4, 7];

input.forEach((e) => {
  for (let i = dp.length; i < e; i++) {
    const a = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009;
    dp.push(a);
  }
  console.log(dp[e - 1]);
});
