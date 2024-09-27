#
# import random
# secret = random.randint(1,10)
# temp = input("猜一下我现在心里想的数字")
# guess = int(temp)
# while guess != secret:
#     temp = input("重新猜一下我现在心里想的数字")
#     guess = int(temp)
#     if guess == secret:
#         print("猜中啦")
#     else:
#         if guess > secret:
#             print("猜大啦")
#         else:
#             print("猜小啦")
# print("游戏结束，正确结果是",secret,"拼接一下")
# print(secret)
# strs = '''从明天起，做一个幸福的人
# 喂马、劈柴，周游世界
# 从明天起，关心粮食和蔬菜
# 我有一所房子，面朝大海，春暖花开。
# 从明天起，和每一个亲人通信
# 告诉他们我的幸福
# 那幸福的闪电告诉我的
# 我将告诉每一个人。
# 给每一条河每一座山取一个温暖的名字
# 陌生人，我也为你祝福
# 愿你有一个灿烂的前程
# 愿你有情人终成眷属
# 愿你在尘世获得幸福
# 我只愿面朝大海，春暖花开。'''
# print(strs)
# help(ValueError)
#
# while True:
#     try:
#         score = int(input("请输入一个分数："))
#         if 100 >= score >= 90:
#             print("A")
#         elif 90 >= score >= 80:
#             print("B")
#         elif 80 >= score >= 70:
#             print("C")
#         elif 70 >= score >= 60:
#             print("D")
#         elif 60 >= score >= 0:
#             print("E")
#         elif score < 0 or score > 100:
#             print("输入错误")
#             continue
#         break
#     except ValueError:
#         print("输入错误，请输入一个整数")
for i in range(10):
    if i % 2 != 0:
        continue
    i += 2
    print(i)

number = []
for i in range(10):
    number.append(i)
    print(number)
number.append(11)
print(number)
number.extend([2,3])
print(number)
number.pop(2)
print(number)
number.insert(2,2)
print(number)
number.remove(11)
print(number)
del number[11]
print(number)
print(number[::-1])

print(2 in number)

temp = 1,2,3
print(type(temp))
temps = ()
print(type(temps))
temps = 1,
print(type(temps)
