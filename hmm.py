# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:45:47 2023

@author: niran
"""
import copy
import math

H = {
    'A': 0.2,
    'C': 0.3,
    'G': 0.3,
    'T': 0.2
}

L = {
    'A': 0.3,
    'C': 0.2,
    'G': 0.2,
    'T': 0.3
}

HMM = {
    'start': [[0.5, H], [0.5, L]],
    'H': [[0.5, H], [0.5, L]],
    'L': [[0.4, H], [0.6, L]]
}

input_sequence = ['G', 'G', 'C', 'A', 'C', 'T', 'G', 'A', 'A']
h_list = []
l_list = []

counter = 0

print(HMM['H'][0][0])

for gene in input_sequence:
    if counter == 0:
        temp = HMM['start']
        ans_h = temp[0][0]*H[gene]
        ans_l = temp[1][0]*L[gene]
        h_list.append(ans_h)
        l_list.append(ans_l)
        counter += 1
    else:

        ans_h = H[gene]*max(h_list[counter-1]*HMM['H'][0][0],
                            l_list[counter-1]*HMM['L'][0][0])
        ans_l = L[gene]*max(h_list[counter-1]*HMM['H'][1][0],
                            l_list[counter-1]*HMM['L'][1][0])

        h_list.append(ans_h)
        l_list.append(ans_l)
        counter += 1


print(h_list)
print(l_list)

prob_seq = []
sequences = []
alt = []
cnt = 0
for i in range(len(h_list)):
    if l_list[i] > h_list[i]:
        prob_seq.append('L')
    elif math.isclose(h_list[i], l_list[i]):
        alt.append(i)
        prob_seq.append('H')
    elif h_list[i] > l_list[i]:
        prob_seq.append('H')

if len(alt) != 0:
    temp = copy.deepcopy(prob_seq)
    for i in alt:
        temp[i] = 'L'
        if temp not in sequences:
            sequences.append(copy.deepcopy(temp))
        temp[i] = 'H'
    temp1 = copy.deepcopy(prob_seq)
    for i in alt:
        temp1[i] = 'L'
    if temp1 not in sequences:
        sequences.append(temp1)

print("The most probable sequence is:")
print(prob_seq)
print(sequences)
