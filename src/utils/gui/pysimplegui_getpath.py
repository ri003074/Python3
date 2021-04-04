import PySimpleGUI as sg


# class GetPath:
#     def __init__(self):
#         sg.theme("Dark Blue 3")

#         layout = [[sg.Text("Python GUI")], [sg.Text("Select Dir:"), sg.FolderBrowse()]]

#         window = sg.Window("Get Path GUI", layout, size=(300, 200))

#         while True:
#             event, values = window.read()

#             if event is None:
#                 break

#         window.close()


# aaa = GetPath()


sg.theme("DarkTeal2")
layout = [
    [sg.T("")],
    # [sg.T("folder: "), sg.Text(size=(15, 1), key="-IN2-", enable_events=True)],
    [
        sg.Text("Choose a folder: "),
        sg.Input(key="-IN2-", change_submits=True),
        sg.FolderBrowse(key="-IN-", button_text="browse"),
    ],
    [sg.Button("Submit")],
]

###Building Window
window = sg.Window("My File Browser", layout, size=(600, 150))

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])
        window["-IN2-"].update(values["-IN-"])
