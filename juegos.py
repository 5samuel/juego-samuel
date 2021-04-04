import turtle
import time 
import random


posponer = 0.1

#marcador
score = 0
high_score =0



#Configuracion de la ventana
wn = turtle.Screen()
wn.title('juego de snake')
wn.bgcolor('black')
wn.setup(width=600,height=600)
wn.tracer(0)


#cabeza de serpiente


cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')

cabeza.goto(0,0)
cabeza.direction = 'stop'
cabeza.color('white')



#comida


comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup()
comida.color('red')
comida.goto(0,100)


#segmento o cuerpo de la serpiente
segmento=[]

#texto 
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("score: 0         high score: 0", align="center", font=("courier", 24, "normal"))



#Funciones


def arriba():
    cabeza.direction = 'up'


def abajo():
    cabeza.direction = 'down'


def izquierda():
    cabeza.direction = 'left'


def derecha():
    cabeza.direction = 'right'





def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)


    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)


    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)


    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
#teclado


wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')




while True:
    wn.update()
      #colicion bordes
    if cabeza.xcor ()>280 or cabeza.xcor()<-280 or cabeza.ycor()>280 or cabeza.ycor()<-280:
        time.sleep (1) #pause to the game 
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        for nuevo_segmento in segmento:
             nuevo_segmento.hideturtle()

        #clean segmentos list
        segmento.clear()
            
            
        
      
            
    
            
            


          


    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.penup()
        nuevo_segmento.goto(0,0)
        nuevo_segmento.color('grey')
        segmento.append(nuevo_segmento)

        # aumentar marcador
        score +=10


        if score >high_score:
            high_score = score
        
           


    #mivimiento del cuerpo
    totalseg=len(segmento)
    for index in range(totalseg -1,0,-1):
        x= segmento[index -1].xcor()
        y = segmento[index -1].ycor()
        segmento[index].goto(x,y)
    
    if totalseg >0:
        x =cabeza.xcor()
        y =cabeza.ycor()
        segmento[0].goto(x,y)
    
  

    mov()
    time.sleep(posponer)