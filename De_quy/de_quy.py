def cal_sum(lst):
	if not lst:	# tương đương if len(lst) == 0:
		return 0
	else:
		return lst[0] + cal_sum(lst[1:])
print(cal_sum([1,2,3,4,5]))