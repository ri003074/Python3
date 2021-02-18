import pyautogui
import time

# print(pyautogui.position())
# print(pyautogui.size())
# pyautogui.click(x=2500, y=1000, duration=1)
# pyautogui.screenshot("sample.png")
# pyautogui.screenshot("sample2.png", region=(0, 200, 300, 300))

pyautogui.click(x=3773, y=12)
pyautogui.write("finder", 0.3)
time.sleep(0.8)
pyautogui.hotkey("return")
