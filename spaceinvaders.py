import turtle
import os
import math
import random


#tela
tl = turtle.Screen()
tl.bgcolor("black")
tl.title =("Space Invaders")


#delay = raw_imput("Enter para sair")

#tela setup
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#pontuação
ponto = 0

ponto_pen = turtle.Turtle()
ponto_pen.speed(0)
ponto_pen.color("white")
ponto_pen.penup()
ponto_pen.setposition(-290, 270)
pontostring = "Pontos: %s" %ponto
ponto_pen.write(pontostring, False, align = "left", font = ("arial", 14, "normal"))
ponto_pen.hideturtle()


#heroi
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


playerspeed = 15



#escolher qtd inimigos
num_inimigos = 5

inimigos = []

#add ini to list

for i in range(num_inimigos):
    inimigos.append(turtle.Turtle())
    
for inimigo in inimigos:
    inimigo.color("yellow")
    inimigo.shape("circle")
    inimigo.penup()
    inimigo.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    inimigo.setposition(x,y)


inimigospeed = 2




#arma
tiro = turtle.Turtle()
tiro.color("red")
tiro.shape("square")
tiro.penup()
tiro.speed(0)
tiro.setheading(90)
tiro.shapesize(0.5, 0.5)
tiro.hideturtle()

tirospeed = 20
#tiro estados
tiroestado = "pronto"


#mover p/ direita e esquerda
def mov_esq():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
    
def mov_dir():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 270
    player.setx(x)
    
#mover tiro

def mov_tiro():
    global tiroestado
    if tiroestado == "pronto":
        tiroestado == "fire"
        x = player.xcor()
        y = player.ycor()
        tiro.setposition(x , y +10)
        tiro.showturtle()
        
def colisao(t1, t2):
    if t1.distance (t2) <20:
        return True
    else:
        return False

    
turtle.listen()
turtle.onkey(mov_esq, "Left")
turtle.onkey(mov_dir, "Right")
turtle.onkey(mov_tiro, "space")
    
    
    
    
# Main Jogo loop
while True:
    
    for inimigo in inimigos:
        #mover o inimigo
        x = inimigo.xcor()
        x += inimigospeed
        inimigo.setx(x)


        #mover o inimigo p/ lado e baixo

        if inimigo.xcor() > 280:
            #mover todos os ini p/ baixo
            for j in inimigos:  
                y = j.ycor()
                y -= 40
                j.sety(y)
            inimigospeed *= -1

        if inimigo.xcor() < -280:
            #mover todos os ini p/ baixo
            for j in inimigos:
                y = j.ycor()
                y -= 40 
                j.sety(y)
            inimigospeed *= -1

        #checar colisao tiro/inimigo 
        if colisao(tiro,inimigo):
         
           tiro.hideturtle()
           tiroestado ="pronto"
           tiro.setposition(0, -400)
           x = random.randint(-200, 200)
           y = random.randint(100, 250)
           inimigo.setposition(x,y)
           
           #pontuacao
           ponto += 10
           pontostring = "Pontos: %s" %ponto
           ponto_pen.clear()
           ponto_pen.write(pontostring, False, align = "left", font = ("arial", 14, "normal"))

        
        
        if colisao(player,inimigo):
            player.hideturtle()
            inimigo.hideturtle()
            print ("Game Over")
            break

    #mover o tiro
    y = tiro.ycor()
    y += tirospeed
    tiro.sety(y)
        
    #tiro some no topo 
    if tiro.ycor() > 275:
        tiro.hideturtle()
        tiroestado = "pronto"
         
 

#delay = raw_input("Enter para sair")


























