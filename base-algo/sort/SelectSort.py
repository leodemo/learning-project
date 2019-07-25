# coding: utf-8
#---------------------------------------  
#   project：选择排序
#   author：GuoLiang
#   date：2018-02-27
#   language：Python 3.6.1
#   desc：数组从小到大排序
#---------------------------------------
def merge_sort(arry):
	n = len(arry)
	if(n == 0 or n == 1):
		return arry
	for i in range(n):   # 外循环遍历N次,即交换N次（0 ~ N-1）
		min = i          # 最小元素的索引，初始为第i个
		for j in range(i+1, n): # 内循环遍历arry, 即比较(n-1, n-2,..., 1)次
			if (arry[j] < arry[min]):                      # 前一个和后一个数比较，如果前一个数大于后一个；比如第一轮遍历后，最后一个数字就是最大的数；
				min=j
		arry[min], arry[i] = arry[i], arry[min] 
	return arry

def 


if __name__ == '__main__':
	arry = [2,1,3,4,5]
	arry = [7,2,1,8,3,4,5]
	sortedArry = select_sort(arry)
	print(sortedArry)