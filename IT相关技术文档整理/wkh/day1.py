#   单行注释  #
#   多行注释 ''''''
# print("hello world")
# var = input("qingshuru:")
#print(var)
#   三角形面积计算
#
# di = input("请输入三角形的底：")
# # if di==int:
#     print(di)
# else:
#     input("长度请输入数字")
# gao = input("请输入三角形的高：")
# if gao==int(gao):
#     print(gao)
# else:
#     input("长度s请输入数字")
# qiuhe = int(di)*int(gao) / 2
# print(qiuhe)
# print('hello world!','北京','天安门',sep='我是分隔符  ，')
# print("hello world!",end='\t')
a = "hello"
b = "e"
print(a+b)
# 算术运算符
a = 10
b = 3
print(f"a + b = {a + b}")  # 加法
print(f"a - b = {a - b}")  # 减法
print(f"a * b = {a * b}")  # 乘法
print(f"a / b = {a / b}")  # 除法
print(f"a // b = {a // b}")  # 整数除法
print(f"a % b = {a % b}")  # 取余
print(f"a ** b = {a ** b}")  # 幂运算

# 比较运算符
c = 5
d = 7
print(f"c == d is {c == d}")  # 等于
print(f"c!= d is {c!= d}")  # 不等于
print(f"c > d is {c > d}")  # 大于
print(f"c < d is {c < d}")  # 小于
print(f"c >= d is {c >= d}")  # 大于等于
print(f"c <= d is {c <= d}")  # 小于等于

# 赋值运算符
e = 15
e += 5
print(f"e after e += 5 is {e}")
e -= 3
print(f"e after e -= 3 is {e}")
e *= 2
print(f"e after e *= 2 is {e}")
e /= 4
print(f"e after e /= 4 is {e}")
e %= 3
print(f"e after e %= 3 is {e}")
e **= 2
print(f"e after e **= 2 is {e}")
e //= 3
print(f"e after e //= 3 is {e}")

# 逻辑运算符
f = True
g = False
print(f"f and g is {f and g}")  # 与
print(f"f or g is {f or g}")  # 或
print(f"not f is {not f}")  # 非

# 成员运算符
h = "hello"
print(f"'e' in h is {'e' in h}")  # in
print(f"'x' not in h is {'x' not in h}")  # not in

# 身份运算符
i = [1, 2, 3]
j = i
k = [1, 2, 3]
print(f"i is j is {i is j}")  # is
print(f"i is k is {i is k}")  # is
print(f"i is not k is {i is not k}")  # is not