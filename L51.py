#the authors' names are Abby Newton and Sydney Eidelbes
import turtle
bob=turtle.Turtle()
def draw_star(color):
    for side in range(6):
        bob.forward(100)
        bob.right(144)
        bob.color(color)
bob.width(5)
bob.speed(0)
mood=input("What is your mood?")
if mood=="happy":
    draw_star("pink")
elif mood=="sad":
    draw_star("blue")
elif mood=="sleepy":
    draw_star("green")
elif mood=="angry":
    draw_star("red")
else:
    print("choose different mood")
