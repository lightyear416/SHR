#coding=utf-8
from __future__ import division
#calculate rank by iteration
import copy
import numpy as np
import common

def num_iterR(A,R,num):
    while num>0:
        R = A*R
        num = num - 1
        print R

#A is Matrix，R is initial vector，c is precison of convergency
def iterR(A,R,c):
    #tempR = copy.deepcopy(R)
    iter_num = 0
    while True:
        if common.cal_elements_dis(R,A*R,method='Manhattan') > c:
            R = A*R
            iter_num = iter_num + 1
        else:
            return [R,iter_num]

def restore_node_R(R,org_len,cluster_len):
    return R*org_len/cluster_len


