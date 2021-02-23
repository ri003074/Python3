import pygetwindow
import pyautogui
import time

display_list = pygetwindow.getAllTitles()
print(display_list)
text_edit_list = [s for s in display_list if "テキストエディット" in s]
print(text_edit_list)

text_edit_geometry = pygetwindow.getWindowGeometry(text_edit_list[0])
print(text_edit_geometry)

text_edit_top_bar = (
    (text_edit_geometry[0] + text_edit_geometry[2] / 2) - 50,
    text_edit_geometry[1] + 10,
)

pyautogui.moveTo(text_edit_top_bar, duration=0.5)
time.sleep(1)
pyautogui.click()
pyautogui.hotkey("ctrl", "option", "d")
