import turtle
import pandas

# import sys

screen = turtle.Screen()
screen.title("US State Challenge")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()

print(all_states)

guessed_state = []
while len(guessed_state) < len(all_states):
    answer_state = screen.textinput(
        title=f"Guess the state{len(guessed_state)}/{len(data)-1}",
        prompt="What's another state name",
    ).title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        print(missing_state)
        df = pandas.DataFrame(missing_state)
        df.to_csv("missed_state.csv")

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        print("ok!")
        guessed_state.append(state_data.state.item())
    else:
        break

screen.exitonclick()
