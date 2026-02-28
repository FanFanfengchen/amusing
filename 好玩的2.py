import sys
import time

a = b = c = d = e = f = ""
task_completed = False  # 标志变量，用于控制任务是否完成


def print_speak(speak):
    for i in speak:
        print(i, flush=True, end='')
        time.sleep(0.27)
    print()


def print_speak_method(sp, ti):
    print_speak(sp)
    time.sleep(ti)


# def continue_or_break(name):
#     name = input().strip()  # 接收用户输入
#     if name == "":
#         continue
#     else:
#         break


def toss():
    time.sleep(0.8)
    print_speak_method("你向上抛掷了一枚硬币，这枚硬币飞至空中", 0.75)
    print_speak_method("然后反向落入水中", 0.75)
    print_speak_method("产生涟漪", 0.7)
    print_speak_method("共振", 0.7)
    print_speak_method("扩散", 0.7)
    print_speak_method("交错", 0.7)
    print_speak_method("这便是意识与意识的交互", 1.3)
    print_speak_method("物质世界的背面", 1.3)
    print_speak_method("灵界的存在想象", 1.3)
    print_speak_method("这里是迪拉克之海", 2)


def anchor_point():
    time.sleep(1.3)
    print_speak_method("你已选中最近的锚点", 1.8)
    print_speak_method("你接触到了锚点", 2)


def bend_your_knees():
    time.sleep(0.3)
    print_speak_method("验证通过", 0.85)
    print_speak_method("恭迎您，陛下", 3.2)  # 陪伴您最长久的灰发女巫，夏绿蒂


def baiwei():
    time.sleep(0.3)
    print_speak_method("验证通过，第一阶段解锁", 2)


def black_rose():
    time.sleep(0.3)
    print_speak_method("验证通过，第二阶段解锁", 2)
    print_speak_method("最终阶段即将展开", 1.5)
    print_speak_method("警告：启用该权能碎片将会导致灵界海洋暴动，产生多次回响，后果难以预知", 2.5)
    print_speak_method("如果执意发动权能，请通过最终验证", 2.5)


def goodbye_charlotte():
    time.sleep(0.3)
    print_speak_method("最终验证结束", 1)
    print_speak_method("黄金大权，权能展开", 1.2)
    print_speak_method("灵界海洋深处，传出无垠回响。", 2.4)
    print_speak_method("现实位面", 1)
    print_speak_method("你睁开双眼，眼瞳深处映照出黄金色的辉煌光芒", 3.5)
    print_speak_method("你伫立于此，却如同端坐在黄金宫殿的恢弘王座之上", 3.7)
    print_speak_method("仅有数息的时间，黄金大全在握", 2.4)
    print_speak_method("你仅抬起手", 2)
    print_speak_method("啪嗒~轻轻地打了个响指", 1.8)
    print_speak_method("召唤仪式99%......", 1.2)
    print_speak_method("中止......", 2.35)
    print_speak_method("水池中即将满溢而出的黑泥，悄无声息的在黄金色的辉光之中湮灭而去，洒落作遍地粉尘。", 3.5)
    print_speak_method("结束开溜", 1)


def goodbye_charlotte_badend():
    time.sleep(0.3)
    print_speak_method("不对！", 1)
    print_speak_method("最终验证结束", 1.5)
    print_speak_method("深呼吸，好好回想陪您最长久的灰发女巫是谁。", 2.5)


def black_rose_badend():
    time.sleep(0.3)
    print_speak_method("验证失败，无法启动第二阶段的权能", 2)
    print_speak_method("别让黑色蔷薇失望啊！", 3.6)
    print_speak_method("我的陛下", 2)


def baiwei_badend():
    time.sleep(0.3)
    print_speak_method("验证失败，无法启动第一阶段的权能", 2)
    print_speak_method("不会看了小凡就来验证了吧？", 2.5)
    print_speak_method("看看原作再来", 2.5)


def bend_your_knees_badend():
    time.sleep(0.3)
    print_speak_method("验证失败，你不是他", 1)


def anchor_point_badend():
    time.sleep(2)
    print_speak_method("前往你的目的地", 2)
    print_speak_method("糟了，迪拉克之海好像有点大", 2)
    print_speak_method("再找找别的锚点吧！", 1)


def toss_badend():
    time.sleep(1.8)
    print_speak_method("达成成就：硬币呢？", 3)
    print_speak_method("抛掷吧！不要忘记开始", 3.2)
    print_speak_method("因为，还有重要之人需要保护。", 1)


start = input("你是否准备好了？\n").strip()  # 接收用户输入
if start == "开始吧":
    pass
else:
    sys.exit()

