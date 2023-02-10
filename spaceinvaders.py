import turtle
import os
import math
import random


#tela
tl = turtle.Screen()
tl.bgcolor("black")
tl.title =("Space Invaders")
tl.bgpic("tl.gif")
tl.tracer(0)

tl.register_shape("invader.gif")
tl.register_shape("player.gif")


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
pontostring = "Pontos: {}" .format(ponto)
ponto_pen.write(pontostring, False, align = "left", font = ("arial", 14, "normal"))
ponto_pen.hideturtle()


#heroi
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0



#escolher qtd inimigos
num_inimigos = 30

inimigos = []

#add ini to list

for i in range(num_inimigos):
    inimigos.append(turtle.Turtle())
    
inimigo_start_x = -225
inimigo_start_y = 250
inimigo_num = 0
       
for inimigo in inimigos:
    inimigo.shape("invader.gif")
    inimigo.penup()
    inimigo.speed(0)
    x = inimigo_start_x + (50 * inimigo_num)
    y = inimigo_start_y 
    inimigo.setposition(x,y)
    
    inimigo_num +=1
    if inimigo_num == 10:
        inimigo_start_y -= 50
        inimigo_num = 0

inimigospeed = 0.02




#arma
tiro = turtle.Turtle()
tiro.color("red")
tiro.shape("square")
tiro.penup()
tiro.speed(0)
tiro.setheading(90)
tiro.shapesize(0.5, 0.5)
tiro.hideturtle()

tirospeed =3
#tiro estado s
tiroestado = "pronto"


#mover p/ direita e esquerda
def mov_esq():
    player.speed = -1

    
def mov_dir():
    player.speed = 1

def mov_player():
    x = player.xcor()
    x += player.speed
    if x <= -280:
        x = -280
    if x >= 280:
        x = 280
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

def win():
    if ponto == 300:
        tl2 = turtle.Screen()
        tl.bgcolor("black")
        tl.title =("Space Invaders")
        tl.bgpic("winner.gif")
        player.setposition(0,-4000)
    
def menu():
    tl3 = turtle.Screen()
    tl.bgcolor("black")
    tl.title =("Space Invaders")
    tl.bgpic("winner.gif")
    #if tl.onkeypress("space"):
       

    
tl.listen()
tl.onkeypress(mov_esq, "Left")
tl.onkeypress(mov_dir, "Right")
tl.onkeypress(mov_tiro, "space")



# Main Jogo loop
while True:
  #  menu()
    tl.update()
    mov_player()
    
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
           tiro.setposition(0, -40000)
           inimigo.setposition(0,10000)
           
           #pontuacao
           ponto += 10
           pontostring = "Pontos: {}" .format(ponto)
           ponto_pen.clear()
           ponto_pen.write(pontostring, False, align = "left", font = ("arial", 14, "normal"))

        
        
        if colisao(player,inimigo):
            player.hideturtle()
            inimigo.hideturtle()
            print ("Game Over")
         

    #mover o tiro
    y = tiro.ycor()
    y += tirospeed
    tiro.sety(y)
        
    #tiro some no topo 
    if tiro.ycor() > 275:
        tiro.hideturtle()
        tiroestado = "pronto"
    win()
        
#o q tem q fazer        
#tela menu        
#setar o speed de todos os bonecos
#tela game over
#tela win
#def vidas():
#--opcional--
#def inimigos atirar
        
#if all inimigos setposition == (0,100000)
    #tela win
        
#if ponto == 300
    #tela win
         
 

