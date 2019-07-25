#encoding:utf-8
import numpy as np 
import imp
basic_var=imp.load_source('basic_var','F:\\workspace\\MachineLeaning\\learn\\python\\basic\\basic_var.py')
import basic_var
# a = [[2,3], [4,3], [1,2]]
# a = basic_var.a32

print ("1. np.linalg.norm")
a = basic_var.a13
print ("   a matric is: " + str(a))
b = np.linalg.norm(a) 
print ("   default norm: " + str(b))

b = np.linalg.norm(a, ord=2) #L2正则化范式 	二范数
print ("   2 norm: " + str(b))

b = np.linalg.norm(a, ord=1)  #	一范数
print ("   1 norm: " + str(b))

b = np.linalg.norm(a, ord=np.inf)  #无穷范数
print ("   inf norm: " + str(b))


print ("2. np.power")
beta=3
t=2
print ("   beta is %s, power is %s. result is %s"%(str(beta), str(t), str(np.power(beta, t)))) # 指数



print ("2. np.random.rand & randn")
rand_matrix = np.random.rand(3,2)  # rand 生成均匀分布的伪随机数。分布在（0~1）之间
print ("   rand matrix:" + str(rand_matrix))

randn_matrix = np.random.randn(3,2)  # randn 生成标准正态分布的伪随机数（均值为0，方差为1）
print ("   rand norm matrix:"  + str(randn_matrix))