import datetime 

class TempMonitor: 
    def __init__(self,location="未知车间",operator="Admin", threshold=1000): 
        self.location=location  
        self.operator=operator 
        self.threshold=threshold
        self.history=[] 
        print(f"---{self.location}监控系统启动(操作员:{self.operator})---") 

    def convert_and_record(self,celsius): 
        fahrenheit=celsius*1.8+32 
        self.history.append(fahrenheit) 
        self.save_to_log(fahrenheit) 
        self.check_alarm(fahrenheit) 
        return fahrenheit  
    
    def check_alarm(self,fahrenheit): 
        if fahrenheit>self.threshold: 
            print(f"⚠️警告:{self.location}温度超过安全阀值！") 
            print(f">>>当前:{fahrenheit:.2f}F|限制：{self.threshold}F") 
            return True 
        return False 
    
    def save_to_log(self,fahrenheit): 
        time_stamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        with open("temperature_log.txt","a",encoding="utf-8")as file: 
            file.write(f"[{time_stamp}]设备:{self.location}|操作员：{self.operator}|记录:{fahrenheit:.2f}F\n") 

    def show_status(self): 
        if not self.history: 
            return 
        print(f"\n📊[{self.location}]实时统计：") 
        print(f"最高：{max(self.history):.2f}F|平均：{sum(self.history)/len(self.history):.2f}F") 


my_sensor=TempMonitor("一号高炉","Chuan",threshold=1000) 

while True: 
    u_input=input("\n请输入摄氏度(q退出):") 
    if u_input.lower()=='q': 
        break 

    try: 
        c=float(u_input) 
        f=my_sensor.convert_and_record(c) 
        print(f">>>当前转换：{f:.2f}F") 
        my_sensor.show_status() 
    except ValueError: 
        print("❌输入无效！")