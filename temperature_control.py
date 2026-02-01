print("---工业温度监控系统已启动---")
print("提示：输入数字进行转换，输入'q'退出程序")

history_fahrenheit = []

while True:
    user_input = input("\n[等待输入]请输入摄氏度：")

    if user_input.lower() == "q":
        if len(history_fahrenheit) > 0:
            print("\n" + "=" * 20)
            print(f"今日运行结束。共记录数据：{len(history_fahrenheit)}条")
            print(f"最高华氏度：{max(history_fahrenheit)}F")
            print(f"最低华氏度：{min(history_fahrenheit)}F")
            print(f"平均华氏度：{sum(history_fahrenheit)/len(history_fahrenheit)}F")
            print("=" * 20)
        else:
            print("未记录到任何有效数据。")
        break

    try:
        celsius = float(user_input)
        fahrenheit = celsius * 1.8 + 32
        print(f">>>转换结果：{fahrenheit}F")

        if fahrenheit >= 212:
            print("[报警]:检测到沸腾状态！")

        else:
            print("[状态]:稳定")

    except ValueError:
        print("[错误]：无效输入！请输入有效数值或'q'。")
