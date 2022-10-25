import turtle
import datetime
import pandas

screen = turtle.Screen()
screen.title("Lietuvos administraciniai centrai")
image = "lietuvos_zemelapis.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("savivaldybes.csv")
centrai = data.centras.tolist()
score=0
correct_guesses = []

name = screen.textinput(title=f"Vardas", prompt="Koks Jūsų vardas?")


while len(correct_guesses) < 55:
    score = len(correct_guesses)
    answer_center = screen.textinput(title=f"{score}/55 atspėta adm. centrų ", prompt="Koks kitas administracinis centras?").title()
    if answer_center == "Baigti":
        break
    if answer_center in centrai and not answer_center in correct_guesses:
        correct_guesses.append(answer_center)
        t = turtle.Turtle()
        t.speed("fastest")
        t.penup()
        t.hideturtle()
        center_data = data[data.centras == answer_center]
        t.goto(center_data.x.item(), center_data.y.item())
        t.write(answer_center)

t = turtle.Turtle()
t.penup()
t.hideturtle()
t.goto(0, 0)
t.write(f"Jūsų rezultatas: {score}")

screen.exitonclick()

date_and_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


fields=[[date_and_time,name,score]]
df = pandas.DataFrame(fields)
df.to_csv('results.csv', mode='a', header=False, index=False)