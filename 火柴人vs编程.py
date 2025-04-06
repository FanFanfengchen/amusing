# hello#NameError:'hello'不存在,NameError(名称错误)
# print()#打印（由于没有提供内容，所以无事发生）
# print("hi")#打印"hi"
# print("hi")
# print("hi")
# a = 1#将变量a赋值为1
# print(a)
# a = 2
# print(a)
# a = 9
# print(a)
# a = 3
# print(a)
# a = 3+2#数学运算
# print(a)
# a = 3-2
# print(a)
# a = 3*2#乘
# print(a)
# a = 3/2#除
# print(a)
# a = 3//2#整除
# print(a)
# a = 3+2
# b = "string"#字符串，现在b表示字符串"string"
# print(b)#打印b的值
# a = 3+2
# b = "string"
# print(b+"ing")#拼接上"ing"
# a = 3+2
# b = "string"
# print(b+b)#拼接上b
# a = 3+2
# b = "string"
# print(b+a)#TypeError(类型错误)
# a = 3+2
# b = "string"
# print(b+str(a))#将a转换为字符串，再拼接上b
# a = 3+2
# b = "string"
# print(len(b+str(a)))#输出a的长度
# a = "string"
# b = a[]
# print()#这波铸币了，报错了
#看电脑精操作
# a = "string"
# b = a[0]#取得a的第一个字符,0代表1，所以输出"s"
# print(b)
# a = "string"
# b = a[1]
# print(b)
# a = "string"
# b = a[2]
# print(b)
# a = "string"
# for i in a:#使用for循环输出a，这是一种常用的for循环用法
#     print(i)#前面的空格是使用了缩进，你可以用tab键,当a是字符串"string"时，for循环len(a)次，每次让i分别等于a的每一个字符，输出"s"，"t"，"r"，"i"，"n"，"g"
# a = "bark"
# while True:#使用了布尔值（bool）,布尔值只有两种状态，True和False，代表1和0，对和错，真和假
#      print(a)#当布尔值为真时，循环会一直执行下去，当布尔值为假时，循环会停止，跳过，所以这个循环会一直执行打印a
# a = "bark"
# while True:#字符串的.isalnum()方法，判断字符串是否为字母和数字，返回布尔值
#     print(a.upper())#字符串的.upper()方法，将字符串转换为大写，返回新的字符串
# a = "bark"
# while a.isdigit():
# print(a.upper())#没有缩进，所以报错IndentationError(缩进错误)
# a = "bark"
# while a.isdigit():
#      print(a.upper())
# a = "1234"#注意到不成立才改了
# while a.isdigit():#字符串的.isdigit()方法，判断字符串是否为数字，返回布尔值
#     print(a.upper())#字符串的.upper()方法，将字符串转换为大写，返回新的字符串
# a = "1234"
# while not a.isprintable():#只有“不可打印”时，才打印
#      print(a.upper())
#电脑精的失误,又可以了
# a = "RRRAAAAAAAAAAAAAA"#小打小闹
# while  not a.isprintable():#字符串的.isprintable()方法，判断字符串是否可打印，返回布尔值，但是有not，所以无输出
#     print(a.upper())#字符串的.upper()方法，将字符串转换为大写，返回新的字符串
# else:#若上方的条件不成立，则执行else的内容
#     print(a)#天晴了雨停了，你又觉得你行了
# bomd = ['BANG', 'BOOM', 'BAM','POW','POOF','PAH']#列表，列表的元素之间用逗号隔开,充满着各种拟声词的字符串列表
# print(*bomd)#（下面出现了三次）在列表前使用*星号，代表将列表解包，简单来讲就是拆开，你试过就知道了
# import turtle#注入画图模块
# t = turtle.Turtle()#拿到一只turtle画笔，赋值给t
# t.forward(400)#前进400个单位
# t.left(90)#左转90度
# t.forward(800)#前进800个单位
# import turtle
# t = turtle.Turtle()
# t.speed('fast')#设置画笔速度为最快
# t.left(135)#左转135度
# t.forward(1280)#前进1280个单位
# import turtle
# t = turtle.Turtle()
# t.speed('fast')#刚打出来就被打断了
# t.right(90)#右转90度
# t.forward(400)#前进400个单位
# import turtle
# t = turtle.Turtle()
# t.speed('fast')#实际上真正运行的
# t.right(135)#右转135度
# t.forward(900)#前进900个单位
#由于需要，所以把以下两个条件移到这里
# t.pensize(10)#设置画笔粗细为10
# t.speed('fastest')#设置画笔速度为最快
# t.left(85)#左转85度
# while True:#无限循环
#     t.right(170)#右转170度
#     t.forward(400)# 前进400个单位
#     t.left(170)#左转170度
#     t.forward(400)#前进400个单位
#     turtle.bye()#强制送走画笔，由于加纳~
# import string as ammo#注入string,但用as重命名ammo
# gun = list(ammo.ascii_uppercase)#ammo.ascii_uppercase代表所有大写字母组成的字符串，（ammo.ascii_lowercase代表所有小写字母组成）
# print(gun.pop())#（在下面出现九次）用list吧字符串变成列表
# #加粗和加速在这
# print(gun.pop())#（在下面出现四次）
# #送走画笔在这！
# print(gun.pop())#（一次）
# #飞起来，落地
# print(gun.pop())（三次）
# #每一次输出都会带走一个字母，直到没有字母为止
# #后面的省略
# import matplotlib.pyplot as plt#注入数据可视化的库，并且命名为plt（这两行在递归的时候还要用）
# import numpy as np#注入numpy,命名为np
# #val = np.random.randint(1,10,5)#刚开始的
# var = np.random.randint(1,10,10)#打完的，生成[1,10)内的10个随机整数，并赋值给var
# plt.bar(range(len(var)), var)#绘制柱状图
# plt.show()#展示图表
# print(*var)#（总共重复了三次）解包统计图中出现的随机统计数据
# while True:#循环生成随机图表
#     val = np.random.randint(1,10,10)#打完的，生成[1,10)内的10个随机整数，并赋值给val
#     plt.bar(range(len(val)), val)#绘制柱状图，原视频没有，但是这里还需要
#     plt.show()#展示图表
# #运行以下五行代码时要把上面的循环关掉
# val = np.random.randint(1,10,20)#生成长度为20，[0,20)的随机整数列表，并赋值给val
# plt.figure(figsize=(10,5))#将图像大小设置为宽10高5
# plt.errorbar(range(len(val)), val,val,#绘制一个带误差的散点图，x轴为0到19，y轴为val，误差为val，散点图样式为圆形，误差条宽度为6
#              fmt='o',capsize=6)
# plt.show()#展示图表，执行下面两行代码之前可以把我提出，跳过解包的
# print(*var)#（总共执行了五次）
# plt.plot(range(20),
#          color='red')#绘制一个红色的直线，x轴为0到19，y轴为val
# plt.show()#我也是
# print(*var)#（两次）
# plt.title(label='TITLE',#标题，字体大小为20，位置在左侧
#           fontsize=20,#字体大小为20
#           loc='left')#位置在左侧
# plt.show()
# plt.title(label='TITLE',#标题，逆时针旋转90度，位置在左侧
#           fontsize=20,
#           rotation=90,#逆时针旋转90度
#           loc='right')
# plt.show()
# import string#后面的递归要用
# def fire(n, c=1):
    #递归函数，n为层数，c为当前层数,def定义一个函数，使用这个函数时需要传入参数，若参数在定义时有默认值则可以省略
    # if c>n:#递归结束条件，是则返，否则跳
    #     return#返回
    # print(' '*(c-1)+'*'*(2*(n-c)+1))#输出层数
    # fire(n, c+1)#递归调用，层数加1,什么，居然没有输出？
