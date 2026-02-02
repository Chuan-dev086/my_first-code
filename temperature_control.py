print("---工业温度监控系统已启动---")
print("提示：输入数字进行转换，输入'q'退出程序")

history_fahrenheit = []

while True: 
    user_input=input("请输入摄氏度 (输入 'q' 退出):") 
    if user_input.lower()=='q':
        break 

    try: 
        celsius=float(user_input) 
        fahrenheit=celsius*1.8+32 
        history_fahrenheit.append(fahrenheit) 

        current_max=max(history_fahrenheit) 
        current_min=min(history_fahrenheit) 
        current_avg=sum(history_fahrenheit)/len(history_fahrenheit) 

        print(f"✅ 转换结果: {fahrenheit:.2f}F") 
        print(f"📊 实时播报 -> 最高: {current_max:.2f}F | 最低: {current_min:.2f}F | 平均: {current_avg:.2f}F")
        print(f"📈 已记录数据点: {len(history_fahrenheit)} 个") 

    except ValueError: 
        print("❌ 输入无效，请输入数字。") 
        