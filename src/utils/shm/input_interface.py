import PySimpleGUI as sg


class ShmooCheckGui:
    def __init__(self):
        self.failed_dut_count = 0
        self.dut_pin = {}
        pass

    def fail_dut_gui(self):
        layout_fail_dut_input = [
            [sg.Text("Failed Dut Count")],
            [sg.Text("Dut Count", size=(5, 1)), sg.InputText("", size=(5, 1))],
            [sg.Submit(button_text="send", size=(15, 1))],
        ]
        window = sg.Window("Shmoo Check", layout_fail_dut_input)

        while True:
            event, values = window.read()

            if event == "send":
                self.failed_dut_count = values[0]
                break

            if event is None:
                break

        window.close()

    def fail_dut_pin_gui(self):
        layout_fail_dut_pin_input = [
            [sg.Text("Python GUI")],
        ]

        for _ in range(int(self.failed_dut_count)):
            layout_fail_dut_pin_input.append(
                [
                    sg.Text("DUT", size=(5, 1)),
                    sg.InputText("", size=(5, 1)),
                    sg.Text("PIN", size=(5, 1)),
                    sg.InputText("", size=(5, 1)),
                ],
            )

        layout_fail_dut_pin_input.append([sg.Submit(button_text="send", size=(25, 1))])

        window = sg.Window("Shmoo Check", layout_fail_dut_pin_input)

        while True:
            event, values = window.read()

            if event == "send":
                for i in range(0, len(values), 2):
                    self.dut_pin[values[i]] = values[i + 1].split(",")
                break

            if event is None:
                break

        window.close()


shmoo_check_gui = ShmooCheckGui()
shmoo_check_gui.fail_dut_gui()
shmoo_check_gui.fail_dut_pin_gui()
print(shmoo_check_gui.dut_pin)
