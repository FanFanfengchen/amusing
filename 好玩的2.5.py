import time

a = b = c = d = e = f = ""


def print_speak(speak):
    for i in speak:
        print(i, flush=True, end='')
        time.sleep(0.27)
    print()


print_speak("闭上眼睛，在心底进行观想")
time.sleep(1)

task_completed = False  # 标志变量，用于控制任务是否完成

while not task_completed:  # 外层循环，用于整个程序的重来机制
    print_speak("想象你的手中的一个硬币：")

    while not task_completed:
        a = input().strip()  # 接收用户输入
        if a == "":
            continue
        else:
            break
    if a == "抛掷":  # 使用比较运算符比较输入内容
        time.sleep(0.8)
        print_speak("你向上抛掷了一枚硬币，这枚硬币飞至空中")
        time.sleep(0.75)
        print_speak("然后反向落入水中")
        time.sleep(0.75)
        print_speak("产生涟漪")
        time.sleep(0.7)
        print_speak("共振")
        time.sleep(0.7)
        print_speak("扩散")
        time.sleep(0.7)
        print_speak("交错")
        time.sleep(0.7)
        print_speak("这便是意识与意识的交互")
        time.sleep(1.3)
        print_speak("物质世界的背面")
        time.sleep(1.3)
        print_speak("灵界的存在想象")
        time.sleep(1.3)
        print_speak("这里是迪拉克之海")
        time.sleep(2)
        while not task_completed:  # 第一层循环，用于目标选择
            print_speak("请选择你的目标：")
            while not task_completed:
                b = input().strip()  # 接收用户输入
                if b == "":
                    continue
                else:
                    break
            if b == "锚点":
                time.sleep(1.3)
                print_speak("你已选中最近的锚点")
                time.sleep(1.8)
                print_speak("你接触到了锚点")
                time.sleep(2)

                while not task_completed:  # 第二层循环，用于验证代码
                    print_speak("身份验证...")
                    time.sleep(0.3)
                    print_speak("请输入验证代码：")
                    while not task_completed:
                        a = input().strip()  # 接收用户输入
                        if a == "":
                            continue
                        else:
                            break
                    if c == "屈膝吧！":
                        time.sleep(0.3)
                        print_speak("验证通过")
                        time.sleep(0.85)
                        print_speak("恭迎您，陛下")  # 陪伴您最长久的灰发女巫，夏绿蒂
                        time.sleep(3.2)

                        while not task_completed:  # 第三层循环，用于验证关键词
                            print_speak("第一阶段验证...")
                            time.sleep(0.3)
                            print_speak("验证关键词：")
                            d = input()
                            if d == "白维":
                                time.sleep(0.3)
                                print_speak("验证通过，第一阶段解锁")
                                time.sleep(2)

                                while not task_completed:  # 第四层循环，用于验证关键词
                                    print_speak("第二阶段验证...")
                                    time.sleep(0.3)
                                    print_speak("验证关键词：")
                                    e = input()
                                    if e == "黑色蔷薇":
                                        time.sleep(0.3)
                                        print_speak("验证通过，第二阶段解锁")
                                        time.sleep(2)
                                        print_speak("最终阶段即将展开")
                                        time.sleep(1.5)
                                        print_speak("警告：启用该权能碎片将会导致灵界海洋暴动，产生多次回响，后果难以预知")
                                        time.sleep(2.5)
                                        print_speak("如果执意发动权能，请通过最终验证")
                                        time.sleep(2.5)
                                        while not task_completed:  # 第五层循环，用于最终验证
                                            print_speak("最终验证...")
                                            time.sleep(0.3)
                                            print_speak("验证关键词：")
                                            f = input()
                                            if f == "再见了，夏绿蒂。" and "再见了，夏绿蒂":
                                                time.sleep(0.3)
                                                print_speak("最终验证结束")
                                                time.sleep(1)
                                                print_speak("黄金大权，权能展开")
                                                time.sleep(1.2)
                                                print_speak("灵界海洋深处，传出无垠回响。")
                                                time.sleep(2.4)
                                                print_speak("现实位面")
                                                time.sleep(1)
                                                print_speak("你睁开双眼，眼瞳深处映照出黄金色的辉煌光芒")
                                                time.sleep(3.5)
                                                print_speak("你伫立于此，却如同端坐在黄金宫殿的恢弘王座之上")
                                                time.sleep(3.7)
                                                print_speak("仅有数息的时间，黄金大全在握")
                                                time.sleep(2.4)
                                                print_speak("你仅抬起手")
                                                time.sleep(2)
                                                print_speak("啪嗒~轻轻地打了个响指")
                                                time.sleep(1.8)
                                                print_speak("召唤仪式99%......")
                                                time.sleep(1.2)
                                                print_speak("中止......")
                                                time.sleep(2.35)
                                                print_speak("水池中即将满溢而出的黑泥，悄无声息的在黄金色的辉光之中湮灭而去，洒落作遍地粉尘。")
                                                time.sleep(3.5)
                                                print_speak("结束开溜")
                                                task_completed = True  # 设置任务完成标志
                                            else:
                                                time.sleep(0.3)
                                                print_speak("不对！")
                                                time.sleep(1)
                                                print_speak("最终验证结束")
                                                time.sleep(1.5)
                                                print_speak("深呼吸，好好回想陪您最长久的灰发女巫是谁。")
                                                time.sleep(2.5)
                                                continue  # 返回到最终验证的if前重新开始
                                    else:
                                        time.sleep(0.3)
                                        print_speak("验证失败，无法启动第二阶段的权能")
                                        time.sleep(2)
                                        print_speak("别让黑色蔷薇失望啊！")
                                        time.sleep(3.6)
                                        print_speak("我的陛下")
                                        time.sleep(2)
                                        continue  # 返回到第四层循环的if前重新开始
                            else:
                                time.sleep(0.3)
                                print_speak("验证失败，无法启动第一阶段的权能")
                                time.sleep(2)
                                print_speak("不会看了小凡就来验证了吧？")
                                time.sleep(2.5)
                                print_speak("看看原作再来")
                                time.sleep(2.5)
                                continue  # 返回到第三层循环的if前重新开始
                    else:
                        time.sleep(0.3)
                        print_speak("验证失败，你不是他")
                        time.sleep(1)
                        continue  # 返回到第二层循环的if前重新开始
            else:
                time.sleep(2)
                print_speak("前往你的目的地")
                time.sleep(2)
                print_speak("糟了，迪拉克之海好像有点大")
                time.sleep(2)
                print_speak("再找找别的锚点吧！")
                time.sleep(1)
                continue  # 返回到第一层循环的if前重新开始
    else:
        time.sleep(1.8)
        print_speak("达成成就：硬币呢？")
        time.sleep(3)
        print_speak("抛掷吧！不要忘记开始")
        time.sleep(3.2)
        print_speak("因为，还有重要之人需要保护。")
        time.sleep(1)
        continue  # 返回到外层循环的if前重新开始

