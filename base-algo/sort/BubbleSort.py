# coding: utf-8
#---------------------------------------  
#   project：冒泡排序
#   author：GuoLiang
#   date：2018-02-27
#   language：Python 3.6.1
#   desc：数组从小到大排序
#---------------------------------------
def bubble_sort(arry):
	n = len(arry)
	if(n == 0 or n == 1):
		return arry
	for i in range(n):   # 外循环遍历N次,即交换N次（0 ~ N-1）
		for j in range(0, n-i-1): # 内循环遍历arry, 即比较(n-1, n-2,..., 1)次 （0 ~ N-1-1-i）
			if (arry[j] > arry[j+1]):                      # 前一个和后一个数比较，如果前一个数大于后一个；比如第一轮遍历后，最后一个数字就是最大的数；
				arry[j+1],arry[j] = arry[j], arry[j+1]  
	return arry

# 增加标识位，如果有一轮遍历没有进行交换数字的操作，说明当前已是有序数组
def bubble_sort_2(arry):
	n = len(arry)
	if(n == 0 or n == 1):
		return arry
	for i in range(n):
		flag = 1
		for j in range(0, n-i-1):
			if (arry[j] > arry[j+1]):
				arry[j+1],arry[j] = arry[j], arry[j+1]
				flag = 0
		if(flag):
			break
	return arry

# 记录最后一次的交换位置，该位置之后的数组都是有序的，则不需要遍历
def bubble_sort_3(arry):
	n = len(arry)
	if (n == 0 or n == 1):
		return arry
	k = n-1    #k用来记录最后一次的交换位置，初始为数组的最后一个数字的位置
	for i in range(n): #交换N次 （0~N-1）
		flag = 1 
		for j in range(0, k): #比较 (N-1-1, N-3, ... , 0)
			# print (i, j, k) 
			if (arry[j] > arry[j+1]):
				arry[j+1],arry[j] = arry[j], arry[j+1]
				flag = 0
				k = j
		if(flag):
			break
	return arry

if __name__ == '__main__':
	arry = [2,1,3,4,5]
	arry = [7,2,1,8,3,4,5]
	sortedArry = bubble_sort_3(arry)
	print(sortedArry)