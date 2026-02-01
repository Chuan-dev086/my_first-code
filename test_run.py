while True:
    age_input=input ("请输入你的年龄（输入 'q' 退出）:")

    if age_input.lower()=='q': 
        print("程序已退出。") 
        break 

    try: 
        age=int(age_input) 
        if age>=18: 
             print("成年，允许进入。")  
        else:
            print("未成年，禁止进入。")  
    except ValueError: 
        print("⚠️ 输入错误！请输入纯数字。")  

print("--- 感谢使用 ---")

   
        