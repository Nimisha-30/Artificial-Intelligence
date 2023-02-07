from collections import deque

def reachTarget(a, b, target):
  m={}
  isSolvable=True
  path=[]
  q=deque()
  q.append([0, 0])
  while len(q)>0:
    x=q.popleft()
    if (x[0], x[1]) in m:
      continue
    if x[0]>a or x[1]>b or x[0]<0 or x[1]<0:
      continue
    path.append([x[0], x[1]])
    m[(x[0], x[1])]=1
    if x[0]==target or x[1]==target:
      isSolvable=True
      if x[0]==target and x[1]!=target:
        path.append([x[0], 0])
      if x[0]!=target and x[1]==target:
        path.append([0, x[1]])
      print(path)
      break
    q.append([x[0], a])
    q.append([b, x[1]])
    n=max(a, b)
    for i in range(n+1):
      c=x[0]+i
      d=x[1]-i
      if c==a or (d==0 and d>=0):
        q.append([c, d])
      c=x[0]-i
      d=x[1]+i
      if d==b or (c==0 and c>=0):
        q.append([c, d])
    q.append([a, 0])
    q.append([0, b])
  if not(isSolvable):
    print("No solution available")

reachTarget(3, 4, 2)