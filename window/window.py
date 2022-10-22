import ctypes
from ctypes import wintypes
from collections import namedtuple
import os


def list_windows():
    user32 = ctypes.windll.user32
    WindowInfo = namedtuple('WindowInfo', 'pid title')
    WNDENUMPROC = ctypes.WINFUNCTYPE(
        wintypes.BOOL, wintypes.HWND, wintypes.LPARAM,)
    result = []

    def enum_proc(hWnd, lParam):
        if user32.IsWindowVisible(hWnd):
            pid = wintypes.DWORD()
            tid = user32.GetWindowThreadProcessId(hWnd, ctypes.byref(pid))
            length = user32.GetWindowTextLengthW(hWnd) + 1
            title = ctypes.create_unicode_buffer(length)
            user32.GetWindowTextW(hWnd, title, length)
            result.append([pid.value, title.value])
        return True
    user32.EnumWindows(WNDENUMPROC(enum_proc), 0)
    return sorted(result, key=lambda x: x[1])


if __name__ == '__main__':
    print('\n'.join(['{}, {}'.format(i, j) for i, j in list_windows()]))

os.system('PAUSE')
