import tkinter
from tkinter import font
from tkinter import messagebox
import time
import win32gui
import json
import pyautogui
import pyperclip

root = tkinter.Tk()
root.geometry("400x300")
root.title(u"ボイスロイド テキスト複数生成プログラム")
root.iconbitmap('set/icon.ico')

font1 = font.Font(size=10, weight='bold')
label = tkinter.Label(root, text="ボイスロイドに台本を読み込ませ\n1行づつ生成するソフトです", font=font1)
label.pack(side="top")

txt = tkinter.Entry(width=40)
txt.pack(side="top")


class App1(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # ボイスロイドウィンドウ名を保存
        self.save = tkinter.Button(
            self, bg='#fd6767', fg='#ffffff', width=15, height=3)
        self.save["text"] = "ウィンドウ名を保存"  # ボタンのテキスト
        self.save["command"] = self.save_Func
        self.save.pack(side="top")

        # 音声ファイルを生成する
        self.make = tkinter.Button(
            self, bg='#fd6767', fg='#ffffff', width=10, height=3)
        self.make["text"] = "保存"  # ボタンのテキスト
        self.make["command"] = self.make_Func  # 割り込み関数
        self.make.pack(side="bottom")

    def make_Func(self):
        with open('set/config.json', encoding="UTF-8") as f:
            config = json.load(f)
        for window in config:
            window = window
        memoapp = win32gui.FindWindow(None, window)
        time.sleep(1)
        win32gui.SetForegroundWindow(memoapp)
        f = open('set/script.txt', 'r', encoding='UTF-8')
        while True:
            data = f.readline()
            if data == '':
                break
            pyperclip.copy(data.rstrip('\n'))
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            save = pyautogui.locateOnScreen('set/save.png', confidence=0.9)
            pyautogui.click(save)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.hotkey('enter')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('del')
        f.close()
        messagebox.showinfo('完了', 'テキスト生成が完了しました')

    def save_Func(self):
        config = {
            "window": txt.get()
        }
        with open('set/config.json', 'w', encoding='UTF-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)


app = App1(master=root)
app.mainloop()
