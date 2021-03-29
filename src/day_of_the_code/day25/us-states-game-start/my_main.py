import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Challenge")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
print(len(data))
data_dic = data.to_dict()
print(data_dic)
for key, value in data_dic.items():
    print(key)
    print(value)

data_formatted = {}
for i in range(1, len(data)):
    data_formatted[data_dic["state"][i].lower()] = (data_dic["x"][i], data_dic["y"][i])


print(data_formatted)

correct_count = 0
while True:
    answer_state = screen.textinput(
        title=f"Guess the state{correct_count}/{len(data)-1}",
        prompt="What's another state name",
    )

    if answer_state.lower() in data_formatted:
        print("ok!")
        correct_count += 1
    else:
        break

screen.exitonclick()
