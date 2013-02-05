#!/usr/bin/python2.7

from subprocess import Popen, PIPE

#return a list of processes consuming >= mincpu % of CPU
def get_top(mincpu):
  p1 = Popen("ps -eo pid,pcpu,comm".split(), stdout=PIPE)
  p2 = Popen("grep -v 0.0".split(), stdin=p1.stdout, stdout=PIPE)
  p1.stdout.close()
  outputs = p2.stdout.readline() #skip labels
  outputs = p2.stdout.readlines()
  print(outputs)
  processes = []
  for line in outputs:
    processes.append(tuple(line.strip().split()))
  processes.sort(key=lambda tup:tup[1], reverse=True)
  return processes

if __name__ == "__main__":
  p = get_top(0.2)
  if p:
    for i in p:
      print(i)

