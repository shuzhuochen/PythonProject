# # 初识python
# # print("hello world")
# print(1 + 2 - 3)
# print(1 + 2 * 3)
# print(1 + 2 / 3)
# print((67.5 + 89.0 + 12.9 + 32.2) / 2)
#
# # python中的变量
# avg = (67.5 + 89.0 + 12.9 + 32.2) / 4
# print(avg)
# total = (67.5 - avg) ** 2 + (89.0 - avg) ** 2 + (12. - avg) ** 2 + (32.2 - avg) ** 2
# print(total)
# result = total / 3
# print(result)
# # 变量可以视为一块可用来存储数据的盒子
#
# # python中的语法
# # '='是赋值运算符
# # 变量名必须是 数字 字母 下划线 构成
# # 变量名不能包含特殊符号 数字不能开头
# # 变量名不能和'关键字'重复
# # python中的变量名，是区分大小写的
# # 给变量命名的时候，尽量用描述性的单词表示
# a = 10
# # 首次使用 '='是创建操作
# b = a
# # 后续使用 '='是修改操作
# print(b)
#
# # python的变量类型
# a = 10.000000000
# print(type(a))
# # 在python中，int类型的范围是无穷的，因此python中没有long类型
# # 在python中，float类型的范围是无穷的，因此python中没有double类型

# # python中的字符串
# c = 'hello'
# d = "hello"
# print(type(c))
# print(type(d))
# # 单引号和双引号输出的字符串类型都是string
# # 如果字符串里面包含了单引号,就可以用双引号引起来
# # 若同时含有双引号和双引号,使用三引号
# e = "My name is 'csz' "
# print(type(e))
# f =''' "My name is 'csz' "  '''
# print(e)
# # 使用内置函数'len'求字符串的长度
# print(len(e))

# 字符串的拼接
# 不能把字符串和数字混合相加
# a1  = 'hello'
# a2  = 'world'
# a3 = a1+a2
# print(a3)
# b1 = 'hello'
# b2 = 10
# b3 = b1+b2
# print(b3)

# 布尔命题
# c1 = True
# c2 = False
# print(type(c1))
# print(type(c2))

# # 类型的意义
# # 不同的类型,占用的内存空间是不同的
# # int默认4字节 动态扩容
# # float固定8字节
# # bool一个字节
# # str变长
# # int/float,+,-*/   不能使用len
# # str +但是不能*,-,/ 可以使用len
# # 动态类型
# a:int = 10
# print(type(a))
# a:str = 'hello'
# print(type(a))
# a = True
# print(type(a))
# # a的类型随着程序的运行,发生了改变
# # 静态类型:程序运行中,变量的类型始终不变

# # '#'右侧表示行注释
# '''
# 表示文档字符串
# '''
# # 注释的内容应该准确

# # 格式化字符串,f表示format,此时可以在{}嵌入数值
# a = 10
# print(f"a = {a}")

# # 通过控制台输入,利用input函数
# # input执行的时候,就会等待用户输入,用户不输入,就一直等待
# # input的返回值是'str'类型,若需要进行算数运算,则应该进行类型转换如:int()
# # num = input('请输入一个整数:\n')
# # print(f'您输入的数字是{num}')
# # print(type(num))
# a = input('请输入第一个整数:')
# b = input('请输入第二个整数:')
# print(f'a + b = {a+b}') #返回值是str
# a = int(a)
# b = int(b)
# print(f'a + b = {a+b}') #返回值是int
# # 若想把整数转成字符串?str()
# # 若想把整数转成浮点数?float()

# # 输入4个小数,求其平均值
# a = input("请输入第一个数字:\n")
# b = input("请输入第二个数字:\n")
# c = input("请输入第三个数字:\n")
# d = input("请输入第四个数字:\n")
# a = float(a)
# b = float(b)
# c = float(c)
# d = float(d)
# avg = (a+b+c+d)/4
# print(f'the avg of a b c d is {avg} ')

