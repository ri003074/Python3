import PySimpleGUI as sg

layout = [
    [sg.Input(key="_FILEBROWSE_", enable_events=True, visible=False)],
    [sg.FileBrowse(target="_FILEBROWSE_")],
    [sg.OK()],
]

window = sg.Window("My new window").Layout(layout)

while True:  # Event Loop
    event, values = window.Read()
    if event is None:
        break
    print(event, values)