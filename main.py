import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state

correct_answers = []

while len(correct_answers) < 51:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="Type a state name or Exit: ").title()

    state_name = turtle.Turtle()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_answers]
        # missing_states = []
        # for state in states:
        #     if state not in correct_answers:
        #         missing_states.append(state)
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("missing_states.csv")
        break

    if answer_state in states.values:

        state_data = data[data.state == answer_state]
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        state_name.write(answer_state, align="center", font=("Courier", 10, "bold"))

        if answer_state not in correct_answers:
            correct_answers.append(answer_state)

