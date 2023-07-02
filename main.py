import multiprocessing
import os
import threading
import cv2
import numpy as np
import pyautogui
import tkinter as tk
from tkinter import ttk
import random
import time
import win32gui
import win32con


shared_switch = multiprocessing.Value('b', False)  # 创建共享整型变量
auto_hero_list = []
hero_list = []
#shared_lock = multiprocessing.Lock()  # 创建进程锁
class AutoClick:
    def __init__(self):
        self.hwnd1 = None
        self.hwnd2 = None

        self.coordinate_list = []

        #self.switch = True

    def start(self):

        m1 = multiprocessing.Process(target=self.execution, args=(shared_switch,), daemon=True)
        m1.start()
        #thread = threading.Thread(target=self.execution, daemon=True)
        # 获取目标窗口的句柄

        #self.hwnd2 = win32gui.FindWindow(None, 'League of Legends (TM) Client')
        # if self.hwnd1 or self.hwnd2 == 0:
        #     print("未找到窗口")
        #     return
        #thread.start()

    def execution(self, shared_switch):
        while True:
            while shared_switch.value:
                #self.hwnd1 = win32gui.FindWindow(None, 'GUI Demo')
                #print(f'自动购买：{self.auto_hero_list}')
                self.img_recognition()

    def img_recognition(self):                  #图像识别
        #pyautogui.screenshot().save('./screenshot.png')
        #img = cv2.imread('./screenshot.png')

        screenshot = pyautogui.screenshot()      #指定截取屏幕 即在选择下方棋子区域
        #win32gui.SetForegroundWindow(self.hwnd1)  #将作弊界面设置为前台窗口

        img = np.array(screenshot)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for img_path in self.hero_list:
            temp = cv2.imread(img_path, 0)
            res = cv2.matchTemplate(img_gray, temp, cv2.TM_CCORR_NORMED)
            threshold = 0.95
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):

                #win32gui.SetForegroundWindow(self.hwnd2) # 将游戏窗口设置为前台窗口
                # 模拟人的点击速度
                pyautogui.click(pt[0]+50, pt[1]-50)
                #time.sleep(0.06)
                #pyautogui.mouseDown(pt[0]+50, pt[1]-50)
                #time.sleep(0.06)
                #pyautogui.mouseUp(pt[0]+50, pt[1]-50)
                print('点击')

        #os.system('cls')

def read_file():
    with open('auto.ini', 'r', encoding='utf-8') as fp:
        name = fp.read().splitlines()


    for path_name in name:
        all_name = os.listdir('./hero')
        path_name = path_name + ".png"
        if path_name in all_name:
            hero_list.append('./hero/' + path_name)
            auto_hero_list.append(path_name.split('.')[0])
        else:
            pyautogui.alert(f'您填写的{path_name}不存在，跳过对{path_name}的自动购买！！')
            print(f'{path_name}不存在，请检查名称！')
            continue






def reset_combobox():
    combo1.set('')
    combo2.set('')
    entry.delete(0, 'end')

def change_Control():
    #global shared_switch
        shared_switch.value = not shared_switch.value
        if shared_switch.value:
            button['text'] = "停止选牌"
        else:
            button['text'] = "开始选牌"
def button_click():
    selected_item = combo1.get()
    selected_item1 = combo2.get()
    text = entry.get()
    if selected_item:
        label.config(text=f"你选中选择牌为: {selected_item}")
    elif selected_item1:
        label.config(text=f"你选中选择牌为: {selected_item1}")
    else:
        label.config(text=f"你选中选择牌为: {text}")
    #开始自动选牌任务

    change_Control()

#def set_foreground_window(window_title):

    # 将窗口设置为活动窗口
    #win32gui.SetActiveWindow(hwnd)

    # 将窗口设置为焦点窗口
    #win32gui.SetFocus(hwnd)
if __name__ == '__main__':

    #创建主窗口
    root = tk.Tk()
    #root.attributes('-fullscreen', True)
    # 设置窗口的背景色或透明度
    root.configure(background='white')  # 设置背景色为黑色

    root.attributes('-topmost', True)
    root.attributes("-alpha", 0.5)
    root.title("GUI Demo")
    root.geometry("450x260")

    # 创建3个用于说明的label
    label1 = ttk.Label(root, text="职业")
    label1.place(x=35, y=60,width=30)
    label2 = ttk.Label(root, text="特质")
    label2.place(x=35, y=130,width=30)
    label3 = ttk.Label(root, text="自定义英雄")
    label3.place(x=10, y=200,width=70)
    # 创建两个下拉框
    combo1 = ttk.Combobox(root,
                          values=["堡垒卫士", "格斗家", "挑战者", "亡眼射手", "枪手", "神谕者", "主宰", "术士",
                                  "潜行者", "裁决战士", "法师", "司令", "大发明家", "流浪法师", "女皇"], height=16)
    combo1.place(x=80,y=60)

    combo2 = ttk.Combobox(root,
                          values=["暗裔", "德玛西亚", "弗雷尔卓德", "艾欧尼亚", "诺克萨斯", "皮尔特沃夫", "涤魂圣枪",
                                  "暗影岛", "恕瑞玛", "巨神峰", "虚空", "约德尔人", "祖安"], height=13)
    combo2.place(x=80,y=130)

    # 创建输入框
    entry = ttk.Entry(root)
    entry.place(x=80,y=200)

    # 创建按钮
    button = ttk.Button(root, text="开始选牌", command=button_click)
    button.place(x=300,y=127)

    # 创建重置按钮
    reset_button = ttk.Button(root, text="重置数据", command=reset_combobox)
    reset_button.place(x=300, y=57)

    # 创建标签用于显示结果
    label = ttk.Label(root, text="")
    label.place(x=290,y=200)

    # 创建标签用于显示结果
    labelwarn = ttk.Label(root, text="提示：以下三个选择只能选一个，要么职业 要么特质 要么自定义英雄")
    labelwarn.place(x=37,y=10)

    # 设置窗口关闭事件
    #root.protocol("WM_DELETE_WINDOW", on_close)

    # 运行主循环
    auto = AutoClick()
    auto.start()
    root.mainloop()

    print("测试1")

