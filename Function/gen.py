def gen():
	while True:
		x = yield # ở đây ta đang yield None, vì ta không cần thiết sinh giá trị gì ở  đây
		yield x ** 2
g = gen()
print(next(g))
print(g.send(2))

