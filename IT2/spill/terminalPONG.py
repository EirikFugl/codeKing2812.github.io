import os
import time
import keyboard

class design:
    HEADER = '\033[95m' # lilla
    BLUE = '\033[94m' # blå
    CYAN = '\033[96m' # turkis
    GREEN = '\033[92m' # grønn
    WARNING = '\033[93m' # gul
    FAIL = '\033[91m' # rød

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


os.system('cls')

print(design.BOLD + 'Welcome to the classic arcade game PONG!' + design.END)
print('Player 1 uses W  S and Player 2 uses arrow up or arrow down')
print('The player with the most points in 90 seconds win')
print('Press C for classic graphics or M for modern graphics')
print('Then press enter to start the game!')

grafikk = input()

if grafikk.lower() == 'c' :
    grafikk = 'O '
elif grafikk.lower() == 'm' :
    grafikk = '██'
else :
    print('You have to write c or m!')




def tegn(x, y, farge):
    if farge == 'l':
        rader[y][x] =  (design.HEADER)
    elif farge == 'r':
        rader[y][x] =  (design.FAIL)
    elif farge == 'b':
        rader[y][x] =  (design.CYAN)
        
    rader[y][x] += (grafikk + design.END)


p1= {'y': 6, 'yv': 0, 'score': 0}
p2= {'y': 6, 'yv': 0, 'score': 0}
ball = {'x': 12, 'y': 7, 'xv': 1, 'yv': 0}

brettHøyde = 15
brettBredde = 25



# # # # # # # # # # GAMELOOP # # # # # # # # # #

spillLengde = 90
framerate = 0.15
tid = startTid = time.time()

while tid < startTid + spillLengde: # gjennom hele spillet

    if keyboard.is_pressed('s'):
        if p1['yv'] < 1 :
            p1['yv'] += 1
    elif keyboard.is_pressed('w'):
        if p1['yv'] > -1 :
            p1['yv'] -= 1

    if keyboard.is_pressed('Down'):
        if p2['yv'] < 1 :
            p2['yv'] += 1
    elif keyboard.is_pressed('Up'):
        if p2['yv'] > -1 :
            p2['yv'] -= 1
    # key lytter


    if time.time() > tid: 
        tid += framerate # kjør frame hvert n'te sekund

        if tid - startTid > spillLengde - 30:
            framerate = 0.10 # gå fortere 
        elif tid - startTid > spillLengde - 15:
            framerate = 0.8 # enda fortere

        
        os.system('cls')
        # refresh skjermen
        

        rader = []
        for i in range(brettHøyde):
            rad = [grafikk]*brettBredde
            rader.append(rad)
        # nullstill alle rader


        
        p1['y'] += p1['yv'] 
        p1['yv'] = 0
        p2['y'] += p2['yv'] 
        p2['yv'] = 0
        # flytt rackerter


        if ball['x'] == 1 :

            if ball['y'] == p1['y'] : 
                ball['xv'] = -ball['xv'] # snu
                if ball['yv'] > -1:
                    ball['yv'] -= 1 # gå opp

            elif ball['y'] == p1['y']+1 :
                ball['xv'] = -ball['xv'] # snu
                
            elif ball['y'] == p1['y']+2 : 
                ball['xv'] = -ball['xv'] # snu
                if ball['yv'] < 1:
                    ball['yv'] += 1 # gå ned
        # sprett i rackert 1


        if ball['x'] == brettBredde-2 :

            if ball['y'] == p2['y'] : 
                ball['xv'] = -ball['xv'] # snu
                if ball['yv'] > -1:
                    ball['yv'] -= 1 # gå opp

            elif ball['y'] == p2['y']+1 :
                ball['xv'] = -ball['xv'] # snu

            elif ball['y'] == p2['y']+2 : 
                ball['xv'] = -ball['xv'] # snu
                if ball['yv'] < 1:
                    ball['yv'] += 1 # gå ned
        # sprett i rackert 2


        if ball['y'] <= 0 :
            ball['y'] = 0
            ball['yv'] = -ball['yv'] 
        elif ball['y'] >= brettHøyde-1 :
            ball['y'] = brettHøyde-1
            ball['yv'] = -ball['yv']
        # sprett i tak/gulv


        if ball['x'] <= 0 :
            p2['score'] += 1
            ball['x'] = 12
            ball['y'] = 7
            ball['yv'] = 0
            ball['xv'] = 1
        elif ball['x'] >= brettBredde-1 :
            p1['score'] += 1
            ball['x'] = 12
            ball['y'] = 7
            ball['yv'] = 0
            ball['xv'] = -1
        # hvis ballen er utenfor


        if p1['y']+2 >= brettHøyde :
            p1['y'] = brettHøyde-3
        elif p1['y'] <= 0:
            p1['y'] = 0
        if p2['y']+2 >= brettHøyde :
            p2['y'] = brettHøyde-3
        elif p2['y'] <= 0:
            p2['y'] = 0
        # hold rackertene på banen
    
        ball['x'] += ball['xv']
        ball['y'] += ball['yv'] 
        tegn(ball['x'], ball['y'], 'r')

        tegn(1, p1['y'], 'b')
        tegn(1, p1['y']+1, 'b')
        tegn(1, p1['y']+2, 'b')
        #rackert 1

        tegn(brettBredde-2, p2['y'], 'l')
        tegn(brettBredde-2, p2['y']+1, 'l')
        tegn(brettBredde-2, p2['y']+2, 'l')
        #rackert 2


        print(design.WARNING + str(spillLengde-(round(tid-startTid))) + '   ' + str(p1['score']) + ' - ' + str(p2['score']) + design.END)

        for rad in rader:
            pikselString = ''
            for piksel in rad:
                pikselString += piksel #lager en string av raden
            print(pikselString) # skriver ut stringen
            
print(design.FAIL + 'T I M E   I S   U P   -   G A M E   O V E R' + design.END)

if p2['score'] < p1['score'] :
    print(design.GREEN + 'CYAN WINS!' + design.END)
else :
    print(design.GREEN + 'PURPLE WINS!' + design.END)