import pyautogui
import time


def main():
    time.sleep(3)
    position = pyautogui.position()
    print(position)
    pyautogui.click(position)


if __name__ == "__main__":
    main()
