import datetime


# 1. 核心计算函数：只负责数学转换
def convert_to_fahrenheit(celsius):
    return celsius * 1.8 + 32


# 2. 数据持久化函数：只负责写硬盘
def save_to_log(fahrenheit):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("temperature_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{time_stamp}] 记录: {fahrenheit:.2f}F\n")


# 3. 统计展示函数：只负责屏幕输出
def show_report(history):
    if not history:
        print("目前尚无数据。")
        return

    print("-" * 25)
    print(f"📈 实时统计:")
    print(f"最高: {max(history):.2f}F")
    print(f"最低: {min(history):.2f}F")
    print(f"平均: {sum(history)/len(history):.2f}F")
    print("-" * 25)


# --- 主程序逻辑 ---
history_fahrenheit = []
print("--- 工业级温度监控系统启动 ---")

while True:
    u_input = input("\n请输入摄氏度 (q退出): ")
    if u_input.lower() == "q":
        break

    try:
        c = float(u_input)
        f = convert_to_fahrenheit(c)  # 调用函数1
        history_fahrenheit.append(f)

        save_to_log(f)  # 调用函数2
        print(f">>> 当前转换: {f:.2f}F")
        show_report(history_fahrenheit)  # 调用函数3

    except ValueError:
        print("❌ 输入无效！")
