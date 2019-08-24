# Bài tập return
# cho hàm y=x**3 + 2 * x**2 - 4 * x + 1
# đầu vào là một dict chứa toạ độ, viết chương trình phân loại, nếu đi qua trả về list A , ko đi qua trả về list B
def f_x(x):
    return x**3 + 2 * x**2 - 4 * x + 1

def check_point(x, y):
    if y == f_x(x):
        return True
    return False

def fil_point(lst_point):
    lst_A, lst_B = [], []
    for l in lst:
        if check_point(*l):
            lst_A.append(l)
            continue
        lst_B.append(l)
    return lst_A, lst_B

def cal_sum(lst):
    s = 0
    for value in lst:
        s += value[1]
    return s

lst = [(-5, -20), (-4, -15), (-3, 4), (-2, 9), (-1, 7), (0, 1)
, (1, -7), (2, -9), (4, 81), (5, 130)]

lst_A_after, lst_B_after = fil_point(lst)
print(abs(cal_sum(lst_A_after) - cal_sum(lst_B_after)))
print(ls)