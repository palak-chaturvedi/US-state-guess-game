import turtle
import pandas

screen = turtle.Screen()
screen.title("US states Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
score = 0


# get coordinates at the position of mouse click
# def get_mouse_click_coor(x,y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
guessed_state = []


while len(guessed_state) <50:
    state = screen.textinput(title=f"States correct{score}/50 ", prompt="Guess name:").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data["state"].to_list()
    if state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data= pandas.DataFrame(missing_states)
        new_data.to_csv("missed states.csv")

        break
    if state in all_states:
        y_cor = data[data.state == state].y
        x_cor = data[data.state == state].x
        tam = turtle.Turtle()
        tam.hideturtle()
        tam.penup()
        tam.goto(int(x_cor),int(y_cor))
        tam.write(state)
        score+=1
        guessed_state.append(state)

screen.bye()