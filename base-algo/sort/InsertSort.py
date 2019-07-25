# coding: utf-8
#---------------------------------------  
#   project：插入排序
#   author：GuoLiang
#   date：2018-02-27
#   language：Python 3.6.1
#   desc：数组从小到大排序
#---------------------------------------
def insert_sort(arry):
	n = len(arry)
	if(n == 0 or n == 1):
		return arry
	for i in range(1, n):   # 外循环遍历N-1次,即交换N次（1 ~ N-1）
		tmp = i
		while (tmp > 0 and arry[tmp] < arry[tmp-1]):  #内循环遍历索引左侧的元素，进行替换
			# print (i, tmp)
			arry[tmp], arry[tmp-1] = arry[tmp-1], arry[tmp]
			tmp -= 1
	return arry

def insert_sort_2(arry):
	n = len(arry)
	if(n == 0 or n == 1):
		return arry
	for i in range(1, n):   # 外循环遍历N-1次,即交换N次（1 ~ N-1）
		# print (i)
		if (arry[i] < arry[i-1]):
			tmp = arry[i]
			index = i
			for j in range(i-1, -1, -1): #内循环遍历索引左侧的元素，进行移动，最后替换
				# print (i, j)
				if (arry[j] > tmp):
					arry[j+1] = arry[j]
					index = j #暂定要插入的下标
				else:
					break
			arry[index] = tmp
	return arry


if __name__ == '__main__':
	arry = [2,1,3,4,5]
	arry = [7,2,1,8,3,4,5]
	sortedArry = insert_sort_2(arry)
	print(sortedArry)