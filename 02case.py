# 人生重开模拟器~
# 游戏开始的时候,设定初始属性:颜值,智力,家境,体质
# 开始游戏随机生成性别和出生点
# 针对每一年生成人生经理(随机因素加当前角色的属性)
import random
import sys
import time

# 界面设置
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('|         游戏加载中          |')
print('|         花有重开日          |')
print('|         人无在少年          |')
print('~~~~~~~欢迎来到人生模拟器~~~~~~~')

Face = 0
Strong = 0
IQ = 0
Home = 0

# 基础属性设置
while True:
    # 设置初始属性:颜值,智力,家境,体质,总和不能超过20,每一项取值都是1-10之间
    print(f'请设置初始属性(总点数20)')
    face = int(input('请输入颜值(1~10):'))
    # strong = int(input('请输入体质(1~10):'))
    # IQ = int(input('请输入智力(1~10):'))
    # home = int(input('请输入家境(1~10):'))

    # 通过条件语句,对于用户的输入进行判断
    if 0 <= face <= 10:
        strong = int(input('请输入体质(1~10):'))
        if 0 <= strong <= 10:
            iq = int(input('请输入智力(1~10):'))
            if 0 <= iq <= 10:
                home = int(input('请输入家境(1~10):'))
                if 0 <= home <= 10:
                    count = face + strong + iq + home
                    if 0 < count <= 20:
                        Face = face
                        Strong = strong
                        IQ = iq
                        Home = home
                        print('初始属性设置完毕')
                        print(f'您当前的属性为:颜值{face},体质{strong},智力{IQ},家境{home}')
                        break
                    # elif 0 <= count < 20:
                    #     temp = 20 - face - strong - IQ - home
                    #     print(f"您尚有{temp}点未分配,请重新分配")
                    #     continue
                    else:
                        print("点数不够用啦~重新进行设置吧")
                        continue
                else:
                    print("请重新输入")
                    continue
            else:
                print("请重新输入")
                continue
        else:
            print("请重新输入")
            continue
    else:
        print("请重新输入")
        continue
    # if face < 1 or face > 10 :
    #     print("请重新输入颜值")
    #     continue
    # if strong < 1 or strong > 10 :
    #     print("请重新输入体质")
    #     continue
    # if IQ < 1 or IQ > 10:
    #     print("请重新输入智力")
    #     continue
    # if home < 1 or home > 10:
    #     print("请重新输入家境")
    #     continue

    # 判断总点数是否正确
    # count = face + strong + IQ + home
    # if count < 0 or count > 20:
    #     print('总属性和越界,请重新输入')
    #     continue
    #
    # print('初始属性设置完毕')
    # print(f'您当前的属性为:颜值{face},体质{strong},智力{IQ},家境{home}')
    # break

# 生成角色的性别
# random.Random(begain,end),就能生成[beg,end]的随机整数
# 在Python中,若想引入其他模块,需要先使用import语句,把模块的名字导入进来
print("正在生成中:")
time.sleep(1)
point = random.randint(1, 9)
# print(f"point={point}")
if point % 2 == 0:
    gender = 'woman'
    print("你是个女孩")
else:
    gender = 'man'
    print("你是个男孩")

# 出生点设置
""" 家境:
        >=10    第一档,巨量属性加成
        7~9     第二档,大量属性加成
        4~6     第三档,少量属性加成
        1~3     第四档,属性衰减   
"""
# 属性加成
point = random.randint(1, 3)
PointFace = random.randint(1, 3)
PointStrong = random.randint(1, 3)
PointIQ = random.randint(1, 3)
PointHome = random.randint(1, 3)
# temp = point + Home
# print(temp)

if Home >= 10:
    # 第一档
    print("您出生在帝都,您的父母是上市公司合伙人")
    Face += PointFace
    Strong += PointStrong
    IQ += PointIQ
    Home += PointHome
elif 7 <= Home <= 9:
    # 第二档
    if point == 1:
        print("您出生在大城市,您的父母是公务员")
        Face += PointFace
        IQ += PointIQ
    elif point == 2:
        print("您出生在大城市,您的父母是企业高管")
        Home += PointHome
        Face += PointFace
    else:
        print("您出生在大城市,您的父母是大学教授")
        IQ += PointIQ
        Home += PointHome
elif 4 <= Home <= 6:
    # 第三档
    if point == 1:
        print("您出生在三线城市,您的父母是医生")
        Strong += PointStrong
    elif point == 2:
        print("您出生在三线城市,您的父母是老师")
        IQ += PointIQ
    else:
        print("您出生在三线城市,您的父母是个体户")
        Home += PointHome
