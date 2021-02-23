import pygetwindow
import pyautogui
import time


class ShmooCheck:
    def __init__(self):
        self.display_size = "maximize"
        self.display_name = ""
        self.file_name = ""
        self.dut_area = (100, 200)
        self.pin_area = (100, 400)
        self.dut_list = ["dut1", "dut2"]
        self.pin_list = ["pin1", "pin2"]
        self.geometry = 0
        self.maxmize_button = 0
        self.top_bar = 0
        self.get_display_name()
        self.get_geometry()
        self.set_top_bar()
        self.set_maximize_button()

    def start_capture(self):
        if self.display_size == "maximize":
            # pyautogui.moveTo(self.maxmize_button)
            # pyautogui.click()
            pyautogui.moveTo(self.top_bar)
            pyautogui.click()
            pyautogui.hotkey("ctrl", "option", "enter")
            self.get_geometry()
            pyautogui.click()

            self.get_screenshot_w_dut_pin()
            # self.write_dut_num()
            # time.sleep(1)
            # self.write_pin_num()
            # time.sleep(1)

            # self.get_screenshot()
            pyautogui.hotkey("ctrl", "option", "d")
            # pyautogui.keyDown("esc")
        else:
            pass

    def get_display_name(self):
        display_list = pygetwindow.getAllTitles()
        shmoo_tool_list = [s for s in display_list if "テキストエディット" in s]
        self.display_name = shmoo_tool_list[0]
        self.text_edit_geometry = pygetwindow.getWindowGeometry(shmoo_tool_list[0])

    def get_geometry(self):
        self.geometry = pygetwindow.getWindowGeometry(self.display_name)

    def set_top_bar(self):
        self.top_bar = (
            (self.geometry[0] + self.geometry[2] / 2) - 50,
            self.geometry[1] + 10,
        )

    def set_maximize_button(self):
        self.maxmize_button = (self.geometry[0] + 60, self.geometry[1] + 15)

    def get_screenshot(self):
        screenshot = pyautogui.screenshot(region=self.geometry)
        screenshot.save(self.file_name)

    def write_dut_num(self):
        pyautogui.moveTo(self.dut_area)
        pyautogui.click()
        pyautogui.write("dut1")

    def write_pin_num(self):
        pyautogui.moveTo(self.dut_area)
        pyautogui.click()
        pyautogui.write("pin1")

    def get_screenshot_w_dut_pin(self):
        for dut_index in range(len(self.dut_list)):
            for pin_index in range(len(self.pin_list)):
                pyautogui.moveTo(self.dut_area)
                pyautogui.click()
                pyautogui.hotkey("command", "a")
                time.sleep(0.5)
                # pyautogui.press("delete")
                # time.sleep(0.5)
                pyautogui.write(self.dut_list[dut_index])
                pyautogui.moveTo(self.pin_area)
                pyautogui.write(self.pin_list[pin_index])
                self.file_name = (
                    self.dut_list[dut_index] + self.pin_list[pin_index] + ".png"
                )
                self.get_screenshot()

        pyautogui.click()


shmoo = ShmooCheck()
shmoo.start_capture()
