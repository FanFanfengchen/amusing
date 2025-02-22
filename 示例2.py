a=100
b=200
print(a,b,'装逼，我让你飞起来')#这是一个简单的代码
================================================
a=50
b=100
c=200
print(a*b/c)
print(a+b)
print("你好，晚上好")
================================================
print('b')
print(chr(98))
print('c')
print(chr(67))
print(8)
print(chr(56))
print('[')
print(chr(91))
================================================
print(ord('你'),ord('好'))
print(chr(20320),chr(22909))
================================================
flag = False
name = 'liunx'
if name == 'liunx':        #判断变量是否为 python
    flag = True            #条件成立时设置标志为真
    print('你好啊，新同学！')  #并输出欢迎信息
else:
    print(name)            #条件不成立时输出变量名称
===================================================
num = 0
if num == 3:        #判断Num的值
 print('boss')
elif num == 2:
 print('user')
elif num == 1:
  print('worker')
elif num == 0:
    print('nimalege')
elif num < 0:       #值小于零时输出
     print('error')
else:
    print('roadman')#条件不成立时输出
===============================================
cao = 9
if cao >= 0 and cao <= 10:#判断值是否在0~10之间
    print('你好，你好，你好！')
#输出结果：我不好

cao = 10
if cao < 0 and cao > 10:#判断值是否在小于0或大于10
    print('我上早八')
else:
    print('宝了个贝的，这是给我干那来了，这还是国内吗？')
#输出结果：孩子，这并不好笑

cao = 8
#判断值是否在0~5或者10~15之间
if(cao >= 0 and cao <= 5)or(cao >= 10 and cao <= 15):
    print('我测你温码')
else:
    print('我是丁真，这是我的好朋友芝士雪豹。')
#输出结果：嗷呜~ 雪豹别叫!
==============================================
var = 100
if var == 100:
    print("太好啦，是烧鸡，我们没救了！")
    print("心还没有悬着就去世了！")
蛊真人 = '大专巅峰'
if 蛊真人 == '大专巅峰':
    print("“你到底干了什么，你不跟我们干，我们以后怎么赚大钱”室友跺着脚恶狠狠地瞪着他。")
    print("他淡然一笑“很简单，我进厂不就是了”说完，他的气息不再掩饰，显露而出，大专巅峰！！一瞬间，流水线再次一寂。")
    print("我乃大专巅峰！何人敢叼我，何人能叼我！他口中低吟道：")
    print("电子厂中寒风吹，流水线上大神归")
    print("一号工位黑奴泪，褪去校服人向北")
    print("无休倒班万人退，三千工资空落泪")
    print("宿命天成当厂妹，本科悔而我不悔!")
    print("早岁已知挣钱艰，仍许资本荡人间")
    print("十年苦读身如絮，无尘车间客独行")
    print("千磨万击手铸铁，殚精竭虑打工件")
    print("今朝人向工位处，打件打人还打天")
    print("从今以后，他就彻底从一位学生变成一位打工人，可以堂堂正正的打螺丝，造福车间了，工友们的历史，资本家们的历史不得不记载他的名字，至此他和数百位工友并肩，宛若大日光照千古，其余同学无论多么豪杰英雄，皆为繁星。")
大专生 = '发言'
if 大专生 == '发言':
    print('不过是些许风霜罢了')
    print('面对凶险万分的流水线，不退反进，仰天大喝：件来！')
    print('今朝剑指叠云处，炼蛊炼人还炼天')
print('今朝剑指叠云处，炼蛊炼人还炼天')
================================================
age = input('Enter your age: ')#输入你的年龄
print(age)#输出你的输入
================================================
x = 10
y = 5
s = x*y
print(s)
================================================
result = '我' + '和' + '你'
print(result)
================================================
a,b,c = 1,2,'jojo'
print(a,b,c)
================================================
str = '你好啊，外邦的旅客！'
print(str)
print(str[0])
print(str[1])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "end")
print(str[:7])
===============================================
list = [ 'What can I say?', 786 , 2.23, 'jojo', 70.2]
tinylist = [123, 'jojo']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)
===============================================
dict = {}
dict['我来助你！'] = "广智救我！"
dict['出门撞大运'] = "新年快乐！"

