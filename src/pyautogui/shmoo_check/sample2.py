import pygetwindow
import pyautogui
import datetime
import os
import sys

# from pynput import mouse

now = datetime.datetime.now()
date_now = now.strftime("%Y%m%d%H%M%S")

input_file = "./shmoo_list.txt"
output_path = "./" + date_now + "_shmoo_log/"
# shmoo_tool_name = "メモ A"
shmoo_tool_name = "テキストエディット sample"

# shmoo_tool_x, shmoo_tool_y, shmoo_tool_w, shmoo_tool_h = pygetwindow.getWindowGeometry(
#     shmoo_tool_name
# )
display_list = pygetwindow.getAllTitles()
print(display_list)

text_edit_list = [s for s in display_list if "テキストエディット" in s]
print(text_edit_list)

if len(text_edit_list) > 1:
    print("exit other shmoo tools!!")
    sys.exit()

shmoo_tool_geometry = pygetwindow.getWindowGeometry(text_edit_list[0])

shmoo_tool_x_button = (
    shmoo_tool_geometry[0] + shmoo_tool_geometry[2],
    shmoo_tool_geometry[1],
)
shmoo_tool_center = (
    shmoo_tool_geometry[0] + shmoo_tool_geometry[2] / 2,
    shmoo_tool_geometry[1] + shmoo_tool_geometry[3] / 2,
)
print(shmoo_tool_x_button)
pyautogui.moveTo(shmoo_tool_x_button)
sys.exit()


shmoo_list = []
dut_list = []
pin_list = []


def make_shmoo_list():
    """ read shmoo_list.txt and return the list of shmoo file name """
    shmoo_list = []
    with open(input_file, "r") as f:
        for line in f.read().splitlines():
            shmoo_list.append(line)

    return shmoo_list


def get_screenshot(shmoo_list, area):
    for i in range(len(shmoo_list)):
        screenshot = pyautogui.screenshot(region=area)
        screenshot.save(output_path + shmoo_list[i] + ".png")


def write_text(phrase, position):
    pyautogui.moveTo(position, duration=1)
    pyautogui.click()
    pyautogui.hotkey("command", "a")
    pyautogui.hotkey("delete")
    pyautogui.write(phrase)


shmoo_list = make_shmoo_list()
os.makedirs(output_path)
write_text("testtest", shmoo_tool_center)
get_screenshot(shmoo_list, shmoo_tool_geometry)
