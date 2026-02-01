import datetime 

print("--- 智能门禁系统 v2.0 ---") 

while True: 
    name=input("\n请输入访客姓名(输入'q'退出):") 
    if name.lower()=='q': 
        break 

    age_input=input(f"你好{name},请输入你的年龄：") 

    try: 
        age=int(age_input) 
        if age>=18: 
            status='已授权'  
            print(f"✅ {status},欢迎进入。") 

            with open("visitors.txt","a",encoding="utf-8")as file: 
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                file.write(f"时间：{now}|姓名：{name}|状态：{status}\n") 

        else: 
            print("❌ 未成年，禁止进入。") 
    except ValueError: 
        print("⚠️ 输入无效，请输入数字。") 

print("记录已保存至 visitors.txt，再见！") 

        