tinydict = {'米饭仙人': '风灵月影','刚满18岁':114514,'我这一生如履薄冰':'菜就多练'}


print(dict['我来助你！'])
print(dict['出门撞大运'])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print(tinydict.items())
===============================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 21
b = 10
c = 0

if a == b:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if a != b:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if a != b:
    print("3 - a 不等于 b")
else:
    print("3 - a 等于 b")

if a < b:
    print("4 - a 小于 b")
else:
    print("4 - a 大于等于 b")

if a > b:
    print("5 - a 大于 b")
else:
    print("5 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print("6 - a 小于等于 b")
else:
    print("6 - a 大于  b")

if b >= a:
    print("7 - b 大于等于 a")
else:
    print("7 - b 小于 a")
======================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = '就凭你也配直视我！'#神
b = '把头低下！'#精
list = ['诶呀', '真的是你呀', '哈哈', '嗐呦', 'baby'];#练习生

if (a in list):#如果，“神”在“练习生”里。就告诉你，勇敢去做，否则，没有不可能
    print("勇敢去做")#对
else:#不
    print("没有不可能")#对

if (b not in list):#如果“神经”在“练习生”里，就偷懒
    print("2 - 变量 b 不在给定的列表中 list 中")#懒
else:#否则
    print("2 - 变量 b 在给定的列表中 list 中")#偷

# 修改变量 a 的值
a = '真的是你呀'#练习时长两年半
if (a in list):#如果你有两年半的练习
    print("3 - 变量 a 在给定的列表中 list 中")#你就练习了两年半
else:#杂鱼
    print("3 - 变量 a 不在给定的列表中 list 中")#错过就是失去，你明白了吗。
===========================================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 20#变量为20
b = 10#变量为10
c = 15#变量为15
d = 5#变量为5
e = 0#变量为0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)#输出上面的式子

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)#费手

e = (a + b) * (c / d);  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)#一对对照组

e = a + (b * c) / d;  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)#看，电灯泡
=======================================================
#!/usr/bin/python

count = 0#设定函数值为0
while (count < 9):#在当函数值小于9的条件下循环输出以下内容
    print('The count is:', count)#输出，包含下一个变量
    count = count + 1#每一次循环都加1

print("Good bye!")#不成熟的解释
=========================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = input("随便 :")  #随便写一个，回车
    print("写了个寂寞: ", num)#输出你刚刚写下的东西

print("拜拜!")#友好的再见
=======================================
#!/usr/bin/python

count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")
==========================================
#!/usr/bin/python

flag = 1

while (flag): print('Given flag is really true!')

print("Good bye!")
===================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

for letter in '一个字，绝':  # 第一个实例
    print("看看看看: %s" % letter)

fruits = ['唱', '跳', 'rap','篮球']
for fruit in fruits:  # 第二个实例
    print('真的是你呀，哈哈！: %s' % fruit)

print("baybay!")
==================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

fruits = ['鸡', '你', '太美']
for index in range(len(fruits)):
    print('真的是你呀！哈哈 ： %s' % fruits[index])

print("beybey!")
====================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

for num in range(10, 20):  # 迭代 10 到 20 (不包含) 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print('%d 是一个质数' % num)

# !/usr/bin/python
# -*- coding: UTF-8 -*-

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i, " 是素数")
    i = i + 1

print("Good bye!")
==============================================
apple = 'eat'
kill = 'eat'  # 修正了这里，将 kill 的值改为 'eat'
I = 'you'
kiss = 'you'

# 检查条件是否满足
if (apple == kill) and (I == kiss):
    print('一袋米要抗几楼（感受痛苦吧），')
    print('一袋米要抗二楼（思考痛苦吧），')
    print('一袋米要给多了（接受痛苦吧），')
    print('一袋米我洗嘞（理解痛苦吧），')
    print('一袋米我洗了那么多泥（不了解痛楚的人），')
    print('和那堆黑瓦，瓦坷垃（是无法了解真正的和平的）！')
    print('颗颗有泥（从现在开始），')
    print('谁给你一袋米呦（让世界感受痛苦），')
    print('行了添水/辛辣天森/心累天塞（神罗天征）！')