# fire(5)
# x = np.arange(0, 30, 0.1)#（小黄写的）生成从0到30，步长为0.1的数组，并赋值给x
# y = np.cos(x)#生成x的余弦值，并赋值给y
# plt.plot(x, y)#绘制曲线
# plt.show()#展示图表
# x = np.arange(0, 40, 0.1)#（电脑改的）生成从0到40，步长为0.1的数组，并赋值给x
# y = np.cos(x)#生成x的余弦值，并赋值给y
# plt.plot(x, y)#绘制曲线
# plt.show()#展示图表
# fire(10)#（重复两遍）
# import pygame#注入pygame
# pygame.init()#初始化pygame，必须的第一步
# #screen = pygame.display.set_mode((4000, 2000))#设置屏幕大小，并赋值给screen，太大了
# screen = pygame.display.set_mode((400, 200))#设置屏幕大小，并赋值给screen
# clock = pygame.time.Clock()#设置时钟，并赋值给clock
# #square_pos = pygame.Rect(2950, 1920, 50, 50)#设置矩形位置，并赋值给spuar_pos
# square_pos = pygame.Rect(175, 75, 50, 50)  # 调整为居中坐标 (400-50)/2=175, (200-50)/2=75
# while True:#无限循环
#     if pygame.event.get(pygame.QUIT): break#获取退出信号，若收到则退出循环
#     screen.fill("black")#填充黑色
#     pygame.draw.rect(screen, "red", square_pos)#绘制矩形
#     pygame.display.flip()#更新屏幕
#     clock.tick(60)#设置帧率，每秒60帧
# pygame.quit()#退出pygame
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((1500, 900))
# clock = pygame.time.Clock()
# square_pos = pygame.Rect(750, 750, 50, 50)
# while True:
#     if pygame.event.get(pygame.QUIT): break
#     keys = pygame.key.get_pressed()#获取键盘上下左右的输入
#     if keys[pygame.K_UP]:
#         square_pos.y -= 20
#     if keys[pygame.K_DOWN]:
#         square_pos.y += 20
#     if keys[pygame.K_LEFT]:
#         square_pos.x -= 20
#     if keys[pygame.K_RIGHT]:
#         square_pos.x += 20
#     screen.fill("black")
#     pygame.draw.rect(screen, "red", square_pos)
#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((1500, 900))
# clock = pygame.time.Clock()
# square_pos = pygame.Rect(750, 750, 50, 50)
# # #circle_pos = pygame.Vector2(1500, 1500)#还是那个原因
# circle_pos = pygame.Vector2(750, 750)#修改小球的位置
# circle_spd = pygame.Vector2()
# circle_rad = 20
# circle_acc = 0.01
# circle_spd_mul = 0.99
# bounce_str = 1.0
# while True:
#     if pygame.event.get(pygame.QUIT): break
#     keys = pygame.key.get_pressed()#获取键盘上下左右的输入
#     if keys[pygame.K_UP]:
#         square_pos.y -= 20
#     if keys[pygame.K_DOWN]:
#         square_pos.y += 20
#     if keys[pygame.K_LEFT]:
#         square_pos.x -= 20
#     if keys[pygame.K_RIGHT]:
#         square_pos.x += 20
#     circle_spd *= circle_spd_mul
#     circle_spd += (yellow.get_pos()-circle_pos)*circle_acc
#     if circle_pos[0]<circle_rad:
#         circle_pos.update(circle_rad, circle_pos[1])
#         circle_spd.update(-circle_spd[0]*bounce_str, circle_spd[1])
#     elif circle_pos[0]>screen.get_width()-circle_rad:
#         circle_pos.update(screen.get_width()-circle_rad, circle_pos[1])
#         circle_spd.update(-circle_spd[0]*bounce_str, circle_spd[1])
#     elif circle_pos[1]<circle_rad:
#         circle_pos.update(circle_pos[0], circle_rad)
#         circle_spd.update(circle_spd[0], -circle_spd[1]*bounce_str)
#     elif circle_pos[1]>screen.get_height()-circle_rad:
#         circle_pos.update(circle_pos[0], screen.get_height()-circle_rad)
#         circle_spd.update(circle_spd[0], -circle_spd[1]*bounce_str)
#     circle_pos = circle_pos + circle_spd
#     screen.fill("black")
#     pygame.draw.circle(screen, "blue", circle_pos, circle_rad)
#     pygame.draw.rect(screen, "red", square_pos)
#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()
# fire(10)#前面写过，所以可以直接调用
# fire(5)
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((1500, 900))
# clock = pygame.time.Clock()
# square_pos = pygame.Rect(750, 750, 50, 50)
# # #circle_pos = pygame.Vector2(1500, 1500)#还是那个原因
# circle_pos = pygame.Vector2(750, 750)#修改小球的位置
# circle_spd = pygame.Vector2()
# circle_rad = 20
# circle_acc = 0.01
# circle_spd_mul = 0.99
# bounce_str = 1.0
# while True:
#     if pygame.event.get(pygame.QUIT): break
#     keys = pygame.key.get_pressed()#获取键盘上下左右的输入
#     if keys[pygame.K_UP]:
#         square_pos.y -= 20
#     if keys[pygame.K_DOWN]:
#         square_pos.y += 20
#     if keys[pygame.K_LEFT]:
#         square_pos.x -= 20
#     if keys[pygame.K_RIGHT]:
#         square_pos.x += 20
#     circle_spd *= circle_spd_mul
#     circle_spd += (yellow.get_pos()-circle_pos)*circle_acc
#     if circle_pos[0]<circle_rad:
#         circle_pos.update(circle_rad, circle_pos[1])
#         circle_spd.update(-circle_spd[0]*bounce_str, circle_spd[1])
#     elif circle_pos[0]>screen.get_width()-circle_rad:
#         circle_pos.update(screen.get_width()-circle_rad, circle_pos[1])
#         circle_spd.update(-circle_spd[0]*bounce_str, circle_spd[1])
#     elif circle_pos[1]<circle_rad:
#         circle_pos.update(circle_pos[0], circle_rad)
#         circle_spd.update(circle_spd[0], -circle_spd[1]*bounce_str)
#     elif circle_pos[1]>screen.get_height()-circle_rad:
#         circle_pos.update(circle_pos[0], screen.get_height()*circle_rad)#修改了这里的减号
#         circle_spd.update(circle_spd[0], -circle_spd[1]*bounce_str)
#     circle_pos = circle_pos + circle_spd
#     screen.fill("black")
#     pygame.draw.circle(screen, "blue", circle_pos, circle_rad)
#     pygame.draw.rect(screen, "red", square_pos)
#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()
# def fire(n, c=1):
#     if c>len(n):
#         return
#     print([ch for ch in n])
#     fire(n, c+1)
# fire(string.digits)#（重复了两遍）
# fire(string.ascii_letters)#ascii码是由美国国家标准化办制定的一种字符编码标准，它将文字符号（英文字母、阿拉伯数字、标点符号等）编码为二进制数，并使用计算机的存储和传输设备进行传输。
# def nuke(n):
#     a=[]
#     for i in range(10):
#         if(n>1):
#             a.append(nuke(n-1))
#         else:
#             a.append(i)
#     return a
# print(nuke(10))#该递归不要随便执行
#GGgggrrRRrRRr!R!!!#打闹的乱码
#hello?







