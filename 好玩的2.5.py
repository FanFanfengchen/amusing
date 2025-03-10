import time  # 正确导入time模块

print("闭上眼睛，在心底进行观想")
time.sleep(2)

task_completed = False  # 标志变量，用于控制任务是否完成

while not task_completed:  # 外层循环，用于整个程序的重来机制
    print("想象你的手中的一个硬币：")
    a = input()  # 接收用户输入
    if a == "抛掷":  # 使用比较运算符比较输入内容
        print("你抛掷了一枚硬币")
        time.sleep(2)
        print("这枚硬币反向落入水中")
        time.sleep(1)
        print("产生涟漪")
        time.sleep(1.25)
        print("共振")
        time.sleep(1)
        print("扩散")
        time.sleep(1)
        print("交错")
        time.sleep(1)
        print("这便是意识与意识的交互")
        time.sleep(2.5)
        print("物质世界的背面")
        time.sleep(2)
        print("灵界的存在想象")
        time.sleep(3)
        print("这里是迪拉克之海")
        time.sleep(3)

        while not task_completed:  # 第一层循环，用于目标选择
            print("你的目标：")
            b = input()
            if b == "锚点":
                time.sleep(1.5)
                print("你已选中最近的锚点")
                time.sleep(2.5)
                print("你接触到了锚点")
                time.sleep(2)

                while not task_completed:  # 第二层循环，用于验证代码
                    print("请输入验证代码：")
                    c = input()
                    if c == "屈膝吧！":
                        time.sleep(0.3)
                        print("验证通过")
                        time.sleep(1)
                        print("恭迎您，陛下")  # 陪伴您最长久的灰发女巫，夏绿蒂
                        time.sleep(4)

                        while not task_completed:  # 第三层循环，用于验证关键词
                            print("验证关键词：")
                            d = input()
                            if d == "白维":
                                time.sleep(0.3)
                                print("验证通过，第一阶段解锁")
                                time.sleep(2)

                                while not task_completed:  # 第四层循环，用于验证关键词
                                    print("验证关键词：")
                                    e = input()
                                    if e == "黑色蔷薇":
                                        time.sleep(0.3)
                                        print("验证通过，第二阶段解锁")
                                        time.sleep(2)
                                        print("最终阶段即将展开")
                                        time.sleep(1.5)
                                        print(
                                            "警告：启用该权能碎片将会导致灵界海洋暴动，产生多次回响，后果难以预知"
                                        )
                                        time.sleep(2.5)
                                        print("如果执意发动权能，请通过最终验证")
                                        time.sleep(2.5)

                                        while not task_completed:  # 第五层循环，用于最终验证
                                            print("验证关键词：")
                                            f = input()
                                            if f == "再见了，夏绿蒂。" and "再见了，夏绿蒂":
                                                time.sleep(0.3)
                                                print("最终验证结束")
                                                time.sleep(1)
                                                print("黄金大权，权能展开")
                                                time.sleep(1.2)
                                                print("灵界海洋深处，传出无垠回响。")
                                                time.sleep(2.6)
                                                print("现实位面")
                                                time.sleep(2)
                                                print(
                                                    "你睁开双眼，眼瞳深处映照出黄金色的辉煌光芒"
                                                )
                                                time.sleep(3.5)
                                                print(
                                                    "你伫立于此，却如同端坐在黄金宫殿的恢弘王座之上"
                                                )
                                                time.sleep(3.7)
                                                print("仅有数息的时间，黄金大全在握")
                                                time.sleep(2.4)
                                                print("你仅抬起手")
                                                time.sleep(2)
                                                print("啪嗒~轻轻地打了个响指")
                                                time.sleep(1.8)
                                                print("召唤仪式99%......")
                                                time.sleep(1.2)
                                                print("中止......")
                                                time.sleep(3)
                                                print(
                                                    "水池中即将满溢而出的黑泥，悄无声息的在黄金色的辉光之中湮灭而去，洒落作遍地粉尘。"
                                                )
                                                time.sleep(5.6)
                                                print("结束开溜")
                                                task_completed = True  # 设置任务完成标志
                                            else:
                                                time.sleep(0.3)
                                                print("不对！")
                                                time.sleep(1)
                                                print("最终验证结束")
                                                time.sleep(1.5)
                                                print(
                                                    "深呼吸，好好回想陪您最长久的灰发女巫是谁。"
                                                )
                                                time.sleep(2.5)
                                                continue  # 返回到最终验证的if前重新开始
                                    else:
                                        time.sleep(0.3)
                                        print("验证失败，无法启动第二阶段的权能")
                                        time.sleep(2)
                                        print("别让黑色蔷薇失望啊！")
                                        time.sleep(3.6)
                                        print("我的陛下")
                                        time.sleep(2)
                                        continue  # 返回到第四层循环的if前重新开始
                            else:
                                time.sleep(0.3)
                                print("验证失败，无法启动第一阶段的权能")
                                time.sleep(2)
                                print("不会看了小凡就来验证了吧？")
                                time.sleep(2.5)
                                print("看看原作再来")
                                time.sleep(2.5)
                                continue  # 返回到第三层循环的if前重新开始
                    else:
                        time.sleep(0.3)
                        print("验证失败，你不是他")
                        time.sleep(2)
                        continue  # 返回到第二层循环的if前重新开始
            else:
                time.sleep(2)
                print("前往你的目的地")
                time.sleep(2)
                print("糟了，迪拉克之海好像有点大")
                time.sleep(2)
                print("再找找别的锚点吧！")
                time.sleep(1)
                continue  # 返回到第一层循环的if前重新开始
    else:
        time.sleep(2.3)
        print("达成成就：硬币呢？")
        time.sleep(2)
        print("抛掷吧！不要忘记开始")
        time.sleep(3)
        print("因为，还有重要之人需要保护。")
        time.sleep(1)
        continue  # 返回到外层循环的if前重新开始

# 如果用户成功完成任务，程序继续执行后续内容
time.sleep(4)
print("剑道场馆")
time.sleep(2)
print("哥......你刚刚去哪儿了？")
time.sleep(3)
print("人有三急。")
time.sleep(2)
print("可刚刚那不是厕所的方向啊。")
time.sleep(2)
print("我有说过我急的是这方面的吗？")
time.sleep(1.5)
print("......")
time.sleep(3)
print("好了，不逗你了")
time.sleep(1)
print("抬手一点妹妹的额头：")
time.sleep(2)
print("我要回去了。")
time.sleep(1)
print("这就走了？")
time.sleep(1.5)
print("没什么好看的，反而麻烦事不少，嗯，今晚我买菜下厨，记得早点回来。")
time.sleep(5)
print("噢噢......")
time.sleep(2)
print("柳生霜月懵懂地点头，旋即喊了声：")
time.sleep(2)
print("对了，哥，我......")
time.sleep(1)
print(
    "她突然想到刚刚感受到的奇怪的记忆，望着白维的背影，只感觉突然间那么的似曾相识，像是另一个人。"
)
g = input()
if g == "怎么了？" and "怎么了":
    time.sleep(1)
    print("唔，路上小心。")
time.sleep(2)
print("她还是没说出口。")
time.sleep(2)
print("好，那是得当心，霓虹的车是移动的穿越设备来着")
time.sleep(1.5)
print("你说着闲话走远了。")
time.sleep(3.5)
print("......不论如何，兄长就是兄长，其他的事不是那么重要......")
time.sleep(4)
print(
    "柳生霜月将多余的思绪抛下，这时再轻轻抚摸手腕，白皙的手腕上什么都没有，浮现的云纹也悄然消退。"
)
time.sleep(5)
