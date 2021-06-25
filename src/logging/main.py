# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import logging
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    data = [{"pin": 1, "test": 1}, {"pin": 1, "test": 1}]
    df = pd.DataFrame(data)
    print_hi("PyCharm")
    logger = logging.getLogger("LoggingTest")
    sh = logging.StreamHandler()
    logger.addHandler(sh)
    a = 2
    formatter = logging.Formatter("%(asctime)s:%(lineno)d:%(levelname)s:%(message)s")
    sh.setFormatter(formatter)
    logger.log(30, f"warning{a}")
    logger.log(30, data)
    logger.log(30, df)

    lst1=[1,2,3]
    lst2=[4,5,6]
    lst=lst1+lst2
    print(lst)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
