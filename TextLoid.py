import tkinter
from tkinter import font
from tkinter import messagebox
import tkinter.ttk as ttk
import time
import win32gui
import json
import pyautogui
import pyperclip

root = tkinter.Tk()
root.geometry("400x300")
root.title(u"TextLoid")
root.iconbitmap('set/icon.ico')

font1 = font.Font(size=10, weight='bold')
label = tkinter.Label(root, text="ボイスロイドに台本を読み込ませ\n1行づつ生成するソフトです", font=font1)
label.pack(side="top")


class App1(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # ボイスロイドを選択
        with open('set/config.json', encoding="UTF-8") as f:
            config = json.load(f)
        self.ov = tkinter.StringVar()
        self.ov.set(config['start_win'])
        self.o = tkinter.OptionMenu(self, self.ov, *config['window'])
        self.o.pack()

        # 音声ファイルを生成する
        self.make = tkinter.Button(
            self, bg='#fd6767', fg='#ffffff', width=10, height=3)
        self.make["text"] = "保存"
        self.make["command"] = self.make_Func
        self.make.pack(side="bottom")

    def make_Func(self):
        window = self.ov.get()
        # コンフィグの呼び出し
        with open('set/config.json', encoding="UTF-8") as f:
            config = json.load(f)
        # ウィンドウの保存
        config['start_win'] = self.ov.get()
        with open('set/config.json', 'w', encoding='UTF-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        # ウィンドウの指定
        win = win32gui.FindWindow(None, window)
        win32gui.SetForegroundWindow(win)
        time.sleep(1)
        # 合成開始
        text = open(config['save_text'], 'r', encoding='UTF-8')
        while True:
            data = text.readline()
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
        if config["end_window"] == True:
            messagebox.showinfo('完了', '保存が完了しました')


app = App1(master=root)
app.mainloop()
