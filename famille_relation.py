# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:36:20 2020

@author: marc-pc-2
"""


def is_reflexive(tmp_lst, max_point):
    total_egual     = list(filter(lambda x: x[0] == x[1], tmp_lst))
    # si le nombre de pair est pareil et égal le nombre
    if len(total_egual) == max_point:
        print('Cette relation est reflexive')
    if len(total_egual) == 0:
        print('Cette relation est irreflexive')
   
def is_sysmetrie(tmp_lst):
    total_pair      = len(tmp_lst)
    total_sysmetri  = 0
    total_sys_equal = 0
    for item in tmp_lst:
        tmp = list(filter(lambda x: item[1] == x[0] and item[0] == x[1], tmp_lst))
        if len(tmp) >= 1:
            total_sysmetri += 1
            if item[0] == item[1]:
                total_sys_equal += 1
    if total_pair == total_sysmetri:
        print('Cette relation est sysmetrique')
    if total_sysmetri == 0 and total_pair > 0:
        print('Cette relation est asysmetrique')
    if total_sysmetri == total_sys_equal:
        print('Cette relation est antisysmetrique')
        
def is_transitif(tmp_lst):
    total_transitive = 0
    total_double = 0
    for item in tmp_lst:
        relation1 = list(filter(lambda x: item[1] == x[0], tmp_lst))
        if len(relation1) > 0:
            for pair in relation1:
                total_double += 1
                relation2 = list(filter(lambda x: item[0] == x[0] and pair[1] == x[1], tmp_lst))
                if len(relation2) > 0:
                    total_transitive += 1
#                    print('Relation transitive {}, {}, {}'.format(item, pair, relation2))
#                else:
#                    print('Relation transitive {}, {}'.format(item, pair))
    if total_double == total_transitive:
        print('Cette relation est transitive ({} pairs)'.format(total_transitive))



#max_point = 4
#pairs = [[1, 2], [2, 3], [3, 4], [4, 1]]
#pairs = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [3, 1], [4, 1]]

max_point = 15
pairs = []

for x in range(max_point):
    for y in range(max_point):
        if x + 1 == y:
            pairs.append([x, y])


is_reflexive(pairs, max_point)
is_sysmetrie(pairs)
is_transitif(pairs)


