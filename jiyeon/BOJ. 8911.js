const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();
const [tc, ...code] = input.split("\n");

let testcase = Number(tc);
const opcode = [
  "ADD",
  "SUB",
  "MOV",
  "AND",
  "OR",
  "NOT",
  "MULT",
  "LSFTL",
  "LSFTR",
  "ASFTR",
  "RL",
  "RR",
];
const sixteen = [
  "0000",
  "0001",
  "0010",
  "0011",
  "0100",
  "0101",
  "0110",
  "0111",
  "1000",
  "1001",
  "1010",
  "1011",
  "1100",
  "1101",
  "1110",
  "1111",
];
const eight = ["000", "001", "010", "011", "100", "101", "110", "111"];

for (let i = 0; i < testcase; i++) {
  let result = "";
  let [assembly, rd, ra, rbORc] = code[i].split(" ");
  if (assembly.endsWith("C")) {
    result += sixteen[assembly.slice(0, assembly.length - 1).findIndex(opcode)];
    result += "10";
  } else {
    result += sixteen[assembly.findIndex(opcode)];
    result += "00";
  }
  result += eight[Number(rd)];
  result += eight[Number(ra)];
  if (assembly.endsWith("C")) {
    result += sixteen[Number(rbORc)];
  } else {
    result += eight[Number(rbORc)];
    result += "0";
  }
  console.log(result);
}
