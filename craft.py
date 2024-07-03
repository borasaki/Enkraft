import win32gui
import win32api
import win32con

def click(x, y):
    hWnd = win32gui.FindWindow(None, "LimbusCompany")
    coords = win32gui.GetWindowRect(hWnd)
    lParam = win32api.MAKELONG(x, y)

    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None) # Fourth parameter can also be window name
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)

click(30,30)