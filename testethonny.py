import WConio2 as WConio2
import cursor
import os
'''
fazer um caractere se mover
x = 5
y = 5

while True:
    gotoxy(x,y)
    print("0")
    c =getkey()
    gotoxy(x,y)
    print(" ")
    if c == 'd' : x += 1
    if c == 'a' : x -= 1
    if c == 'w' : y -= 1
    if c == 's' : y += 1
    if c == 'x' : break

'''
'''
x = 5
y = 5

while True:
    gotoxy(x,y)
    print("O")
    c =getkey()
    gotoxy(x,y)
    print(" ")
    if c == 'd' and x <15: x += 1
    if c == 'a' and x> 5: x -= 1
    if c == 'w' and y >5 : y -= 1
    if c == 's' and y <15 : y += 1
    if c == 'x' : break
'''
'''
for i in range(4,17):
    gotoxy(i,4);print("#")
    gotoxy(i,16);print("#")    
    gotoxy(4,i);print("#")
    gotoxy(16,i);print("#")


x = 5
y = 5

while True:
    gotoxy(x,y)
    print("O")
    
    c =getkey()
    gotoxy(x,y)
    
    print(" ")
    if c == 'd' and x <15: x += 1
    if c == 'a' and x >5: x -= 1
    if c == 'w' and y >5 : y -= 1
    if c == 's' and y <15 : y += 1
    if c == 'x' : break



x = 50
y = 40


while True:
    gotoxy(x,y)
    print("O")
    
    c =getkey()
    gotoxy(x,y)
    
    print(" ")
    if c == 'd' and x < 15 : x += 1
    if c == 'a' and x > 5  : x -= 1
    if c == 'w' and y > 5  : y -= 1
    if c == 's' and y < 15 : y += 1
    if c == 'x' : break



'''



cursor.hide()
os.system('cls')

tiro = '⛬'
tiroX = 56 #56
tiroY = 19

heroi = '⛫'
heroiX = 56
heroiY = 17 #4

bicho = '⛒'
bichoX = 10
bichoY = 4

#contador de frames
cont=0
aux = 0

while True:
    WConio2.gotoxy(0,0)
    
    
    
    print('='*118)
    for j in range(20):
        print('+', end='')
        for k in range(116): #116
            char = ' '
            
            if j==bichoY and k==bichoX:
                char=bicho

            
            if j==heroiY and k==heroiX:
                char=heroi
                
            if j==tiroY and k==tiroX:
                char=tiro

            print(char, end='')

        print('+')
    print('='*118)


    #controlando    
    if cont%200 == 0: #velocidade dos inimigos 200min 150 max
        bichoX+=3  #quadros q o inimigo anda 3 
    if bichoX > 108: # ate ele vai na tela
        bichoX=10
        
    if heroiX > 114: # ate ele vai na tela
        heroiX+= -1
    
    elif heroiX < 0: # ate ele vai na tela
        heroiX-= -1
  
    if aux%200 == 0: #talvez fazer disso uma função e chamar na hora de ativar a tecla z
        tiroY-=3
        if tiroY <-3:
            tiroY = 16
            tiroX = heroiX
        
    #pegando comandos do teclado
    if WConio2.kbhit():
        (key, symbol) = WConio2.getch()

        if symbol=='a':
            heroiX-=1
        elif symbol=='d':
            heroiX+=1
        if symbol=='w':
            heroiY-=1
        elif symbol=='s':
            heroiY+=1
            
        if symbol == 'z':
            tiroY-= 1
            tiro()
        

    cont+=1
    aux+=1

















