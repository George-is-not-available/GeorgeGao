import tkinter as tk
from tkinter import messagebox
import random


class CarSelectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Car Selection ")

        # 定义车辆列表
        self.cars = ["SpiderPi", "Jet tank", "Jet Hexa", "JetRover", "SpiderPi-3C"]

        # 创建变量用于存储选中的车辆
        self.selected_car = tk.StringVar()

        # 创建界面元素
        self.create_widgets()

    def create_widgets(self):
        # 创建标签
        label = tk.Label(self.master, text="请选择一辆车:")
        label.pack(pady=10)

        # 创建车辆选择框
        for car in self.cars:
            radio_button = tk.Radiobutton(self.master, text=car, variable=self.selected_car, value=car)
            radio_button.pack()

        # 创建确认按钮
        confirm_button = tk.Button(self.master, text="随机选择", command=self.random_selection)
        confirm_button.pack(pady=10)

    def random_selection(self):
        # 随机选择一辆车（不重复）
        if self.cars:
            selected_car = random.sample(self.cars, 1)[0]
            self.cars.remove(selected_car)  # 从列表中移除已选择的车辆
            messagebox.showinfo("选择结果", f"系统为您随机选择了：{selected_car}")
        else:
            messagebox.showwarning("警告", "所有车辆已经被选择完毕")


if __name__ == "__main__":
    root = tk.Tk()
    app = CarSelectionApp(root)
    root.mainloop()
