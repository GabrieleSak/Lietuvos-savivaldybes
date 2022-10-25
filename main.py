import turtle

import pandas

screen = turtle.Screen()
screen.title("Lietuvos administraciniai centrai")
image = "lietuvos_zemelapis.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("savivaldybes.csv")
centrai = data.values.tolist()

print(centrai)
for centras in centrai:
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.hideturtle()
    t.goto(centras[1], centras[2])
    t.write(centras[0])

# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")








turtle.mainloop()