import turtle
import pandas
data = pandas.read_csv("day25/50_states.csv")
print(data)
data1 =data['state'].to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day25/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
gusessed_state = []
game_on = True


while len(gusessed_state ) < 50:
    answer_state = screen.textinput(f"{len(gusessed_state)} / 50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state in data1:
        gusessed_state.append(answer_state)
        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state_data = data[data.state == answer_state]
        state.goto(state_data.x.item(), state_data.y.item())
        state.write(answer_state)
    elif answer_state == 'Exit':
        missing_states = [item for item in data1 if item not in gusessed_state ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
# states_to_learn.csv
