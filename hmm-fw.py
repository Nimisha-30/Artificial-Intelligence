# HMM
# Forward Algorithm

H = {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2}
L = {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3}
transitionP = {('S', 'H'): 0.5, ('S', 'L'): 0.5, ('H', 'H'): 0.5,
               ('L', 'L'): 0.6, ('L', 'H'): 0.4, ('H', 'L'): 0.5}
seq = 'GGCA'
P = []

for i in seq:
    if len(P) == 0:
        p = [transitionP[('S', 'H')] * H[i], transitionP[('S', 'L')] * L[i]]
    else:
        p = []
        # H
        # (H -> H) + (L -> H)
        p.append(P[-1][0] * transitionP[('H', 'H')] * H[i] +
                 P[-1][1] * transitionP[('L', 'H')] * H[i])
        # L
        # (L -> L) + (H -> L)
        p.append(P[-1][1] * transitionP[('L', 'L')] * L[i] +
                 P[-1][0] * transitionP[('H', 'L')] * L[i])
    P.append(p)

print(P)
print()
print(P[-1][0] + P[-1][1])
