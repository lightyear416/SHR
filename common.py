#coding=utf-8
from __future__ import division
import numpy as np
import copy

#Judging the existence of node values for the original matrix
def check_node_hash(dic,order,hash):
    return [order.index(hash), count_node_hash(dic,hash), cal_cluster.sum_node(dic, order)] if hash in order else [-1, 0, cal_cluster.sum_node(dic, order)]

#The number of hash corresponding to statistics
def count_node_hash(dic,hash):
    return dic[hash][0]

#Find the existence of hash which is corresponding to the index of num_i
def check_node_index(dic,order,num_i):
    for key in dic:
        if num_i in dic[key][1]:
            return [order.index(key),key,count_node_hash(dic,key)]

#calculate distance between a and b by different methods
#&, | and ^ are AND, OR and XOR
#Except for string data in Hamming, the rest are vectors.
# Else is Chebyshev Distance
def cal_elements_dis(a,b,method):
    if method == 'Hamming2':
        return bin(int(a,2)^int(b,2)).count('1')
    if method == 'Hamming16':
        return bin(int(a,16)^int(b,16)).count('1')
    elif method == 'Consine':
        return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    elif method == 'Euclidean':
        return np.sqrt(np.sum(np.square(a-b)))
    elif method == 'Manhattan':
        return np.sum(np.abs(a-b))
    else:
        return np.max(np.abs(a-b))

#Decide whether to set a number to -1 according to th and oper
def revalue_distance(value,th,oper):
    if oper=='>=':
        return -1 if value>=th else value
    elif oper=='>':
        return -1 if value>th else value
    elif oper=='<=':
        return -1 if value<=th else value
    else:
        return -1 if value<th else value

#Processing the distance matrix mat, setting the -1 for the meaningless data in the me mode under the threshold th condition setting.
def redefine_mat_distance(mat,th,me='>='):
    if me=='>=':
        return map(lambda x:[[i,-1][i>=th] for i in x],mat)
    elif me=='>':
        return map(lambda x:[[i,-1][i>th] for i in x],mat)
    elif me=='<=':
        return map(lambda x:[[i,-1][i<=th] for i in x],mat)
    else:
        return map(lambda x:[[i,-1][i<th] for i in x],mat)

#
#Normalizing mat by column normalization. If When the diagonal coefficient is 0, this column does not need to be normalized.
#In order to retain the normalized matrix for further research, we use deep copy to copy.
def uniform_mat_col(mat):
    cmat = copy.deepcopy(mat)
    colsum=np.sum(cmat,axis=0)
    for j in range(0,len(cmat)):
        if cmat[j][j] != 0:
            for i in range(0,len(cmat)):
                cmat[i][j] = cmat[i][j]/colsum[j]
    return cmat

#sum column for all node model
def sum_node_mat_hor(en,j,dis_m,hl):
    sum = 0
    for i in range(0,en):
        if dis_m[i][j] != -1:
            if i!=j:
                sum = sum + hl - dis_m[i][j]
    return sum

#extend matrix with row vector and column vector
def extend_mat_rc(mat,newrow,newcol,cornerValue):
    return np.c_[np.r_[mat,[newrow]],np.r_[newcol,[cornerValue]]]

#delete a row and column by index where index is [r,c]
def remove_mat_rc(mat,index):
    mat = np.delete(mat,index[0],axis=0)
    mat = np.delete(mat,index[1],axis=1)
    return mat


