import PySimpleGUI as sg

left_side_picture_path = ""

sg.theme("DarkTeal2")
layout = [
    [sg.T("")],
    [
        sg.Text("left images folder", size=(15, 1)),
        sg.Input(key="IN", change_submits=True, size=(50, 1)),
        sg.FolderBrowse(key="IN", size=(10, 1)),
    ],
    [sg.Button("Execute", size=(10, 1))],
]

window = sg.Window("My File Browser", layout, size=(600, 150))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Execute":
        left_side_picture_path = values["IN"]
        break

print(left_side_picture_path)
