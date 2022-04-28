import pygame
import os, time
from pygame.constants import K_SPACE

pygame.init()
pygame.mixer.init()

scX, scY = 1500, 1000
stredX, stredY = scX//2, scY//2
screen = pygame.display.set_mode([scX, scY], pygame.RESIZABLE)
pygame.display.set_caption('puzzle')
clock = pygame.time.Clock()
nazev = pygame.font.Font("Emulogic.ttf", 100)
font1 = pygame.font.Font("Emulogic.ttf", 30)
font2 = pygame.font.Font("Emulogic.ttf", 50)
font3 = pygame.font.Font("Emulogic.ttf", 150)
nastaveni = 0

click = pygame.mixer.Sound("sound/click.wav")
click.set_volume(0.2)
hudba = pygame.mixer.music.load("sound/music.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

zvukOn = pygame.image.load("icon/soundOn.png").convert_alpha()
zvukOff = pygame.image.load("icon/soundOff.png").convert_alpha()
hudbaOn = pygame.image.load("icon/musicOn.png").convert_alpha()
hudbaOff = pygame.image.load("icon/musicOff.png").convert_alpha()
nasta = pygame.image.load("icon/settings.png").convert_alpha()
reset = pygame.image.load("icon/Restart.png").convert_alpha()
kriz = pygame.image.load("icon/krizek.png").convert_alpha()
frame = pygame.image.load("icon/ctverec.png").convert_alpha()
back = pygame.image.load("icon/Back.png").convert_alpha()

BLOK = 60

stena = pygame.image.load("grafika/stena.png").convert()
stena = pygame.transform.scale(stena, (BLOK, BLOK))
box = pygame.image.load("grafika/krabiceCela.png").convert()
box = pygame.transform.scale(box, (BLOK, BLOK+BLOK//3))
podlaha = pygame.image.load("grafika/podlaha2.png").convert()
podlaha = pygame.transform.scale(podlaha, (BLOK, BLOK))
boxZ = pygame.image.load("grafika/krabiceZelena.png").convert()
boxZ = pygame.transform.scale(boxZ, (BLOK, BLOK+BLOK//3))
podlahaZ = pygame.image.load("grafika/podlahaZelena.png").convert()
podlahaZ = pygame.transform.scale(podlahaZ, (BLOK, BLOK))
karaZezadu = pygame.image.load("grafika/KaraZezaduX.png").convert_alpha()
karaZezadu = pygame.transform.scale(karaZezadu, (BLOK, BLOK+BLOK//3))
karaZezadu2 = pygame.image.load("grafika/KaraZezaduX2.png").convert_alpha()
karaZezadu2 = pygame.transform.scale(karaZezadu2, (BLOK, BLOK+BLOK//3))
karaZeStrany = pygame.image.load("grafika/KaraZeStrany.png").convert_alpha()
karaZeStrany = pygame.transform.scale(karaZeStrany, (BLOK, BLOK+BLOK//3))
karaZeStrany2 = pygame.image.load("grafika/KaraZeStrany2.png").convert_alpha()
karaZeStrany2 = pygame.transform.scale(karaZeStrany2, (BLOK, BLOK+BLOK//3))
karaZDruhyStrany = pygame.transform.flip(karaZeStrany, True, False)
karaZDruhyStrany2 = pygame.transform.flip(karaZeStrany2, True, False)
karaZepredu = pygame.image.load("grafika/KaraZepredu.png").convert_alpha()
karaZepredu = pygame.transform.scale(karaZepredu, (BLOK, BLOK+BLOK//3))
karaZepredu2 = pygame.image.load("grafika/KaraZepredu2.png").convert_alpha()
karaZepredu2 = pygame.transform.scale(karaZepredu2, (BLOK, BLOK+BLOK//3))


ZVUK = True
HUDBA = True

FPS = 60
BLUE = (70, 132, 255)
RED = (255, 90, 90)
YELLOW = (252, 148, 3)
SCENA = "main menu"
POCETLEVELU = 20

jede = True
i = 0
scenaPred = "main menu"
levly = {}
levlyComplet = []
levl = ""

dataRead = open("data.txt", "r")
daticka = dataRead.read()
for jkvnjs in daticka:
    if jkvnjs.isdigit():
        levl+=jkvnjs
    else:
        levlyComplet.append(int(levl))
        levl = ""

dataRead.close()
data = open("data.txt", "a")

#################### MAPA ################################

def ctiMapu(cislo):
    global mapa, radek
    mapa = []
    radek = []
    f = open("mapa.txt")

    while True:
        x = f.read(1)
        if x == str(cislo) or (cislo >= 10 and x == str(cislo)[0] and f.read(1) == str(cislo)[1]):
            while True:
                x = f.read(1)
                if x == ".":
                    mapa.append(radek)
                    f.close()
                    break
                elif x == "\n":
                    if len(radek) != 0:
                        mapa.append(radek)
                        radek = []
                else: radek.append(x)
            break
        elif x == "!": break
ctiMapu(1)

def rozmery(x):
    kolik = 0
    if x == "y":
        for i in mapa:
            kolik += 1
    elif x == "x":
        for i in radek:
            kolik += 1
    return kolik
#####################################    KLAAAAAAAAAAAAAAAAASSSSSSYYYYYYYYYYYYYYYYYYYY    ####################################



def btn(screen,sizePos,text="nic",obrazek="",barva=(0,0,0),barvaTextu=(100,100,100)):
    
    font = pygame.font.Font("Emulogic.ttf", sizePos[3] // 3)
    b1 = pygame.draw.rect(screen, barva, sizePos, border_radius = 5)
    if text == "nic":
        obrazek = pygame.transform.scale(obrazek, (60, 60))
        obraz = obrazek.get_rect()
        obraz.center = b1.center
        screen.blit(obrazek,obraz)
    else:
        txt1 = font.render(text, True, barvaTextu)
        txtRect = txt1.get_rect()
        txtRect.center = b1.center
        screen.blit(txt1,txtRect)
    return b1

casik = 0

def kresli():
    global restart,casik,zpet

    if SCENA == "hra":
        screen.fill((0,0,0))
        btn(screen,(scX - 300, 20,200,50),"fps: " + str(int(clock.get_fps())) + "  XY: " + str(p.x) +","+ str(p.y), 100)
        restart = btn(screen,(20,20,70,70),obrazek=reset,barva=(0,0,0))
        zpet = btn(screen,(100,20,70,70),obrazek=back,barva=(0,0,0))
        krabice = []
        krabiceZ = []
        for x in range(rozmery("x")):
            for y in range(rozmery("y")):
                if mapa[y][x] == " " or mapa[y][x] == "@":
                    screen.blit(podlaha,(x*BLOK + (scX-rozmery("x")*BLOK)/2,y*BLOK + (scY-rozmery("y")*BLOK)/2,BLOK,BLOK))
                elif mapa[y][x] == "#":
                    screen.blit(stena,(x*BLOK + (scX-rozmery("x")*BLOK)/2,y*BLOK + (scY-rozmery("y")*BLOK)/2,BLOK,BLOK))
                elif mapa[y][x] == "B":
                    krabice.append(x)
                    krabice.append(y)
                elif mapa[y][x] == "O":
                    screen.blit(podlahaZ,(x*BLOK + (scX-rozmery("x")*BLOK)/2,y*BLOK + (scY-rozmery("y")*BLOK)/2,BLOK,BLOK))
                elif mapa[y][x] == "X":
                    krabiceZ.append(x)
                    krabiceZ.append(y)
        
        postava.kreslim()

        #aby vozík nejezdil po boxech, vykreslíme boxy až po něm
        for x in range(0,len(krabice)//2):
            screen.blit(box,(krabice[x*2]*BLOK + (scX-rozmery("x")*BLOK)/2,krabice[x*2+1]*BLOK + (scY-rozmery("y")*BLOK)/2 - BLOK//3,BLOK,BLOK + BLOK//3))
        for x in range(0,len(krabiceZ)//2):
            screen.blit(boxZ,(krabiceZ[x*2]*BLOK + (scX-rozmery("x")*BLOK)/2,krabiceZ[x*2+1]*BLOK + (scY-rozmery("y")*BLOK)/2 - BLOK//3,BLOK,BLOK + BLOK//3))
    
    elif SCENA == "main menu":
        screen.fill((0,0,0))
        global i, nastaveni
        i += 1
        nastaveni = btn(screen,(20,20,70,70), obrazek = nasta)
        text = nazev.render("Puzzle", True, (255, 255, 255))
        text2 = font1.render('pro start stiskni "MEZERNIK"', True, (255, 255, 255))
        textRect = text.get_rect()
        text2Rect = text2.get_rect()
        textRect.center = (stredX, stredY - 250)
        text2Rect.center = (stredX, stredY + 200)
        screen.blit(text, textRect)
        if i <= 30:
            screen.blit(text2, text2Rect)
        elif i == 60:
            i = 0

    elif SCENA == "levely":
        screen.fill((0,0,0))
        nastaveni = btn(screen,(20,20,70,70), obrazek = nasta)
        text = nazev.render("Levels", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (stredX, stredY - 350)
        screen.blit(text, textRect)
        levliky()

    elif SCENA == "nastaveni": #nastaveni
        screen.fill((0,0,0))
        global hudbaBtn, krizek, zvukBtn
        text = font2.render("Nastaveni", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (stredX, stredY - 200)
        screen.blit(text, textRect)
        if ZVUK:
            zvukBtn = btn(screen,(stredX-150, stredY-50,100,100), obrazek = zvukOn)
        else:
            zvukBtn = btn(screen,(stredX-150, stredY-50,100,100), obrazek = zvukOff)
        if HUDBA:
            hudbaBtn = btn(screen,(stredX+50, stredY-50,100,100), obrazek = hudbaOn)
        else:
            hudbaBtn = btn(screen,(stredX+50, stredY-50,100,100), obrazek = hudbaOff)
        krizek = btn(screen,(stredX+310, stredY-260,100,100), obrazek = kriz)
        screen.blit(frame,(stredX-500, stredY-500))
    
    elif SCENA == "vyhra":
        text = font2.render("Completed", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (stredX, stredY - 300)
        screen.blit(text, textRect)

    pygame.display.flip()


def levliky():
    ii = -1
    for i in range(POCETLEVELU):
        if i%10 == 0:
            ii+=1
        if i+1 in levlyComplet:
            levly[i+1] = btn(screen,(stredX-10*90/2+i*90-ii*900,400+ii*100,70,70),str(i+1),barva=(0,255,0),barvaTextu = (0,0,0))
        else: levly[i+1] = btn(screen,(stredX-10*90/2+i*90-ii*900,400+ii*100,70,70),str(i+1),barva=(255,255,255),barvaTextu = (0,0,0))
        
            
class postava:
    def __init__(self):
        print(mapa)
        for i in range(len(mapa)):
            for y in range(len(radek)):
                if mapa[i][y] == "@":
                    self.x = y
                    self.y = i
                    mapa[i][y] = " "
                    break
        self.smer = "nahoru"

    def kreslim():
        global casik
        if p.smer == "nahoru":
            if casik == 30:
                casik = 0
                screen.blit(karaZezadu, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            elif casik >= 15: screen.blit(karaZezadu, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            else: 
                screen.blit(karaZezadu2, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            casik += 1
        elif p.smer == "doleva":
            if casik == 30:
                casik = 0
                screen.blit(karaZeStrany, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            elif casik >= 15: screen.blit(karaZeStrany, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            else: 
                screen.blit(karaZeStrany2, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            casik += 1

        elif p.smer == "doprava":
            if casik == 30:
                casik = 0
                screen.blit(karaZDruhyStrany, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            elif casik >= 15: screen.blit(karaZDruhyStrany, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            else: 
                screen.blit(karaZDruhyStrany2, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            casik += 1 
        
        elif p.smer == "dolu":
            if casik == 30:
                casik = 0
                screen.blit(karaZepredu, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            elif casik >= 15: screen.blit(karaZepredu, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            else: 
                screen.blit(karaZepredu2, (p.x*BLOK + (scX-rozmery("x")*BLOK)/2, p.y*BLOK + (scY-rozmery("y")*BLOK)/2  - BLOK//3,BLOK,BLOK + BLOK//3))
            casik += 1

    def hybu(self,kam):
        if kam == "nahoru":
            if mapa[self.y-1][self.x] == " " or mapa[self.y-1][self.x] == "O":
                self.y -= 1
            elif mapa[self.y-1][self.x] == "B" and mapa[self.y-2][self.x] == " ":
                mapa[self.y-1][self.x] = " "
                mapa[self.y-2][self.x] = "B"
                self.y -= 1
            elif mapa[self.y-1][self.x] == "B" and mapa[self.y-2][self.x] == "O":
                mapa[self.y-1][self.x] = " "
                mapa[self.y-2][self.x] = "X"
                self.y -= 1
            elif mapa[self.y-1][self.x] == "X" and mapa[self.y-2][self.x] == "O":
                mapa[self.y-1][self.x] = "O"
                mapa[self.y-2][self.x] = "X"
                self.y -= 1
            elif mapa[self.y-1][self.x] == "X" and mapa[self.y-2][self.x] == " ":
                mapa[self.y-1][self.x] = "O"
                mapa[self.y-2][self.x] = "B"
                self.y -= 1
        elif kam == "dolu":
            if mapa[self.y+1][self.x] == " " or mapa[self.y+1][self.x] == "O":
                self.y += 1
            elif mapa[self.y+1][self.x] == "B" and mapa[self.y+2][self.x] == " ":
                mapa[self.y+1][self.x] = " "
                mapa[self.y+2][self.x] = "B"
                self.y += 1
            elif mapa[self.y+1][self.x] == "B" and mapa[self.y+2][self.x] == "O":
                mapa[self.y+1][self.x] = " "
                mapa[self.y+2][self.x] = "X"
                self.y += 1
            elif mapa[self.y+1][self.x] == "X" and mapa[self.y+2][self.x] == "O":
                mapa[self.y+1][self.x] = "O"
                mapa[self.y+2][self.x] = "X"
                self.y += 1
            elif mapa[self.y+1][self.x] == "X" and mapa[self.y+2][self.x] == " ":
                mapa[self.y+1][self.x] = "O"
                mapa[self.y+2][self.x] = "B"
                self.y += 1
        elif kam == "doleva":
            if mapa[self.y][self.x-1] == " " or mapa[self.y][self.x-1] == "O":
                self.x -= 1
            elif mapa[self.y][self.x-1] == "B" and mapa[self.y][self.x-2] == " ":
                mapa[self.y][self.x-1] = " "
                mapa[self.y][self.x-2] = "B"
                self.x -= 1
            elif mapa[self.y][self.x-1] == "B" and mapa[self.y][self.x-2] == "O":
                mapa[self.y][self.x-1] = " "
                mapa[self.y][self.x-2] = "X"
                self.x -= 1
            elif mapa[self.y][self.x-1] == "X" and mapa[self.y][self.x-2] == "O":
                mapa[self.y][self.x-1] = "O"
                mapa[self.y][self.x-2] = "X"
                self.x -= 1
            elif mapa[self.y][self.x-1] == "X" and mapa[self.y][self.x-2] == " ":
                mapa[self.y][self.x-1] = "O"
                mapa[self.y][self.x-2] = "B"
                self.x -= 1
        elif kam == "doprava":
            if mapa[self.y][self.x+1] == " " or mapa[self.y][self.x+1] == "O":
                self.x += 1
            elif mapa[self.y][self.x+1] == "B" and mapa[self.y][self.x+2] == " ":
                mapa[self.y][self.x+1] = " "
                mapa[self.y][self.x+2] = "B"
                self.x += 1
            elif mapa[self.y][self.x+1] == "B" and mapa[self.y][self.x+2] == "O":
                mapa[self.y][self.x+1] = " "
                mapa[self.y][self.x+2] = "X"
                self.x += 1
            elif mapa[self.y][self.x+1] == "X" and mapa[self.y][self.x+2] == "O":
                mapa[self.y][self.x+1] = "O"
                mapa[self.y][self.x+2] = "X"
                self.x += 1
            elif mapa[self.y][self.x+1] == "X" and mapa[self.y][self.x+2] == " ":
                mapa[self.y][self.x+1] = "O"
                mapa[self.y][self.x+2] = "B"
                self.x += 1

def vyhra():
    for x in range(rozmery("x")):
            for y in range(rozmery("y")):
                if mapa[y][x] == "B":
                    return False
    if not aktivniMapa in levlyComplet:
        levlyComplet.append(aktivniMapa)
        data.write(str(aktivniMapa) + ",")
    return True


#####################################################################################################################


p = postava()
vyhraDelay = 0
while jede:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jede = False
        elif event.type == pygame.VIDEORESIZE:
            scX, scY = 1920, 1080
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jede = False
            elif event.key == pygame.K_SPACE and SCENA == "main menu": 
                SCENA = "levely"
            elif (event.key == pygame.K_UP or event.key == pygame.K_w) and SCENA == "hra":
                postava.hybu(p,"nahoru")
                p.smer = "nahoru"
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and SCENA == "hra":
                postava.hybu(p,"dolu")
                p.smer = "dolu"
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and SCENA == "hra":
                postava.hybu(p,"doleva")
                p.smer = "doleva"
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and SCENA == "hra":
                postava.hybu(p,"doprava")
                p.smer = "doprava"
            elif event.key == pygame.K_SPACE and SCENA == "hra":
                ctiMapu(aktivniMapa)
                p = postava()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if SCENA == "nastaveni":
                if zvukBtn.collidepoint(pygame.mouse.get_pos()):
                    click.play()
                    ZVUK = not ZVUK
                if hudbaBtn.collidepoint(pygame.mouse.get_pos()):
                    if ZVUK: click.play()
                    HUDBA = not HUDBA
                    if HUDBA: pygame.mixer.music.set_volume(0.2)
                    else: pygame.mixer.music.set_volume(0)
                if krizek.collidepoint(pygame.mouse.get_pos()):
                    if ZVUK: click.play()
                    SCENA = scenaPred
            elif SCENA == "main menu" or SCENA == "levely":
                if nastaveni.collidepoint(pygame.mouse.get_pos()):
                    if ZVUK: click.play()
                    scenaPred = SCENA
                    SCENA = "nastaveni"
                if SCENA == "levely":
                    for i in range(POCETLEVELU):
                        if levly[i+1].collidepoint(pygame.mouse.get_pos()):
                            cisloLevelu = i+1
                            ctiMapu(i+1)
                            aktivniMapa = i+1
                            SCENA = "hra"
                            p = postava()
                            break
            elif SCENA == "hra":
                if restart.collidepoint(pygame.mouse.get_pos()):
                    ctiMapu(aktivniMapa)
                    p = postava()
                elif zpet.collidepoint(pygame.mouse.get_pos()):
                    SCENA = "levely"
    
    kresli()
    if vyhra() and SCENA == "hra" or SCENA == "vyhra":
        if vyhraDelay != 120:
            SCENA = "vyhra"
            vyhraDelay += 1
        else:
            SCENA = "levely"
            vyhraDelay = 0
    
pygame.quit()