elif (apple == kill) and (I != kiss):
    print('一袋米引发的战争')
'''试了三次啊，三次，终于成功了'''
========================================================
a = input("第一个数字：")
b = input("第二个数字：")
# print(type(a))#查看变量类型
a = int(a)
b = int(b)
# print(type(a))
print(a+b)
================================
money = int(input("交出你的money，哈哈哈: "))
if money >= 500:
    print("太好啦，是钱，我们有救了！")
else:
    print("太好了，让我们进入米奇妙妙屋。")
if money >= 1000:
    if money > 1000 and money < 5000:
        print('加油加油！')
    elif money ==1000:
        print('有所懈怠了呀。')
    if money == 1000:
        print('刚刚好，是不是故意的？')
if money >= 500 and money <= 1000:
    if money == 500:
        print('回家吧，你也不希望在外面出丑吧？')
    if money == 1000:
        print('不是故意的，就是有意的！')
    if money > 500 and money < 1000:
        print('你的想法真是让人捉摸不透啊！')
    else:
        print('嘿，你瞅啥呢，我是你蝶！')
================================================
a = int(input("来来来："))
b = 0
while b <= 100: #用while循环
    print(a)
    b = b + 1
    a = a + b
    print(b)
    a = a - b
    # break 用break直接结束循环
====================================时间戳的运用示例
import time

# 获取当前时间戳（秒级时间戳）
timestamp = time.time()
print("当前时间戳（秒）:", timestamp)

# 获取当前时间戳（毫秒级时间戳）
timestamp_ms = int(round(time.time() * 1000))
print("当前时间戳（毫秒）:", timestamp_ms)


import time
from datetime import datetime

# 将秒级时间戳转换为日期时间
timestamp = time.time()
dt = datetime.fromtimestamp(timestamp)
print("从时间戳转换为日期时间:", dt)

# 将毫秒级时间戳转换为日期时间
timestamp_ms = 1672531200000  # 示例毫秒级时间戳
dt_ms = datetime.fromtimestamp(timestamp_ms / 1000)
print("从毫秒级时间戳转换为日期时间:", dt_ms)


from datetime import datetime

# 将日期时间转换为秒级时间戳
dt = datetime.now()
timestamp = dt.timestamp()
print("从日期时间转换为时间戳（秒）:", timestamp)

# 将日期时间转换为毫秒级时间戳
timestamp_ms = int(dt.timestamp() * 1000)
print("从日期时间转换为时间戳（毫秒）:", timestamp_ms)


import time
from datetime import datetime

# 获取当前时间戳并格式化为日期时间字符串
timestamp = time.time()
formatted_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
print("格式化的时间:", formatted_time)


from datetime import datetime

# 计算两个时间戳之间的时间差
timestamp1 = time.time()
time.sleep(2)  # 模拟等待2秒
timestamp2 = time.time()

# 计算时间差（秒）
time_diff = timestamp2 - timestamp1
print("时间差（秒）:", time_diff)


from datetime import datetime, timedelta

# 创建一个日期时间对象
dt = datetime.now()
print("当前日期时间:", dt)

# 添加时间
new_dt = dt + timedelta(days=1, hours=2, minutes=30)
print("添加时间后:", new_dt)

# 减去时间
old_dt = dt - timedelta(days=1)
print("减去时间后:", old_dt)


from datetime import datetime

# 定义两个日期时间
start_time = datetime(2024, 1, 1)
end_time = datetime(2024, 1, 15)

# 计算时间戳差
time_diff = (end_time - start_time).total_seconds()
print("两个日期之间的时间戳差（秒）:", time_diff)
========================================================时间控制循环示例（好玩）
# 使用 time.time() 来控制循环时间
import time

# 设置循环的最大运行时间（秒）
max_duration = 5  # 例如，让循环运行 5 秒

# 记录循环开始的时间
start_time = time.time()

while True:
    # 检查是否超过时间限制
    if time.time() - start_time > max_duration:
        print("循环运行时间已超过限制，停止循环。")
        break

    # 循环内的代码
    print("我是time.time()")
    time.sleep(1)  # 模拟每次循环耗时 1 秒

