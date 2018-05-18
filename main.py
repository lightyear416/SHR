#coding=utf-8
from __future__ import division
# this file use to calculate semantic hash rank
# we maintain a table about order and ID where name_list is corresponding to order in the dic

import numpy as np
import math
import pandas as pd
import xlwt
import cal_SHR

#Hamming distance
hl = 48
#Restricted Hamming distance
rhl = 24
#Restriction operation
oper = '>='
#Calculate method for distance
dis_method = 'Hamming16'
#Whether use restriction operation
isRestrict = True
#precision value
prec = math.pow(10,-8)
#damping coefficient
damping = 0.85
#open the file for ID and hash
name_list = np.loadtxt(fname="filename.txt",dtype="string")
hash_list = np.loadtxt(fname="filehash.txt",dtype="string")
if len(name_list)!=len(hash_list):
    print "ID and name are not match!"
else:
    #According to hash_list，we calculate R by SHR
    [u_R,u_A,u_dis_m,u_iter_num] = cal_SHR.cal_node_Rank(hash_list,hl,rhl,oper=oper,dis_method=dis_method,isRestrict=isRestrict,damping=damping,prec=prec)

    print u_R

    ResultOUT = pd.DataFrame(u_R)
    ResultPATH = r"nodeR2.xls"
    ResultOUT.to_excel(ResultPATH)