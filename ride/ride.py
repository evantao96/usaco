"""
PROG: ride
LANG: PYTHON3
"""

fin = open('ride.in', 'r')
comet = fin.readline().strip()
line = fin.readline().strip()
fin.close()

letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
prod_c = 1
for c in comet: 
	prod_c = prod_c * letters[c]

prod_l = 1
for l in line:
	prod_l = prod_l * letters[l]

if prod_c % 47 == prod_l % 47: 
	ans = 'GO'
else: 
	ans = 'STAY'

fout = open('ride.out', 'w')
fout.write(ans + '\n')
fout.close()
