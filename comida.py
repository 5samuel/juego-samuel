import turtle
import time
import random 

posponer = 0.1
#window configuration
wn = turtle.Screen ()
wn.title ("Juego de Snake")
wn.bgcolor ("pink")
wn.setup(width=600,height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle ()
head.speed (0)
head.shape("circle")
head.penup()
head.goto(0,0)
head.direction="stop"
head.color ("black")

#food
food = turtle.Turtle ()
food.speed (0)
food.shape ("square")
food.color("red")
food.penup()
food.goto(0,100)

#snake body IT CREATES AN EMPTY LIST // se agrega el segmento de la lista new_segment

segmentos = []

#Functions
def mov():

    #to move up
    if head.direction=="up":
        y = head.ycor()
        head.sety(y+20)
    #to move down
    if head.direction=="down":
        y = head.ycor()
        head.sety(y-20)
    #to move left
    if head.direction=="left":
        x = head.xcor()
        head.setx(x-20)

    #to move right
    if head.direction=="right":
        x = head.xcor()
        head.setx(x+20)

#Functions to link w/keyboard
def arriba ():
    head.direction="up"
def abajo ():
    head.direction="down"
def izquierda ():
    head.direction="left"
def derecha ():
    head.direction="right"

#Keyboard
wn.listen()
#Parametros pasados a la funcion, la primera letra mayusucula para indicar que es la flecha del keyboard
wn.onkeypress (arriba,"Up")
wn.onkeypress (abajo,"Down")
wn.onkeypress (izquierda,"Left")
wn.onkeypress (derecha,"Right")


#all game have always a loop
while True:
    wn.update()
    #collision egdes
    if head.xcor ()>280 or head.xcor()<-290 or head.ycor()>280 or head.ycor()<-280:
        time.sleep (1) #pause to the game 
        head.goto(0,0)
        head.direction = "stop"
    #hide the segments after the game reiniciate
      

    #segments of body 
    if head.distance (food)<20:
        #parametros de distribucion de la comida 
        x = random.randint (-280,280)
        y = random.randint (-280,280)
        food.goto (x,y)

       

        new_segment = turtle.Turtle ()
        new_segment.speed (0)
        new_segment.penup()
        new_segment.shape("circle")
        new_segment.color ("grey")
        segmentos.append(new_segment)

        #move snakes body
    totalSeg = len(segmentos)
    for index in range (totalSeg-1,0,-1):
        x = segmentos [index-1].xcor ()
        y = segmentos [index-1].ycor ()
        segmentos [index].goto(x,y)
    if totalSeg>0:
        x = head.xcor()
        y = head.ycor()
        segmentos [0].goto(x,y)
    
    
    
    mov ()
    time.sleep (posponer)