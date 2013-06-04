import random

f = open('randomInts.txt','w')
for i in range(0,10000):
  a = random.randint(0,1000000)
  f.write(str(a))
  f.write(',')
  if (i % 10 == 0):
    f.write('\n');
f.close()
