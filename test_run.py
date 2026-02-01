while True: 
    print("\n---新的访客---") 
    age_input=input 

    if age_input=='quit': 
        print("门禁系统关闭，再见！") 
        break 

    age_input=input("请输入你的年龄：")
    age= int(age_input) 
    if age >=18: 
        print("验证通过，请进。") 
    else: 
        print("未成年，禁止进入。") 
        