#coding=utf-8
from __future__ import division
#calculate matrix A
import numpy as np
import cal_cluster
import cal_dis_mat
import common

#calculate all date for all node model
def cal_node_A(list,dis_m,hl):
    #number of node is en
    en = len(list)
    A = np.zeros((en,en))
    for j in range(0,en):
        Amother = cal_dis_mat.sum_node_ham_dis_hor(en,j,dis_m,hl)
        for i in range(0,en):
            if dis_m[i][j]==-1 or i==j:
                A[i][j] = 0
            else:
                A[i][j] = hl-dis_m[i][j]/Amother
    return A

#calculate A with damping coefficent
def cal_node_A_damping(A,damping):
    return damping*A + (1-damping)/A.shape[0]*np.ones((A.shape[0],A.shape[0]))

