temp_in_text = input("请输入当前的摄氏度：")
celsius = float(temp_in_text)
fahrenheit = celsius * 1.8 + 32

print("转换后的华氏度为：", fahrenheit)
if fahrenheit >= 212:
    print("警告：水已经沸腾了！")
    print("请检查压力阀。")

else:
    print("系统运行正常")
