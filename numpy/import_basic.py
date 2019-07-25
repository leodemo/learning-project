#encoding:utf-8
import numpy as np
import imp
basic_var=imp.load_source('basic_var','F:\\workspace\\MachineLeaning\\learn\\python\\basic\\basic_var.py')
import basic_var

# a = basic_var.a32
# a1 = np.random.rand(3,2) # randn 
# print (a1)

# a1 = (a1 < 0.5)
# print (a1)

# a = a * a1
# print (a)

# a1 = np.random.randn(3,2)
# print (a1)


c=np.array([[[0, 1, 2,3], 
               [4, 5, 6,7]],
               [[1, 2, 3,4],
                [5,6,7,8]]])

# c=np.array([[0, 1], 
#                [4, 5],
#                [1, 2],
#                 [5,6]])

print (c.shape)
print (c.sum(axis=0).shape)
print (c.sum(axis=1).shape) 
print (c.sum(axis=2).shape)   