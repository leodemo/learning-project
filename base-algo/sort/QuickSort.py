# coding: utf-8
#---------------------------------------  
#   project：快速排序
#   author：GuoLiang
#   date：2018-03-04
#   language：Python 3.6.1
#   desc：数组从小到大排序
#---------------------------------------
def quick_sort_main(arry):
	# shuffle arry 消除对输入的依赖
	return quick_sort(arry,0,len(arry)-1)

def quick_sort(arry, lo, hi):
	if lo >= hi:
		return arry
	lop = partition(arry, lo, hi)
	quick_sort(arry, lo, lop-1)
	quick_sort(arry, lop+1, hi)
	return arry

def partition(arry, lo, hi): # 切分
	pivot = arry[lo] # 基准是第一个数字
	lop = lo
	hip = hi
	while lop < hip:
		while lop < hip and arry[hip] >= pivot:
			hip -= 1
		while lop < hip and arry[lop] <= pivot:
			lop += 1
		arry[lop], arry[hip] = arry[hip], arry[lop]
	arry[lo], arry[lop] = arry[lop], arry[lo]
	return lop

if __name__ == '__main__':
	arry = [2,1,3,4,5]
	arry = [7,2,1,8,7,3,4,5]
	sortedArry = quick_sort_main(arry)
	print(sortedArry)