else:
    # 第四档
    if point == 1:
        print("您出生在农村,您的父母是农民")
        Strong += PointStrong
        Face -= PointFace
    else:
        print("您出生在农村,您的父母是无业游民")
        Home -= PointHome

print(f'您当前的属性为:颜值{Face},体质{Strong},智力{IQ},家境{Home}')

# 角色人生经历
"""年龄阶段:
            幼年阶段(0,6)       可塑性强
            青年阶段[6,22)      求学
            壮年阶段[23,55)     平稳
            老年阶段(55++)      颜值,体质,智力明显退化
            游戏结束判定
"""

# 使用一个循,按照你年龄循环1~10
# 针对每一年,都生成一个随机数
# 根据角色年龄,性别,年龄,各种属性出发各种事件,随机数会对事件的结果造成影响
# 每一年结束,打印这一年发生的事件,及属性
# 若遇到夭折的情况,使用exit函数结束程序

# 幼年阶段:
for age in range(0, 11):
    # 把一年的打印整理到一个字符串,在年尾统一打印
    info = f'你今年{age}岁, '
    point = random.randint(0, 3)
    # 编写各种事件的代码

    # 性别触发的事件
    if gender == "woman" and Home <= 3 and point == 0:
        info += "您的家里人重男轻女,很不幸您被遗弃了. "
        print(info)
        print("游戏结束")
        # sys是system的缩写,是python内部提供的模块
        # sys.exit的作用是退出程序
        sys.exit(0)
    # 体质触发事件
    elif Strong <= 0:
        info += "由于您的体质过差,下个世界再见吧."
        print(info)
        print("游戏结束")
        sys.exit(0)
    elif 0 < Strong < 3:
        info += "你生了一场大病, "
        if Home >= 5:
            info += "在父母的悉心照料下,你康复了. "
            # god是上帝因子,确定增减属性的值
            God = random.randint(1, 3)
            Strong += God
            Home -= God
        else:
            info += "你的身体状况又糟糕了. "
            # god是上帝因子,确定增减属性的值
            God = random.randint(1, 3)
            Strong -= God
    # 年龄触发事件
    elif age == 6:
        info += "你上小学了, "
    # 颜值触发事件
    elif Face <= 2 and age >= 6:
        info += "因为相貌原因,您被周围人孤立了. "
        if IQ > 5:
            info += "学习可以使你快乐. "
            # god是上帝因子,确定增减属性的值
            God = random.randint(1, 3)
            IQ += God
        else:
            if Strong > 5:
                info += "你和小朋友打了起来. "
                # god是上帝因子,确定增减属性的值
                God = random.randint(1, 3)
                Strong += God
                IQ -= God
            else:
                info += "你经常被别的小朋友欺负. "
                # god是上帝因子,确定增减属性的值
                God = random.randint(1, 3)
                Strong -= God
    # 智商触发事件
    elif IQ <= 0 and age > 6:
        info += "你被送入了特殊学校"
        # god是上帝因子,确定增减属性的值
        God = random.randint(1, 3)
        IQ += God
    elif 0 < IQ <= 2:
        info += "您看起来傻傻的. "
        if Home >= 8 and age >= 6:
            info += "你的父母把你送到更好的学校学习. "
            # god是上帝因子,确定增减属性的值
            God = random.randint(1, 3)
            IQ += God
        elif 4 <= Home <= 7:
            if gender == "man":
                info += "你的父母鼓励你多运动,争取成为运动员. "
                # god是上帝因子,确定增减属性的值
                God = random.randint(1, 3)
                Strong += God
            else:
                info += "你的父母鼓励你多打扮自己. "
                # god是上帝因子,确定增减属性的值
                God = random.randint(1, 3)
                Face += God
        else:
            # 家境<4
            info += "你的家长为你操碎了心"
            if point == 1:
                # god是上帝因子,确定增减属性的值
                God = random.randint(1, 3)
                Strong -= 1
            elif point == 2:
                # god是上帝因子,确定增减属性的值
                God = random.randint(1, 3)
                IQ -= God
            else:
                pass
    # 健康成长事件
    else:
        info += "你健康成长, "
        if point == 1:
            info += "你看起来更结实了. "
            # god是上帝因子,确定增减属性的值
            God = random.randint(1, 3)
            Strong += God
        elif point == 2:
            info += "你看起来更好看了"
            # god是上帝因子,确定增减属性的值
            God = random.randint(1, 3)
            Face += God
        else:
            # 无事发生
            pass
    Strong += 1
    IQ += 1
    # 打印这一年发生的事情
    print(info)
    print(f'您当前的属性为:颜值{Face},体质{Strong},智力{IQ},家境{Home}')
    print("------------------------------------------------------")
    # time 也是python提供的模块,sleep是暂停一秒
    time.sleep(1)