# 使用 datetime.timedelta 来控制循环时间
from datetime import datetime, timedelta

# 设置循环的最大运行时间（秒）
max_duration = 5  # 例如，让循环运行 5 秒

# 记录循环开始的时间
start_time = datetime.now()

while True:
    # 检查是否超过时间限制
    if (datetime.now() - start_time).total_seconds() > max_duration:
        print("循环运行时间已超过限制，停止循环。")
        break

    # 循环内的代码
    print("我是datetime.timedelta")
    time.sleep(1)  # 模拟每次循环耗时 1 秒


# # 使用 signal 模块（仅限 Unix 系统）
# import signal
# import time
#
# # 定义一个标志变量，用于控制循环
# stop_loop = False
#
# # 定义信号处理函数
# def handle_timeout(signum, frame):
#     global stop_loop
#     print("时间限制已到，停止循环。")
#     stop_loop = True
#
# # 设置信号处理
# signal.signal(signal.SIGALRM, handle_timeout)
# signal.alarm(5)  # 设置 5 秒后发送 SIGALRM 信号
#
# try:
#     while not stop_loop:
#         print("循环正在运行...")
#         time.sleep(1)  # 模拟每次循环耗时 1 秒
# finally:
#     signal.alarm(0)  # 取消定时信号

# 使用多线程
import threading
import time

# 定义一个标志变量，用于控制循环
stop_loop = False

# 定义一个函数来控制循环时间
def stop_after_timeout(timeout):
    global stop_loop
    time.sleep(timeout)
    stop_loop = True
    print("时间限制已到，停止循环。")

# 设置时间限制
timeout = 5  # 例如，让循环运行 5 秒

# 启动一个线程来控制时间
thread = threading.Thread(target=stop_after_timeout, args=(timeout,))
thread.start()

# 主循环
while not stop_loop:
    print("注意，我是多线程")
    time.sleep(1)  # 模拟每次循环耗时 1 秒

thread.join()  # 等待线程结束


# 使用 asyncio（异步方式）
import asyncio

async def main():
    # 设置循环的最大运行时间（秒）
    max_duration = 5  # 例如，让循环运行 5 秒

    # 记录循环开始的时间
    start_time = asyncio.get_event_loop().time()

    while True:
        # 检查是否超过时间限制
        if asyncio.get_event_loop().time() - start_time > max_duration:
            print("循环运行时间已超过限制，停止循环。")
            break

        # 循环内的代码
        print("我是asyncio")
        await asyncio.sleep(1)  # 模拟每次循环耗时 1 秒

# 运行异步主函数
asyncio.run(main())
==========================================================
s = "这是真的啊，你不会忘了吧？"
for i in s:
    print("这一次，请确定:",i)

for i in range(10): #从0数到10，但不包含10
    print(i)

for i in range(3,10): #3~9
    print(i)

i = 1
while i <= 10:
    print(i)
    i = i + 2

for i in range(1,10,2):
    print(i)

x = 10
if x > 5:
    pass #跳过，下次想好了再补充
print("吹牛逼呢，见过吗，这叫俄罗斯大贝塔，你就只能看着我骑")
===========================================================
# int:整数，可以进行整数之间的加减乘除，以及比较大小
# 比如：
a = 10
b = 15
print(a+b)
print(a-b)
print(a*b)
print(a/b)
if a < b:
    print('a < b')
if a > b:
    print('a > b')
if a == b:
    print('a == b')
if a >= b:
    print('a >= b')
if a <= b:
    print('a <= b')

# float:小数，浮点数
# 比如:
a = 10.57
print(a)
# 但是，有一个无限小数点
# 比如：
print(10/3) #它的输出的最后一位存在误差，说明关于无穷，计算机也是只能给出不准确的数
#还有，小数的数据范围是无限的，而整数会在某一个特定区间内是可以清楚表示的
#就像你与你命中注定的人的距离，处于小数时，距离是可以无限近和无限远的。但是，处于整数时，在一瞬间，你们两个的关系就明确了
#计算机是一款二进制产品，语言基础就：0,1，人家本来就难，不要强迫别人，所以，计算机在表示一个小数时是会有误差的
bool
