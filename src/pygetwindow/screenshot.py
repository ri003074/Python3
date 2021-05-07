import pygetwindow
import win32gui
import pyautogui

print(pygetwindow.getAllTitles())

hnd = win32gui.FindWindow(None, "a - メモ帳")
print(hnd)
x0, y0, x1, y1 = win32gui.GetWindowRect(hnd)
area = win32gui.GetWindowRect(hnd)
# area2 = pygetwindow.getWindowGeometry("a - メモ帳")
print(x0)
print(y0)
print(x1)
print(y1)
print(area)
# print(area2)

area = (x0 + 7, y0, x1 - x0 - 17, y1 - y0 - 7)

screenshot = pyautogui.screenshot(region=area)
screenshot.save("a.png")
