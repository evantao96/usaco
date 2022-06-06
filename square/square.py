"""
PROBLEM: http://www.usaco.org/index.php?page=viewproblem2&cpid=663#
PROG: square
LANG: PYTHON3
"""

fin = open('square.in', 'r')
l1 = fin.readline()
l2 = fin.readline()
fin.close()

r1x1, r1y1, r1x2, r1y2 = l1.split()
r2x1, r2y1, r2x2, r2y2 = l2.split()

r1x1 = int(r1x1)
r1y1 = int(r1y1)
r1x2 = int(r1x2)
r1y2 = int(r1y2)
r2x1 = int(r2x1)
r2y1 = int(r2y1)
r2x2 = int(r2x2)
r2y2 = int(r2y2)

dimx = max(r1x1, r1x2, r2x1, r2x2) - min(r1x1, r1x2, r2x1, r2x2) 
dimy = max(r1y1, r1y2, r2y1, r2y2) - min(r1y1, r1y2, r2y1, r2y2)
ans = max(dimx, dimy) ** 2

fout = open('square.out', 'w')
fout.write(str(ans) + '\n')
fout.close()