# 如果用户成功完成任务，程序继续执行后续内容
time.sleep(2)
print_speak("另一边...")
print_speak("剑道场馆")
time.sleep(1.75)
print_speak("哥......你刚刚去哪儿了？")
time.sleep(1.4)
print_speak("人有三急。")
time.sleep(0.95)
print_speak("可刚刚那不是厕所的方向啊。")
time.sleep(1.2)
print_speak("我有说过我急的是这方面的吗？")
time.sleep(1)
print_speak("......")
time.sleep(3)
print_speak("好了，不逗你了")
time.sleep(0.89)
print_speak("抬手一点妹妹的额头：")
time.sleep(1.2)
print_speak("我要回去了。")
time.sleep(1)
print_speak("这就走了？")
time.sleep(1.5)
print_speak("没什么好看的，反而麻烦事不少，嗯，今晚我买菜下厨，记得早点回来。")
time.sleep(4.6)
print_speak("噢噢......")
time.sleep(1.23)
print_speak("柳生霜月懵懂地点头，旋即喊了声：")
time.sleep(2.2)
print_speak("对了，哥，我......")
time.sleep(1)
print_speak("她突然想到刚刚感受到的奇怪的记忆，望着白维的背影，只感觉突然间那么的似曾相识，像是另一个人。")
g = input("（请按回车：）")
if g == "怎么了？" or "怎么了":
    time.sleep(0.68)
    print_speak("唔，路上小心。")
time.sleep(1.67)
print_speak("她还是没说出口。")
time.sleep(1.85)
print_speak("“好，那是得当心，霓虹的车是移动的穿越设备来着”")
time.sleep(1)
print_speak("你说着闲话走远了。")
time.sleep(2.5)
print_speak("......不论如何，兄长就是兄长，其他的事不是那么重要......")
time.sleep(3)
print_speak("柳生霜月将多余的思绪抛下，这时再轻轻抚摸手腕，白皙的手腕上什么都没有，浮现的云纹也悄然消退。")
time.sleep(5)

