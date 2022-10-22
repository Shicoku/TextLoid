import time
import json
import tkinter
import win32gui
import pyautogui
import pyperclip
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("400x300")
root.title(u"TextLoid")
root.iconbitmap('set/icon.ico')


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
        self.o.pack(pady=10)

        # 音声ファイルを生成する
        self.make = tkinter.Button(
            self, bg='#fd6767', fg='#ffffff', width=7, height=2)
        self.make["text"] = "保存"
        self.make["command"] = self.make_Func
        self.make.pack()

    # 生成
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
        if win == 0:
            messagebox.showerror('エラー', 'ボイスロイドが起動されていないもしくは、名前が間違っています')
            return
        win32gui.SetForegroundWindow(win)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('del')
        time.sleep(0.5)
        # 合成開始
        text = open(config['save_text'], 'r', encoding='UTF-8')
        while True:
            data = text.readline()
            if data == '':
                break
            pyperclip.copy(data.rstrip('\n'))
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            save = pyautogui.locateOnScreen('set/save.png', confidence=0.9)
            pyautogui.click(save)
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            pyautogui.hotkey('enter')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('del')
        f.close()
        if config["end_window"] == True:
            messagebox.showinfo('完了', '保存が完了しました')


app = App1(master=root)
app.mainloop()
