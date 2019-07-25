# coding: utf-8
#---------------------------------------  
#   project：希尔排序 基于插入排序
#   author：GuoLiang
#   date：2018-02-27
#   language：Python 3.6.1
#   desc：数组从小到大排序
#---------------------------------------
def shell_sort(arry):
	n = len(arry)
	h = 1
	while (h < n/3): #1, 4, 13, 40
		h = 3*h + 1  #初始步长 
	while (h >= 1):  
		for i in range(h, n): #每一列进行插入排序
			j = i
			while (j >=h and arry[j] < arry[j-h]):
				arry[j], arry[j-h] = arry[j-h], arry[j]
				j -= h
		h = round(h/3)
		# print (h)
	return arry

def shell_sort_2(arry):
	n = len(arry)
	h = round(n/3)    
	while (h > 0):
		for i in range(h, n):  #每一列进行插入排序
			tmp = arry[i]
			j = i 
			while (j >=h and arry[j] < arry[j-h]):
				arry[j] = arry[j-h]
				j -= h
			arry[j] = tmp
		h = round(h/3)
		# print (h)
	return arry
	




if __name__ == '__main__':
	arry = [2,1,3,4,5]
	arry = [7,2,1,8,3,4,5]
	sortedArry = shell_sort_2(arry)
	print(sortedArry)