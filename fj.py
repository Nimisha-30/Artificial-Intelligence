START = 'ab-uv'
GOAL = 'uv-ab'
right = 'ab'
left = 'uv'


def swap_positions(s, i, j):
    if i < j:
      return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]


def apply_move(s, f):
    x = s.index(f)
    if f in right:
        if x+1 < len(s) and s[x+1] == '-':
            return swap_positions(s, x, x+1)
        if x+2 < len(s) and s[x+1] != '-' and s[x+2] == '-':
            return swap_positions(s, x, x+2)
    if f in left:
        if x-1 >= 0 and s[x-1] == '-':
            return swap_positions(s, x-1, x)
        if x-2 >= 0 and s[x-1] != '-' and s[x-2] == '-':
            return swap_positions(s, x-2, x)


def next_moves(s):
    i = s.index('-')
    ms = []
    if i-1 >= 0 and s[i-1] in right:
        ms.append(s[i-1])
    if i-2 >= 0 and s[i-2] in right:
        ms.append(s[i-2])
    if i+1 < len(s) and s[i+1] in left:
        ms.append(s[i+1])
    if i+2 < len(s) and s[i+2] in left:
        ms.append(s[i+2])
    return ms


def search(s):
    work = set([("", s)])
    states = 0
    while work:
        path, cur = work.pop()
        states += 1
        print(cur)
        for k in next_moves(cur):
            succ = apply_move(cur, k)
            work.add((path+k, succ))
            print(path+k, " --> ", print(succ))


search(START)
