import PySimpleGUI as sg

#  セクション1 - オプションの設定と標準レイアウト
sg.theme("Dark Blue 3")

layout = [
    [sg.Text("Python GUI")],
    [
        sg.Text("DUT", size=(5, 1)),
        sg.InputText("×", size=(3, 1)),
        sg.Text("PIN", size=(5, 1)),
        sg.InputText("×", size=(3, 1)),
    ],
    [sg.Submit(button_text="実行ボタン")],
]

# セクション 2 - ウィンドウの生成
window = sg.Window("住所を入力", layout)

# セクション 3 - イベントループ
while True:
    event, values = window.read()

    if event is None:
        print("exit")
        break

    if event == "実行ボタン":
        show_message = "名前：" + values[0] + "が入力されました。\n"
        print(show_message)
        sg.popup(show_message)


# セクション 4 - ウィンドウの破棄と終了
window.close()
