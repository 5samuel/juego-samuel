#tortuga de importación
import turtle
import random

window = turtle.Screen()
window.bgcolor("red")

random_colors = ["#0ca90c", "#c20d0d", "#ffffff", "#ffd700", "#3225de", "#8314b9"]

tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.left(90)

def dibujarArbol(tamanoDeRama, tortuga):
    tortuga.pensize(tamanoDeRama/10)
    if (tamanoDeRama < 40):
        tortuga.dot(random.randint(7, 10), random.choice(random_colors))
        return
    tortuga.forward(tamanoDeRama)
    tortuga.left(30)
    dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga)
    tortuga.right(60)
    dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga)
    tortuga.left(30)
    tortuga.backward(tamanoDeRama)

tortuga.penup()
tortuga.setpos(0, -250)
tortuga.pendown()
tortuga.hideturtle()
tortuga.color("#406c35")
dibujarArbol(100, tortuga)


exit() # borrar para hacer arbol navideño


tortuga.penup()
tortuga.setpos(-60, 150)
tortuga.pendown()
tortuga.color("yellow")
tortuga.begin_fill()
for i in range(5): # estrella de 5 puntas
    tortuga.forward(150)
    tortuga.right(144)
tortuga.end_fill()

# LUCES
maxY = 250
maxX = 350
luces = []

for j in range(0, 10000):
    y = random.randint(-1*maxY, maxY)
    x = random.randint(-1*maxX, maxX)
    luz = turtle.Turtle()
    luz.speed(0)
    luz.hideturtle()
    luz.penup()
    luz.setpos(x, y)
    luz.pendown()
    luz.dot(random.randint(1, 5), random.choice(random_colors))
    luces.append(luz)
    if len(luces) > 150:
        luzAApagar = random.choice(luces)
        luzAApagar.clear()



texto = turtle.Turtle()
	
texto.color("white")
texto.penup() # para que no aparezca la plumita que pinta el texto
texto.hideturtle()
texto.goto(0,260)
texto.write("samuel jose ", align = "center", font = ("Courier", 24,"normal"))


window.exitonclick()