print_speak_method("闭上眼睛，在心底进行观想", 1)

while not task_completed:  # 外层循环，用于整个程序的重来机制
    print_speak("想象你的手中的一个硬币：")

    while not task_completed:
        a = input().strip()  # 接收用户输入
        if a == "":
            continue
        else:
            break
    if a == "抛掷":  # 使用比较运算符比较输入内容
        toss()
        while not task_completed:  # 第一层循环，用于目标选择
            print_speak("请选择你的目标：")
            while not task_completed:
                b = input().strip()  # 接收用户输入
                if b == "":
                    continue
                else:
                    break
            if b == "锚点":
                anchor_point()
                while not task_completed:  # 第二层循环，用于验证代码
                    print_speak_method("身份验证...", 0.3)
                    print_speak("请输入验证代码：")
                    while not task_completed:
                        c = input().strip()  # 接收用户输入
                        if c == "":
                            continue
                        else:
                            break
                    if c == "屈膝吧！":
                        bend_your_knees()
                        while not task_completed:  # 第三层循环，用于验证关键词
                            print_speak_method("第一阶段验证...", 0.3)
                            print_speak("验证关键词：")
                            while not task_completed:
                                d = input().strip()  # 接收用户输入
                                if d == "":
                                    continue
                                else:
                                    break
                            if d == "白维":
                                baiwei()
                                while not task_completed:  # 第四层循环，用于验证关键词
                                    print_speak_method("第二阶段验证...", 0.3)
                                    print_speak("验证关键词：")
                                    while not task_completed:
                                        e = input().strip()  # 接收用户输入
                                        if e == "":
                                            continue
                                        else:
                                            break
                                    if e == "黑色蔷薇":
                                        black_rose()
                                        while not task_completed:  # 第五层循环，用于最终验证
                                            print_speak_method("最终验证...", 0.3)
                                            print_speak("验证关键词：")
                                            while not task_completed:
                                                f = input().strip()  # 接收用户输入
                                                if f == "":
                                                    continue
                                                else:
                                                    break
                                            if f == "再见了，夏绿蒂。" and "再见了，夏绿蒂":
                                                goodbye_charlotte()
                                                task_completed = True  # 设置任务完成标志
                                            else:
                                                goodbye_charlotte_badend()
                                                continue  # 返回到最终验证的if前重新开始
                                    else:
                                        black_rose_badend()
                                        continue  # 返回到第四层循环的if前重新开始
                            else:
                                black_rose_badend()
                                continue  # 返回到第三层循环的if前重新开始
                    else:
                        bend_your_knees_badend()
                        continue  # 返回到第二层循环的if前重新开始
            else:
                anchor_point_badend()
                continue  # 返回到第一层循环的if前重新开始
    else:
        toss_badend()
        continue  # 返回到外层循环的if前重新开始
# 如果用户成功完成任务，程序继续执行后续内容
time.sleep(2)
print_speak("另一边...")
print_speak_method("剑道场馆", 1.75)
print_speak_method("哥......你刚刚去哪儿了？", 1.4)
print_speak_method("人有三急。", 0.95)
print_speak_method("可刚刚那不是厕所的方向啊。", 1.2)
print_speak_method("我有说过我急的是这方面的吗？", 1)
print_speak_method("......", 3)
print_speak_method("好了，不逗你了", 0.89)
print_speak_method("抬手一点妹妹的额头：", 1.2)
print_speak_method("我要回去了。", 1)
print_speak_method("这就走了？", 1.5)
print_speak_method("没什么好看的，反而麻烦事不少，嗯，今晚我买菜下厨，记得早点回来。", 4.6)
print_speak_method("噢噢......", 1.23)
print_speak_method("柳生霜月懵懂地点头，旋即喊了声：", 2.2)
print_speak_method("对了，哥，我......", 1)
print_speak_method("她突然想到刚刚感受到的奇怪的记忆，望着白维的背影，只感觉突然间那么的似曾相识，像是另一个人。", 1.5)
g = input("（请按回车：）").strip()
if g == "怎么了？" or g == "怎么了":
    time.sleep(0.68)
    print_speak("唔，路上小心。")
time.sleep(1.67)
print_speak_method("她还是没说出口。", 1.85)
print_speak_method("“好，那是得当心，霓虹的车是移动的穿越设备来着”", 1)
print_speak_method("你说着闲话走远了。", 2.5)
print_speak_method("......不论如何，兄长就是兄长，其他的事不是那么重要......", 3)
print_speak_method("柳生霜月将多余的思绪抛下，这时再轻轻抚摸手腕，白皙的手腕上什么都没有，浮现的云纹也悄然消退。", 5)
