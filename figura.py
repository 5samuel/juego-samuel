import turtle

window = turtle.Screen()
flecha = turtle.Turtle()
window.color=("grey")

def triangulo():
   for i in range(3):
      flecha.forward(100)
      flecha.left(120)

def cuadrado():
   for i in range(4):
      flecha.forward(100)
      flecha.left(90)

def pentagono():
   for i in range(5):
      flecha.forward(100)
      flecha.left(72)
      

triangulo()
cuadrado()
pentagono()