# # 运算符
# # 算数运算符: + - * / % ** // 先算乘方,再算乘除,最后计算加减
# # result = (1 + 2) * 3
# # print(result)
# # 在python中,0不能做除数 程序运行异常之后,异常后的程序不会被执行
# # print(result/0.0)
# # 在python中整数除以整数,结果可能是小数,不会出现截断的情况
# # %是求余数~ 得到的余数一定是小于除数的!
# # print(7 % 3)
# # **是乘方运算,既支持整数次方,又支持小数次方
# # print(4 ** 2)
# # print(4 ** 0.5)
# # //是地板除法(取整除法),对针对计算的结果进行"向下取整"
# print(7 // 2)
# print(-7 // 2)
# # 关系运算符:比较两个操作数之间的"大小""相等"的关系
# #  > < >= <= == !=
# # 关系运算符的表达形式是布尔类型,而且可以比较字符串
# # 关系运算符比较字符串是比较的字典序,中文字符串比较没有意义
# # a = 'hello'
# # b = 'world'
# # print(a < b)
# # print(a > b)
# # print(a >= b)
# # print(a <= b)
# # print(a == b)
# # print(a != b)
# # 针对浮点数来说,正确的比较是否相等的方法的是做差,看看是否在误差之内
# # a = 0.1 + 0.2
# # b = 0.3
# # # 在python中支持连续比较的写法
# # print(-0.0000001 < (a - b) < 0.0000001)
# # 逻辑运算符
# a = 10
# b = 20
# c = 30
# print(a < b and b < c)
# print(a < b and b > c)
# print(a > b or b < c)
# print(a > b or b > c)
# print(not a < b)
# print(not a > b)
# 连续赋值a = b = c = 20
# # 在实际环境中,一般不采用这种方法进行赋值
# # 多元赋值
# a, b = 10, 20
# temp =10
# temp = a
# a = b
# b = temp
# # 使用多元赋值进行交换
# # a = 10
# # b = 20
# # a, b = b, a
# # print(a,b)
# # 复合赋值运算符
# # a = 0
# # a += 1
# # print(a)
# # a = 'hello'
# a = 10
# # b = 'world'
# # b = 10
# # b = 2.2
# # b = True python中整数可以与布尔值相加 但是该操作没有意义
# print(a+b)
# # 顺序语句 python是顺序执行
# # print('111')
# # print('222')
# # print('333')
# # # 条件语句
# # choice = int(input("输入1表示卷王,输入0表示咸鱼"))
# # if choice == 1:
# #     print("卷王")
# # elif choice ==0:
# #     print("咸鱼")
# # else:
# #     print("请重新输入")
# # 关于缩进
# # a = int(input("请输入一个整数"))
# # if a == 1:
# #     print("aaa")
# #     print("bbb")
# # 判断是否是闰年
# # 每隔4年润一次
# # 若年份能被100整除,是世纪闰年,得看是否被400整除
# # a = int(input("请输入一个年份"))
# # if a % 100 ==0:
# #     # 世纪闰年的判定
# #     if a % 400 ==0:
# #         print("闰年")
# #     else:
# #         print("不是闰年")
# # else:
# #     if a % 4 ==0:
# #         print("是闰年")
# #     else:
# #         print("不是闰年")
# # 输入一个数字,若为1,则打印hello
# # a = int(input("请输入一个数字:\n"))
# # if a == 1:
# #     # 为了保持代码缩进,啥都不做可以使用pass
# #     # print('hello')
# #     pass
# # else:
# #     print('wrong')
# # 循环语句(while and for)
# # while 循环
# '''while'''
# num = 1  # '''循环变量的初始值'''
# while num <= 10:  # 循环变量的结束条件
#     print(num)
#     num = num + 1
# 计算1 ~ 100的和
# i = 1
# sum = 0
# while i <= 100:
#     sum = sum +i
#     i   = i + 1
# print(f'sum ={sum}')
# # 计算5的结成
# i = 1
# result =1
# while i < 6:
#     result *= i
#     i += 1
# print(f'result ={result}')
'''    for 循环的基础语法  '''
# for i in range(1,11,2):
#     # range是一个内建函数,左闭右开区间
#     # range是一个内建函数,左闭右开区间
#     print(i)
# # 求1+2+3+...+100
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)
# 假设我要吃5个包子
# for i in range(1,6):
#     if i ==3:
#         continue
#     print(f'吃第{i}个包子')
# for i in range(1,6):
#     if i ==3:
#         break
#     print(f'吃第{i}个包子')
# 给定若干个数字,求取其平均值
# Sum = 0
# Count = 0
# while True:
#     num = input('请输入一个数字')
#     if num == ';':
#         # 当用户输入一个分号的时候,表示输入结束
#         break
#     num = float(num)
#     Sum += num
#     Count += 1
# print(f'avera= {Sum/Count}')