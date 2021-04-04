import PySimpleGUI as sg


class GetPath:
    def __init__(self):
        self.dir_path = ""
        sg.theme("Dark Blue 3")

        layout = [
            [sg.Text("Python GUI")],
            [
                sg.Text("Choose a folder: "),
                sg.Input(key="-IN2-", change_submits=True, size=(65, 5)),
                sg.FolderBrowse(key="-IN-", button_text="browse", size=(6, 1)),
                sg.Button("exec", size=(6, 1)),
            ],
        ]

        window = sg.Window("Get Path GUI", layout, size=(650, 80))

        while True:
            event, values = window.read()

            if event is None:
                break

            if event == "exec":
                self.dir_path = values["-IN-"]
                break

        window.close()


get_dir_path = GetPath()
print(get_dir_path.dir_path)
