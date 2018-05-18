#coding=utf-8
#construct distance matrix with hash code
import numpy as np
import common

# Calculation of upper triangular matrix for digit
def cal_dis_mat(list,method,th,oper,isRestrict=False):
    dig_len = len(list)
    dis_matrix = np.zeros((dig_len,dig_len))
    for indexR,itemR in enumerate(list):
        cursor = indexR+1
        dis_matrix[indexR][indexR] = 0
        while cursor<dig_len:
            dis_matrix[indexR][cursor] =  common.cal_elements_dis(itemR,list[cursor],method=method)
            if isRestrict == True:
                dis_matrix[indexR][cursor] =  common.revalue_distance(dis_matrix[indexR][cursor],th,oper)
            dis_matrix[cursor][indexR] = dis_matrix[indexR][cursor]
            cursor = cursor + 1
    return dis_matrix

# update distance matrix (add one row or column at last of matrix)
def update_dis_mat_add(order,hash,org_dis_m,th,oper,dis_method,isRestrict):
    en = len(order)
    A_line = np.zeros(en)
    for i in range(0,en):
        A_line[i] = common.cal_elements_dis(order[i],hash,dis_method)
        if isRestrict == True:
            A_line[i] = common.revalue_distance(A_line[i],th,oper)
    return common.extend_mat_rc(org_dis_m,A_line,A_line,0)

# update distance matrix (del one row and column by index)
def update_dis_mat_del(dis_m,index_r,index_c):
    return common.remove_mat_rc(dis_m,[index_r,index_c])

#sum column value according to j for all node model
def sum_node_ham_dis_hor(en,j,dis_m,hl):
    return common.sum_node_mat_hor(en,j,dis_m,hl)
