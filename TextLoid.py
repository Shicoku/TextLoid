import time
import json
import tkinter
import win32gui
import pyautogui
import pyperclip
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

root = tkinter.Tk()
root.geometry('400x300')
root.title(u'TextLoid')
root.iconbitmap('set/icon.ico')

with open('set/config.json', encoding='UTF-8') as f:
    config = json.load(f)


class App1(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # タブの設定
        self.note = ttk.Notebook(root)
        self.main = tkinter.Frame(self.note)
        self.setting = tkinter.Frame(self.note)
        self.note.add(self.main, text='メイン')
        self.note.add(self.setting, text='設定')

        # メインタブ
        self.val = tkinter.StringVar(value=config['start_win'])
        voice = tkinter.OptionMenu(self.main, self.val, *config['window'])
        voice.grid(row=0, column=0, padx=5, pady=10)

        self.make = ttk.Button(self.main)
        self.make['text'] = '保存'
        self.make['command'] = self.make_Func
        self.make.grid(row=0, column=1, pady=10)

        # 設定タブ
        self.val2 = tkinter.BooleanVar(value=config['end_window'])
        self.end_chk = ttk.Checkbutton(self.setting, variable=self.val2)
        self.end_chk['text'] = '生成完了後、終了ウィンドウを表示'
        self.end_chk['command'] = self.end_wind
        self.end_chk.grid(padx=5, pady=10)

        self.script_btn = ttk.Button(self.setting)
        self.script_btn['text'] = '台本を選択'
        self.script_btn['command'] = self.select_script
        self.script_btn.grid(padx=5, sticky=tkinter.W)

        self.defa = ttk.Button(self.setting)
        self.defa['text'] = '初期状態に戻す'
        self.defa['command'] = self.default
        self.defa.grid(padx=5, pady=30, sticky=tkinter.W)

        self.note.pack(expand=True, fill='both')

    def end_wind(self):
        config['end_window'] = self.val2.get()
        with open('set/config.json', 'w', encoding='UTF-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

    def select_script(self):
        fltype = [('テキストファイル', '*.txt')]
        dir = 'set/'
        config['save_text'] = filedialog.askopenfilename(
            filetypes=fltype, initialdir=dir)
        with open('set/config.json', 'w', encoding='UTF-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

    def default(self):
        config['end_window'] = True
        config['save_text'] = 'set/script.txt'
        with open('set/config.json', 'w', encoding='UTF-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

    def make_Func(self):
        window = self.val.get()
        config['start_win'] = window
        with open('set/config.json', 'w', encoding='UTF-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        win = win32gui.FindWindow(None, window)
        if win == 0:  # ウィンドウが見つからなければエラーログを出して処理を終了
            messagebox.showerror('エラー', 'ボイスロイドが起動されていないもしくは、名前が間違っています')
            return
        win32gui.SetForegroundWindow(win)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('del')
        time.sleep(0.5)
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
        if config['end_window'] == True:  # 設定でtrueになってれば生成完了後、確認ウィンドウを出す
            messagebox.showinfo('完了', '保存が完了しました')


app = App1(master=root)
app.mainloop()
