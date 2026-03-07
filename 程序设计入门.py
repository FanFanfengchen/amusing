# **任务一 编写猜数字的游戏程序**
# ·步骤1->给定要猜的数字是8，让别人猜
print("猜数字小游戏")
num = input("不妨猜一下我现在心里想的是哪一个数字：")
guess = int(num)  # 将输入的字符串转换为整数
# 进行判断猜测是否正确
if guess == 8:
    print("你是我心里的蛔虫么？猜得这么准！")
else:
    print("猜错啦，我现在心里想的是8！")
print("游戏结束，不玩啦！")
# ·步骤2->增加猜测答案提示
guess = int(num)
secret = 8
if guess == secret:
    print("哎呀，你真厉害，被你猜中了！")
else:
    # 猜错时，提示猜大了还是猜小了
    if guess > secret:
        print("你猜大了哦")
    else:
        print("你猜小了哦")
# ·步骤3->提供多次机会给用户猜测
num = input("猜猜我现在心里想的是哪一个数字？")
guess = int(num)
secret = 8
# 循环判断猜测是否正确
while guess != secret:
    if guess > secret:
        print("你猜大了哦")
    else:
        print("你猜小了哦")
    num = input("请再试一次吧！")  # 再次提示用户输入下一个猜测，否则·你试试
    guess = int(num)
print("哎呀，你真厉害，被你猜中了！")
# ·步骤4->游戏的答案是随机
import random  # 导入random模块，用于生成随机数

secret = random.randint(1, 10)  # 设定随机数生成的范围为1到10
num = input("猜猜我现在心里想的是哪个数字？")
guess = int(num)
times = 1
while guess != secret and times < 3:
    if guess > secret:
        print("你猜大了哦")
    else:
        print("你猜小了哦")
    num = input("请再试一次吧！")
    guess = int(num)
    times = times + 1
if times < 3 and guess == secret:
    print("哎呀，你真厉害，被你猜中了！")
else:
    print("给你三次机会都猜不中，不跟你玩了！")
# ·铁路托运行李时，根据行李重量按一定标准收费
x = float(input('请输入行李重量:'))  # 输入行李重量，转换为浮点数。以免出现整数相除的情况（？）
y = 0
if x > 150:
    print('行李超重！')
else:
    if x > 50:
        y = 0.5 * x  # 好像与原题有出处，好吧，去掉好像，既然知道了就不做更改了，反正是文字游戏
    else:
        y = 0.35 * x
print('行李总费用为：', y, '元')
# **任务二 身份证信息识别**
# ·步骤1->分析编写策略
# 生肖列表特点：年份除以12的余数为列表的索引号
sheng_xiao = ["猴", "鸡", "狗", "猪", "鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊"]  # 因为会出现下标位置错位的情况，所以从“猴”开始
id = input("请输入18位身份证号码：")
y = id[6:10]  # 读取年份，身份证中7~10
m = id[10:12]  # 读取月份，身份证中11~12
d = id[12:14]  # 读取日期，身份证中13~14
print("您的生日为：", y, "年", m, "月", d, "日")
sx = int(y) % 12  # 计算生肖的下标
print("属", sheng_xiao[sx])  # 字符串格式化的一种
# **任务三 统计学生成绩**
# ·题目描述，输入身份证号码，输出出生年月、年龄和生肖
# ·题目描述：求6位同学成绩的最高分、最低分、平均分
# ·键盘输入6位同学成绩，输出最高分、最低分、平均分
cj = []  # 成绩列表初始为空
v = eval(input("请输入第1位同学的成绩："))  # 输入学生成绩
cj.append(v)  # 将成绩添加到cj列表中
v = eval(input("请输入第2位同学的成绩："))
cj.append(v)
v = eval(input("请输入第3位同学的成绩："))
cj.append(v)
v = eval(input("请输入第4位同学的成绩："))
cj.append(v)
v = eval(input("请输入第5位同学的成绩："))
cj.append(v)
v = eval(input("请输入第6位同学的成绩："))
cj.append(v)
print("6位同学成绩为：", cj)
print("最高分：", max(cj))  # max()求列表最大值
print("最低分：", min(cj))  # min()求列表最小值
avg = sum(cj) / 6  # 先sum()求列表总和，再算平均
print("平均分：", avg)
# **任务四 简单爬取网络图片**（学明白了可以去玩爬虫了）
import os
import requests

# import json

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件
herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x: x['cname'], herolist.json()))
# 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], herolist.json()))  # 提取英雄的编号


# 定义下载图片的函数方法
def downloadPic():
    i = 0
    for j in hero_number:
        # 创建文件夹
        os.mkdir(r"D:\软件\pycharm\英雄\\" + hero_name[i])
        # 进入创建好的文件夹
        os.chdir(r"D:\软件\pycharm\英雄\\" + hero_name[i])
        i += 1
        for k in range(10):  # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)


# 写入文件
downloadPic()
# 完结散花