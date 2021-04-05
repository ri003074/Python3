import PySimpleGUI as sg

#  セクション1 - オプションの設定と標準レイアウト
sg.theme("Dark Blue 3")

layout = [
    [sg.Text("Python GUI")],
    [sg.Text("名前", size=(15, 1)), sg.InputText("○○〇×××")],
    [sg.Text("住所", size=(15, 1)), sg.InputText("△△△△村")],
    [sg.Text("電話番号", size=(15, 10)), sg.InputText("xxx-xxx-xxx")],
    [sg.Submit(button_text="実行ボタン")],
    [sg.Submit(button_text="追加ボタン")],
]

layout.append([sg.Text("DUT", size=(15, 1)), sg.InputText("abc")])
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
        show_message += "住所：" + values[1] + "が入力されました。\n"
        show_message += "電話番号：" + values[2] + "が入力されました。"
        print(show_message)
        # ポップアップ
        sg.popup(show_message)

    if event == "追加ボタン":
        layout.append([sg.Text("DUT", size=(15, 1)), sg.InputText("abc")])
        window = sg.Window("住所を入力", layout)


# セクション 4 - ウィンドウの破棄と終了
window.close()