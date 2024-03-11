import sys
input=sys.stdin.readline

dict = {
  'ADD':'00000',
  'ADDC':'00001',
  'SUB':'00010', 
  'SUBC':'00011',
  'MOV':'00100',  
  'MOVC':'00101', 
  'AND':'00110',  
  'ANDC':'00111', 
  'OR':'01000',  
  'ORC':'01001', 
  'NOT':'01010',  
  'MULT':'01100',  
  'MULTC':'01101', 
  'LSFTL':'01110',  
  'LSFTLC':'01111', 
  'LSFTR':'10000',  
  'LSFTRC':'10001', 
  'ASFTR':'10010',  
  'ASFTRC':'10011', 
  'RL':'10100',  
  'RLC':'10101', 
  'RR':'10110',  
  'RRC':'10111', 
}

n = int(input())
code = [list(input().split()) for _ in range(n)]

for i in code:
  op, rd, ra, s = i[0], i[1], i[2], i[3]

  op = dict[op]

  if op[4] == '0':
    s = format(int(s),'03b') + '0'
  elif op[4] == '1':
    s = format(int(s),'04b')

  if ra == '0':
    ra = '000'
  else:
    ra = format(int(ra),'03b')

  rd = format(int(rd),'03b')

  result = ''.join([op,'0',rd,ra,s])
  print(result)

