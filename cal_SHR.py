#coding=utf-8
from __future__ import division
#Enter of rank

import numpy as np
import math
import cal_A
import cal_Rank
import cal_dis_mat

#Enter of rank for all node model
def rank_node(A,hash_list,damping,prec):
    if damping != 1:
        damping_A = cal_A.cal_node_A_damping(A,damping)
        [R,iter_num] = cal_Rank.iterR(np.mat(damping_A),np.mat(np.ones(len(hash_list))).T,prec)
    else:
        [R,iter_num] = cal_Rank.iterR(np.mat(A),np.mat(np.ones(len(hash_list))).T,prec)
    return [R,iter_num]

#calculate rank for all node model
def cal_node_Rank(hash_list,hl,rhl,oper='>=',dis_method='Hamming2',isRestrict=True,damping=1,prec=math.pow(10,-8)):
    #calculate distance matrix
    dis_m = cal_dis_mat.cal_dis_mat(hash_list,dis_method,rhl,oper,isRestrict=isRestrict)
    #calculate A matrix
    A = cal_A.cal_node_A(hash_list,dis_m,hl)
    #Test for 6 times results of A
    #cal_Rank.num_iterR(np.mat(A),np.mat(np.ones(en)).T,6)
    #calculate A with damping coefficient
    [R,iter_num] = rank_node(A,hash_list,damping,prec)
    return [R,A,dis_m,iter_num]

