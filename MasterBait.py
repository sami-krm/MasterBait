#importation des bibliothèques
import random
import pygame
from pygame.locals import *
pygame.init()

  
# Setup Pygame
fpsClock = pygame.time.Clock()
Fenêtre_Largeur = 1366
Fenêtre_Hauteur = 768
fenêtre = pygame.display.set_mode((Fenêtre_Largeur, Fenêtre_Hauteur))
screen = pygame.display.set_mode((Fenêtre_Largeur, Fenêtre_Hauteur))
Icone = pygame.image.load("Assets/icone.png")
pygame.display.set_icon(Icone)
pygame.display.set_caption("MasterBait")

#Chargement de tous les sprites
SBackground1 = pygame.image.load("Assets/Sprites/UI/SBackground1.png").convert()
SBackground2 = pygame.image.load("Assets/Sprites/UI/SBackground2.png").convert()
SPeche1A = pygame.image.load("Assets/Sprites/UI/SPeche1.png").convert()
SPeche2A = pygame.image.load("Assets/Sprites/UI/SPeche2.png").convert()
SAmelioration = pygame.image.load("Assets/Sprites/UI/SAmélioration.png").convert()
SBVendreN = pygame.image.load("Assets/Sprites/UI/SBVendreN.png").convert_alpha()
SBVendreH = pygame.image.load("Assets/Sprites/UI/SBVendreH.png").convert_alpha()
SBAmeliorerN = pygame.image.load("Assets/Sprites/UI/SBAmeliorerN.png").convert_alpha()
SBAmeliorerH = pygame.image.load("Assets/Sprites/UI/SBAmeliorerH.png").convert_alpha()
SBBlackN = pygame.image.load("Assets/Sprites/UI/SBBlackN.png").convert_alpha()
SBBlackH = pygame.image.load("Assets/Sprites/UI/SBBlackH.png").convert_alpha()
SMoney = pygame.image.load("Assets/Sprites/UI/SMoney.png").convert_alpha()
SRideau = pygame.image.load("Assets/Sprites/UI/SRideau.png").convert_alpha()
STransparent = pygame.image.load("Assets/Sprites/UI/STransparent.png").convert_alpha()
SCanne1 = pygame.image.load("Assets/Sprites/Cannes/SCanne1.png").convert_alpha()
SCanne2 = pygame.image.load("Assets/Sprites/Cannes/SCanne2.png").convert_alpha()
SCanne3 = pygame.image.load("Assets/Sprites/Cannes/SCanne3.png").convert_alpha()
SCanne4 = pygame.image.load("Assets/Sprites/Cannes/SCanne4.png").convert_alpha()
SCanne5 = pygame.image.load("Assets/Sprites/Cannes/SCanne5.png").convert_alpha()
SCanne6 = pygame.image.load("Assets/Sprites/Cannes/SCanne6.png").convert_alpha()
SRarete1 = pygame.image.load("Assets/Sprites/UI/SRarete1.png").convert_alpha()
SRarete2 = pygame.image.load("Assets/Sprites/UI/SRarete2.png").convert_alpha()
SRarete3 = pygame.image.load("Assets/Sprites/UI/SRarete3.png").convert_alpha()
SRarete4 = pygame.image.load("Assets/Sprites/UI/SRarete4.png").convert_alpha()
SRarete5 = pygame.image.load("Assets/Sprites/UI/SRarete5.png").convert_alpha()
SRarete6 = pygame.image.load("Assets/Sprites/UI/SRarete6.png").convert_alpha()
SRarete7 = pygame.image.load("Assets/Sprites/UI/SRarete7.png").convert_alpha()
SRarete8 = pygame.image.load("Assets/Sprites/UI/SRarete8.png").convert_alpha()
SMusique = pygame.image.load("Assets/Sprites/UI/SMusique.png").convert_alpha()
SBCthulhu = pygame.image.load("Assets/Sprites/UI/Cthulhu.png").convert()
SPoissonChargementN = pygame.image.load("Assets/Sprites/UI/SPoissonChargement.png").convert_alpha()
SPoissonChargementOR = pygame.image.load("Assets/Sprites/UI/SPoissonChargementOR.png").convert_alpha()
SFBlack = pygame.image.load("Assets/Sprites/UI/SFBlack.png").convert()
SChuthuluFE = pygame.image.load("Assets/Sprites/UI/CthulhuFATALERROR.png").convert()

#Poissons normaux
SAnchois = pygame.image.load("Assets/Sprites/Poissons/Normal/SAnchois.png").convert_alpha()
SAnguille =  pygame.image.load("Assets/Sprites/Poissons/Normal/SAnguille.png").convert_alpha()
SBaleineBleue =  pygame.image.load("Assets/Sprites/Poissons/Normal/SBaleineBleue.png").convert_alpha()
SBar= pygame.image.load("Assets/Sprites/Poissons/Normal/SBar.png").convert_alpha()
SBeluga= pygame.image.load("Assets/Sprites/Poissons/Normal/SBeluga.png").convert_alpha()
SCabillaud=pygame.image.load("Assets/Sprites/Poissons/Normal/SCabillaud.png").convert_alpha()
SCachalot=pygame.image.load("Assets/Sprites/Poissons/Normal/SCachalot.png").convert_alpha()
SCalamar=pygame.image.load("Assets/Sprites/Poissons/Normal/SCalamar.png").convert_alpha()
SCarpe=pygame.image.load("Assets/Sprites/Poissons/Normal/SCarpe.png").convert_alpha()
SCarpeKoi=pygame.image.load("Assets/Sprites/Poissons/Normal/SCarpeKoi.png").convert_alpha()
SCrabe=pygame.image.load("Assets/Sprites/Poissons/Normal/SCrabe.png").convert_alpha()
SCrapet=pygame.image.load("Assets/Sprites/Poissons/Normal/SCrapet.png").convert_alpha()
SCrevette=pygame.image.load("Assets/Sprites/Poissons/Normal/SCrevette.png").convert_alpha()
SDaurade=pygame.image.load("Assets/Sprites/Poissons/Normal/SDaurade.png").convert_alpha()
SEcrevisse=pygame.image.load("Assets/Sprites/Poissons/Normal/SEcrevisse.png").convert_alpha()
SGardon=pygame.image.load("Assets/Sprites/Poissons/Normal/SGardon.png").convert_alpha()
SMorue=pygame.image.load("Assets/Sprites/Poissons/Normal/SMorue.png").convert_alpha()
SOrque=pygame.image.load("Assets/Sprites/Poissons/Normal/SOrque.png").convert_alpha()
SPerche=pygame.image.load("Assets/Sprites/Poissons/Normal/SPerche.png").convert_alpha()
SPieuvre=pygame.image.load("Assets/Sprites/Poissons/Normal/SPieuvre.png").convert_alpha()
SPoissonChat=pygame.image.load("Assets/Sprites/Poissons/Normal/SpoissonCHat.png").convert_alpha()
SRaie=pygame.image.load("Assets/Sprites/Poissons/Normal/SRaie.png").convert_alpha()
SRequinBlanc=pygame.image.load("Assets/Sprites/Poissons/Normal/SRequinBlanc.png").convert_alpha()
SRequinMako=pygame.image.load("Assets/Sprites/Poissons/Normal/SRequinMako.png").convert_alpha()
SRequinMarteau=pygame.image.load("Assets/Sprites/Poissons/Normal/SRequinMarteau.png").convert_alpha()
SRequinMartin=pygame.image.load("Assets/Sprites/Poissons/Normal/SRequinMartin.png").convert_alpha()
SRequinMartinSHINY=pygame.image.load("Assets/Sprites/Poissons/Normal/SRequinMartinSHINY.png").convert_alpha()
SRequinScie=pygame.image.load("Assets/Sprites/Poissons/Normal/SRequinScie.png").convert_alpha()
SRouget= pygame.image.load("Assets/Sprites/Poissons/Normal/SRouget.png").convert_alpha()
SRoussette=pygame.image.load("Assets/Sprites/Poissons/Normal/SRoussette.png").convert_alpha()
SSardine=pygame.image.load("Assets/Sprites/Poissons/Normal/SSardine.png").convert_alpha()
SSaumon=pygame.image.load("Assets/Sprites/Poissons/Normal/SSaumon.png").convert_alpha()
SSilure=pygame.image.load("Assets/Sprites/Poissons/Normal/SSilure.png").convert_alpha()
SThon=pygame.image.load("Assets/Sprites/Poissons/Normal/SThon.png").convert_alpha()
STruite=pygame.image.load("Assets/Sprites/Poissons/Normal/STruite.png").convert_alpha()
STurbot=pygame.image.load("Assets/Sprites/Poissons/Normal/STurbot.png").convert_alpha()
#poissons or
SAnchoisOR = pygame.image.load("Assets/Sprites/Poissons/OR/SAnchoisOR.png").convert_alpha()
SAnguilleOR =  pygame.image.load("Assets/Sprites/Poissons/OR/SAnguilleOR.png").convert_alpha()
SBaleineBleueOR =  pygame.image.load("Assets/Sprites/Poissons/OR/SBaleineBleueOR.png").convert_alpha()
SBarOR= pygame.image.load("Assets/Sprites/Poissons/OR/SBarOR.png").convert_alpha()
SBelugaOR= pygame.image.load("Assets/Sprites/Poissons/OR/SBelugaOR.png").convert_alpha()
SCabillaudOR=pygame.image.load("Assets/Sprites/Poissons/OR/SCabillaudOR.png").convert_alpha()
SCachalotOR=pygame.image.load("Assets/Sprites/Poissons/OR/SCachalotOR.png").convert_alpha()
SCalamarOR=pygame.image.load("Assets/Sprites/Poissons/OR/SCalamarOR.png").convert_alpha()
SCarpeOR=pygame.image.load("Assets/Sprites/Poissons/OR/SCarpeOR.png").convert_alpha()
SCarpeKoiOR=pygame.image.load("Assets/Sprites/Poissons/OR/SCarpeKoiOR.png").convert_alpha()
SCrabeOR=pygame.image.load("Assets/Sprites/Poissons/OR/SCrabeOR.png").convert_alpha()
SCrapetOR=pygame.image.load("Assets/Sprites/Poissons/OR/SCrapetOR.png").convert_alpha()
SCrevetteOR=pygame.image.load("Assets/Sprites/Poissons/OR/SCrevetteOR.png").convert_alpha()
SDauradeOR=pygame.image.load("Assets/Sprites/Poissons/OR/SDauradeOR.png").convert_alpha()
SEcrevisseOR=pygame.image.load("Assets/Sprites/Poissons/OR/SEcrevisseOR.png").convert_alpha()
SGardonOR=pygame.image.load("Assets/Sprites/Poissons/OR/SGardonOR.png").convert_alpha()
SMorueOR=pygame.image.load("Assets/Sprites/Poissons/OR/SMorueOR.png").convert_alpha()
SOrqueOR=pygame.image.load("Assets/Sprites/Poissons/OR/SOrqueOR.png").convert_alpha()
SPercheOR=pygame.image.load("Assets/Sprites/Poissons/OR/SPercheOR.png").convert_alpha()
SPieuvreOR=pygame.image.load("Assets/Sprites/Poissons/OR/SPieuvreOR.png").convert_alpha()
SPoissonChatOR=pygame.image.load("Assets/Sprites/Poissons/OR/SpoissonCHatOR.png").convert_alpha()
SRaieOR=pygame.image.load("Assets/Sprites/Poissons/OR/SRaieOR.png").convert_alpha()
SRequinBlancOR=pygame.image.load("Assets/Sprites/Poissons/OR/SRequinBlancOR.png").convert_alpha()
SRequinMakoOR=pygame.image.load("Assets/Sprites/Poissons/OR/SRequinMakoOR.png").convert_alpha()
SRequinMarteauOR=pygame.image.load("Assets/Sprites/Poissons/OR/SRequinMarteauOR.png").convert_alpha()
SRequinMartinOR=pygame.image.load("Assets/Sprites/Poissons/OR/SRequinMartinOR.png").convert_alpha()
SRequinMartinSHINYOR=pygame.image.load("Assets/Sprites/Poissons/OR/SRequinMartinSHINYOR.png").convert_alpha()
SRequinScieOR=pygame.image.load("Assets/Sprites/Poissons/OR/SRequinScieOR.png").convert_alpha()
SRougetOR= pygame.image.load("Assets/Sprites/Poissons/OR/SRougetOR.png").convert_alpha()
SRoussetteOR=pygame.image.load("Assets/Sprites/Poissons/OR/SRoussetteOR.png").convert_alpha()
SSardineOR=pygame.image.load("Assets/Sprites/Poissons/OR/SSardineOR.png").convert_alpha()
SSaumonOR=pygame.image.load("Assets/Sprites/Poissons/OR/SSaumonOR.png").convert_alpha()
SSilureOR=pygame.image.load("Assets/Sprites/Poissons/OR/SSilureOR.png").convert_alpha()
SThonOR=pygame.image.load("Assets/Sprites/Poissons/OR/SThonOR.png").convert_alpha()
STruiteOR=pygame.image.load("Assets/Sprites/Poissons/OR/STruiteOR.png").convert_alpha()
STurbotOR=pygame.image.load("Assets/Sprites/Poissons/OR/STurbotOR.png").convert_alpha()



#Audios
M1 = ("Assets/Audio/Musiques/Anchois Lullaby.ogg", "Anchois Lullaby")
M2 = ("Assets/Audio/Musiques/Fishing Day.ogg", "Fishing Day")
M3 = ("Assets/Audio/Musiques/Golden Squid.ogg", "Golden Squid")
M4 = ("Assets/Audio/Musiques/Hell Lion.ogg", "Hell Lion")
M5 = ("Assets/Audio/Musiques/Jazz Zone.ogg", "Jazz Zone")
M6 = ("Assets/Audio/Musiques/Old Sport.ogg", "Old Sport")
M7 = ("Assets/Audio/Musiques/Reeling.ogg", "Reeling")
M8 = ("Assets/Audio/Musiques/Rivage Martin.ogg", "Rivage Martin")
M9 = ("Assets/Audio/Musiques/Sables Chaud.ogg", "Sables Chaud")
M10 = ("Assets/Audio/Musiques/Saumon Louche.ogg", "Saumon Louche")
M11 = ("Assets/Audio/Musiques/Sweet Cabillaud.ogg", "Sweet Cabillaud")
M12 = ("Assets/Audio/Musiques/Thousand Seas.ogg", "Thousand Seas")
M13 = ("Assets/Audio/Musiques/Turbot Mode.ogg", "Turbot Mode")
M14 = ("Assets/Audio/Musiques/Peche a la mouche.ogg", "Pêche à la Mouche")
Doomsnight = ("Assets/Audio/Musiques/Doomsnight.ogg", "Doomsnight")
LastSquid = pygame.mixer.Sound("Assets/Audio/Musiques/Last Squid.ogg")
# Création de la playlist d'ambiance aléatoire
Playlist = [M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14]
random.shuffle(Playlist)
PisteVague = pygame.mixer.Channel(0)
PisteVague.set_volume(0.3)
SonVagues = pygame.mixer.Sound("Assets/Audio/SFX/SFXVagues.wav")
SonPeche = pygame.mixer.Sound("Assets/Audio/SFX/SFXPeche.wav")
SonAchat = pygame.mixer.Sound("Assets/Audio/SFX/SFXAchat.wav")
SonWin = pygame.mixer.Sound("Assets/Audio/SFX/SFXWin.wav")
SonWin.set_volume(0.6)
SonLose = pygame.mixer.Sound("Assets/Audio/SFX/SFXLose.wav")
SonLose.set_volume(0.2)
SonCthulhu = pygame.mixer.Sound("Assets/Audio/SFX/SFXCthulhu.wav")
SonFatalError = pygame.mixer.Sound("Assets/Audio/SFX/SFXToo_Late.ogg")

# Fonts
pygame.font.init()
pygame.font.Font("Assets/Font/IntroRust-Base.otf", 12)


#Création des classes pour pygame et pour le jeu
# Boutons
class bouton:
  def __init__(self, pos, imageN, imageH, scale):
    hauteur = imageN.get_height()
    largeur = imageN.get_width()
    self.imageN = pygame.transform.scale(imageN, (int(largeur * scale), int(hauteur * scale)))
    self.imageH = pygame.transform.scale(imageH, (int(largeur * scale), int(hauteur * scale)))
    self.rect = self.imageN.get_rect()
    self.rect.topleft = (pos)
    self.clicked = False  
    self.hover = False
  def update(self):
        self.clicked = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if clic:
                self.image = self.imageN
                self.hover = False
            else:
                self.image = self.imageH
                if clic_relache:
                    self.clicked = True
                self.hover = True
        else:
            self.image = self.imageN
            self.hover = False
        screen.blit(self.image, (self.rect.topleft))
clic=False
clic_relache = False

class scene:
  def __init__(self, image, scale):
    hauteur = image.get_height()
    largeur = image.get_width()
    self.image = pygame.transform.scale(image, (int(largeur * scale), int(hauteur * scale)))
  def draw(self):
    screen.blit(self.image,(0,0))
    
class élément_visuel:  
    def __init__(self, image, pos, scale):
        hauteur = image.get_height()
        largeur = image.get_width()
        self.image = pygame.transform.scale(image, (int(largeur * scale), int(hauteur * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos
    def draw(self):
        screen.blit(self.image,(self.rect.center))
        
        
    
class Pole():
    def __init__(self,quality):
        self.quality = quality #int
    def upgrade(self):
            self.quality+=1
    def downgrade(self):
            self.quality-=1
            return True
    def fish(self):
        global prise
        global fish_bonus
        fish_bonus = random.randint(1,100)
        if self.quality == 1:
            prise = random.choices(sea1, weights=wsea1)[0]
        if self.quality == 2 :
            prise = random.choices(sea2, weights=wsea2)[0]
        if self.quality == 3 :
            prise = random.choices(sea3, weights=wsea3)[0]
        if self.quality == 4 :
            prise = random.choices(sea4, weights=wsea4)[0]
        if self.quality == 5 :
            prise = random.choices(sea5, weights=wsea5)[0]
        if self.quality == 6 :
            prise = random.choices(sea6, weights=wsea6)[0]


#Création de la classe espèce qui contient les données de chaque espèce et la méthode de calcul du poids et du prix lorsque le poisson est attrapé
class Species():
    def __init__(self,name,quality,weight_range,base_price,rarity, spriteN, spriteOR):
        self.name = name #string
        self.quality = quality #int
        self.weight_range = weight_range #tuple
        self.base_price = base_price #int
        self.rarity = rarity #int
        self.sell_price = 0 #float
        self.spriteN =  pygame.transform.scale(spriteN, (750,750))
        self.spriteOR = pygame.transform.scale(spriteOR, (750,750))
    def caught(self):
        self.weight = round(random.uniform(self.weight_range[0],self.weight_range[1]),3) #Attribue un poids aléatoire dans la range possible du poisson
        self.weight_factor = self.weight/self.weight_range[1] #Donne un indice de poids de 0 à 1 où 1 est le poids maximal du poisson et 0 le minimal
        self.sell_price = round(self.base_price+((self.base_price/5)*self.weight_factor),2) #Calcul du prix de vente (prix de base + 20% du prix de base * l'indicateur de poid)
        if fish_bonus > 95 :
            self.est_or = True
            self.sprite = self.spriteOR
            self.sell_price = round(self.sell_price*3,2)
        else:
            self.est_or = False
            self.sprite = self.spriteN
    def draw(self):
        screen.blit(self.sprite,(0,100))

#Initilaisation des instances d'espèces pêchables
Anchois = Species("Anchois", 1, (0.015, 0.025), 7, 1, SAnchois, SAnchoisOR)
Crevette = Species("Crevette", 1, (0.003, 0.015), 9, 1, SCrevette, SCrevetteOR)
Crapet = Species("Crapet", 1, (0.650, 0.900), 30, 1, SCrapet, SCrapetOR)
Crabe = Species("Crabe commun", 1, (0.250, 0.500), 20, 1, SCrabe, SCrabeOR)
Sardine = Species("Sardine", 1, (0.010, 0.030), 10, 1, SSardine, SSardineOR)
Bar = Species("Bar", 1, (0.300, 0.500), 20, 1, SBar, SBarOR)
Poisson_chat = Species("Poisson-chat", 1, (0.450, 0.910), 25, 1, SPoissonChat, SPoissonChatOR)
Cabillaud = Species("Cabillaud", 1, (0.800, 1.200),50, 2, SCabillaud, SCabillaudOR)

Perche = Species("Perche", 2, (2.350, 2.780), 30, 2, SPerche, SPercheOR)
Roussette = Species("Roussette", 2, (2.800, 3.120), 50, 2, SRoussette, SRoussetteOR)
Gardon = Species("Gardon", 2, (0.400, 0.570), 25, 1, SGardon, SGardonOR)
Rouget = Species("Rouget", 2, (0.430, 0.670), 60, 2, SRouget, SRougetOR)
Daurade = Species("Daurade", 2, (0.900, 2.400), 70, 3, SDaurade, SDauradeOR)
Anguille = Species("Anguille", 2, (2.580, 3.260), 80, 3, SAnguille, SAnguilleOR)
Ecrevisse = Species("Ecrevisse", 2, (0.050, 0.150), 90, 3, SEcrevisse, SEcrevisseOR)

Calamar = Species("Calamar",3, (0.300, 0.700),100, 3, SCalamar, SCalamarOR)
Carpe = Species("Carpe", 3, (2,3), 150, 3, SCarpe, SCarpeOR)
Truite = Species("Truite", 3,  (0.500, 2), 100, 3, STruite, STruiteOR)
Thon = Species("Thon", 3, (50,200), 500, 4, SThon, SThonOR)
Silure = Species("Silure", 3, (30,100.0), 300, 4, SSilure, SSilureOR)
Saumon = Species("Saumon", 3, (3.5,5),200, 3, SSaumon, SSaumonOR)

RequinMartin = Species("Requin-Martin", 4, (84,84), 1, 7, SRequinMartin, SRequinMartinOR)
RequinMartinShiny = Species("Requin-Martin SHINY", 4, (142,142), 2, 8, SRequinMartinSHINY, SRequinMartinSHINYOR)
Morue = Species("Morue", 4, (35.5,42), 150, 3, SMorue, SMorueOR)
Turbot = Species("Turbot", 4, (10.5,15), 200, 3, STurbot, STurbotOR)
CarpeKoi = Species("Carpe Koï", 4, (5.7, 8.9), 300, 4, SCarpeKoi, SCarpeKoiOR)
RaieManta = Species("Raie Manta", 4, (1000,2000), 1000, 5, SRaie, SRaieOR)
Pieuvre = Species("Pieuvre", 4, (20.5,50), 500, 4, SPieuvre, SPieuvreOR)

RequinMarteau = Species("Requin-Marteau", 5, (80.5,90), 2000, 5, SRequinMarteau, SRequinMarteauOR)
RequinScie = Species("Requin-Scie", 5, (2.5,6), 1000, 5, SRequinScie, SRequinScieOR)
RequinMako = Species("Requin Mako", 5, (60,140), 3000, 5, SRequinMako, SRequinMakoOR)
RequinBlanc = Species("Requin Blanc", 5, (680.0,1100), 5000, 6, SRequinBlanc, SRequinBlancOR)
Cachalot = Species("Cachalot", 5, (35000,45000), 8500, 6, SCachalot, SCachalotOR)
Orque = Species("Orque", 5, (3000,4000), 6000, 6, SOrque, SOrqueOR)
Beluga = Species("Béluga", 5, (1100,1600), 1500, 5, SBeluga, SBelugaOR)
BaleineBleue = Species("Baleine Bleue", 5, (130000,150000), 10000, 6, SBaleineBleue, SBaleineBleueOR)

Chtulhu = Species("CHTULU", 6, (1000000,1000000), 0, 7, SAnchois, SAnchoisOR)

#Fonctions pour la fin du jeu
SBCthulhu = pygame.transform.scale_by(SBCthulhu,(0.71,0.71))
BLACK=(0,0,0)
def BlendSurface(image, alpha):
    image.set_alpha(min(1.0,alpha)*255)
    screen.blit(SBCthulhu,(0,0))

clock = pygame.time.Clock()

def ending():
    i = 0
    done = False
    while not done:
        clock.tick(60)
        i += 1
        if i > 200:
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)
        BlendSurface(SBCthulhu, i/200) 
        pygame.display.flip()
    ChuthuluFE.draw()
    PisteVague.play(SonFatalError)
    check=True
    pygame.display.flip()
    # Cette partie modifie le fichier save.txt pour simuler une corruption par Cthulu
    données = [
    "-1",
    "Alors que vous lancez la ligne, vous ne pouvez vous empêcher de sentir dans vos tripes que cela sera votre dernier lancé.",
    "Vous voyez le bouchon s'éloigner plus loin qu'il n'était jamais allé, à l'endroit où mer et ciel ne font qu'un. Vous hameçonnez l'océan et sentez la mer mordre.",
    "Les vagues se déchaînent alors que vous remontez votre prise. La violence de la mer vous surprend, le poisson n'a pas l'air d'essayer de résister. C'est alors que vous vous apercevez que vous n'avez pas péché un simple poisson.",
    "Ce que vous remontez n'a rien de naturel, et le grondement sourd et bas que cette chose émet confirme votre plus grande peur. Vous sentez votre cœur s'engouffrer dans le vide béant qu'est la peur qui s'accumule à mesure où votre prise se découvre du drap tumultueux que sont les vagues de l'océan.",
    "Vous le savez maintenant, il est trop tard, votre insatisfaction permanente vous a mené ici. Vous ne tirez plus sur la canne, la créature se lève d'elle même.",
    "Ses yeux se découvrent et montrent un abysse sans fond, tirant et luttant pour arracher votre âme à mesure où vous les regardez. La chose que vous regardez n'a pas de taille, elle déforme l'espace autour d'elle. Plus la créature émerge, plus vous vous sentez petit.",
    "Vous l'entendez, elle parle. À travers votre tétanie, vous entendez ces mots:",
    "",
    "Mgr'luh, Y' ah Cthulhu, throdog ph' hup shagg r'lyeih, ilyaa hafh’drn l' uln ya.",
    "Ymg', ahf' mgepuln, Y' ahor ymg' goka gotha. Ymg' vulgtlagln ymg' r'luhhor llll vulgtmnah ot zhro ymg' mnahn'  lw'nafh, Y' ahor h' goka.",
    "Mg, Y' ahor ulnah shugg llll ymg' vulgtmm ng turn fahf shuggog ph'nglui shogg, ah'mgehye nilgh'ri ymg' ehye mgepkadishtu.",
    "",
    "Observe, je suis Cthulhu, le Grand Au-Delà du domaine des rêves de R’Lyeih, attendant l’appel d’un invocateur.",
    "Toi, qui m’a appelé, je t’accorde un voeu. Tu pries ton dieu pour une fin clémente à ta vie sans valeur, je peux te l’accorder.",
    "Cependant, je revendiquerai la Terre pour tes prières et transformerai ce monde en un royaume de ténèbres, détruisant tout ce que tu connais."]
    with open("save.txt", "w") as s:
        s.write('\n'.join(données))
    while check:
        if not PisteVague.get_busy():
            pygame.QUIT
            check=False
            return
    
    


#Retrouver les données sauvegardées dans le fichier save.txt dans le cas où la première ligne n'est pas "-1" (cas de la corruption)
with open("save.txt","r") as s:
    indicERREUR = int(s.readline())
if indicERREUR == -1:
    ERREUR = True
else:
    ERREUR = False

if not ERREUR:
    with open("save.txt","r") as s:
        global money
        global AnchoisCounter
        money = int(s.readline())
        lvl = int(s.readline())
        AnchoisCounter = int(s.readline())
    canne = Pole(lvl)

#Creation des instances
#Backgrounds
BBackground1 = scene(SBackground1,0.36)
BBackground2 = scene(SBackground2,0.72)
BPeche1 = scene(SPeche1A,0.72)
BPeche2 = scene(SPeche2A,0.72)
BAmelioration = scene(SAmelioration,0.72)
BCthulhu = scene(SBCthulhu,0.72)
BBlack = scene(SFBlack,0.72)
ChuthuluFE = scene(SChuthuluFE,0.72)

#UI
UMoney = élément_visuel(SMoney, (10,75), 0.35)
URarete1 = élément_visuel(SRarete1, (740,235), 0.7)
URarete2 = élément_visuel(SRarete2, (740,235), 0.7)
URarete3 = élément_visuel(SRarete3, (740,235), 0.7)
URarete4 = élément_visuel(SRarete4, (740,235), 0.7)
URarete5 = élément_visuel(SRarete5, (740,235), 0.7)
URarete6 = élément_visuel(SRarete6, (740,235), 0.7)
URarete7 = élément_visuel(SRarete7, (740,235), 0.7)
URarete8 = élément_visuel(SRarete8, (740,235), 0.7)



#Boutons
BPecher = bouton((0,140), STransparent,STransparent, 4)
BVendre = bouton((725,420), SBVendreN, SBVendreH, 0.6)
BVendreBlack = bouton((715,600), SBBlackN, SBBlackH, 0.6)
BAmeliorer = bouton((840,20),SBAmeliorerN, SBAmeliorerH, 0.6)


F32 = pygame.font.Font("Assets/Font/IntroRust-Base.otf", 32)
F45 = pygame.font.Font("Assets/Font/IntroRust-Base.otf", 45)
F60 = pygame.font.Font("Assets/Font/IntroRust-Base.otf", 60)


##############################################################################################################################
#Ces  tuples contiennent les probabilités de pêche pour chaque poisson selon le niveau de la canne à pêche, en pourcentage.
#Chaque niveau contient d'abord un tuple des poissons disponibles, puis un tuple des probabilités associés, les deux tuples sont utilisés dans la méthode fish de la classe pole.
#Cette partie prend beaucoup de lignes pour une meilleure lisibilité.

#Niveau 1
sea1 = (Anchois,Crevette,Crapet,Crabe,Sardine,Bar,Poisson_chat,Cabillaud)
wsea1 = (
    40, #Anchois
    10, #Crevette
    10, #Crapet de roche
    5, #Crabe
    5, #Sardine
    10, #Bar
    10, #Poisson-chat
    10, #Cabillaud
)
#Niveau 2
sea2 = (Anchois,Crevette,Crapet,Crabe,Sardine,Bar,Poisson_chat,Cabillaud,Perche,Roussette,Gardon,Rouget,Daurade, Anguille, Ecrevisse)
wsea2 = (
    35, #Anchois
    5, #Crevette
    5, #Crapet de roche
    4, #Crabe
    4, #Sardine
    5, #Bar
    5, #Poisson-chat
    5, #Cabillaud
    6, #Perche
    5, #Roussette
    7, #Gardon
    5, #Rouget
    4, #Daurade
    3, #Anguille
    2, #Ecrevisse
)
#Niveau 3
sea3 = (Anchois,Crevette,Crapet,Crabe,Sardine,Bar,Poisson_chat,Cabillaud,Perche,Roussette,Gardon,Rouget,Daurade, Anguille, Ecrevisse, Calamar, Carpe, Truite, Thon, Silure, Saumon)
wsea3 = (
    30, #Anchois
    3, #Crevette
    3, #Crapet de roche
    4, #Crabe
    4, #Sardine
    3, #Bar
    3, #Poisson-chat
    5, #Cabillaud
    5, #Perche
    5, #Roussette
    5, #Gardon
    5, #Rouget
    4, #Daurade
    3, #Anguille
    2, #Ecrevisse
    3, #Calamar
    3, #Carpe
    3, #Truite
    1, #Thon
    2, #Silure
    4, #Saumon
)
#Niveau 4
sea4 = (Anchois,Crevette,Crapet,Crabe,Sardine,Bar,Poisson_chat,Cabillaud,Perche,Roussette,Gardon,Rouget,Daurade, Anguille, Ecrevisse, Calamar, Carpe, Truite, Thon, Silure, Saumon, RequinMartin, RequinMartinShiny, Morue, Turbot, CarpeKoi, RaieManta, Pieuvre)
wsea4 = (
    25, #Anchois
    3, #Crevette
    3, #Crapet de roche
    3, #Crabe
    3, #Sardine
    3, #Bar
    3, #Poisson-chat
    4, #Cabillaud
    4, #Perche
    4, #Roussette
    4, #Gardon
    4, #Rouget
    3, #Daurade
    3, #Anguille
    2, #Ecrevisse
    3, #Calamar
    3, #Carpe
    3, #Truite
    1, #Thon
    2, #Silure
    4, #Saumon
    0.04, #Requin-Martin
    0.0001, #Requin-Martin Shiny
    4, #Morue
    4, #Turbot
    3, #Carpe Koi
    0.4, #Raie Manta
    1.5599, #Pieuvre
)
#Niveau 5
sea5 = (Anchois,Crevette,Crapet,Crabe,Sardine,Bar,Poisson_chat,Cabillaud,Perche,Roussette,Gardon,Rouget,Daurade,Anguille,Ecrevisse,Calamar,Carpe,Truite,Thon,Silure,Saumon,RequinMartin,RequinMartinShiny,Morue,Turbot,CarpeKoi,RaieManta,Pieuvre,RequinMarteau,RequinScie,RequinMako,RequinBlanc,Cachalot,Orque,Beluga,BaleineBleue)
wsea5 = (
    20, #Anchois
    3, #Crevette
    3, #Crapet de roche
    3, #Crabe
    3, #Sardine
    3, #Bar
    3, #Poisson-chat
    3, #Cabillaud
    3, #Perche
    3, #Roussette
    4, #Gardon
    3, #Rouget
    3, #Daurade
    3, #Anguille
    2, #Ecrevisse
    3, #Calamar
    3, #Carpe
    3, #Truite
    3, #Thon
    3, #Silure
    4, #Saumon
    0.04, #Requin-Martin
    0.0001, #Requin-Martin Shiny
    3, #Morue
    3, #Turbot
    4, #Carpe Koi
    1.4, #Raie Manta
    2.5559, #Pieuvre
    0.5, #Requin-Marteau
    1.5, #Requin-Scie
    0.5, #Requin Mako
    0.3, #Requin Blanc
    0.2, #Cachalot
    0.7, #Orque
    1, #Béluga
    0.3, #Baleine Bleue
)
#Niveau 6
sea6 = (Anchois,Crevette,Crapet,Crabe,Sardine,Bar,Poisson_chat,Cabillaud,Perche,Roussette,Gardon,Rouget,Daurade,Anguille,Ecrevisse,Calamar,Carpe,Truite,Thon,Silure,Saumon,RequinMartin,RequinMartinShiny,Morue,Turbot,CarpeKoi,RaieManta,Pieuvre,RequinMarteau,RequinScie,RequinMako,RequinBlanc,Cachalot,Orque,Beluga,BaleineBleue,Chtulhu)
wsea6 = (
    19.8, #Anchois
    3, #Crevette
    3, #Crapet de roche
    3, #Crabe
    3, #Sardine
    3, #Bar
    3, #Poisson-chat
    3, #Cabillaud
    3, #Perche
    3, #Roussette
    4, #Gardon
    3, #Rouget
    3, #Daurade
    3, #Anguille
    2, #Ecrevisse
    3, #Calamar
    3, #Carpe
    3, #Truite
    3, #Thon
    3, #Silure
    4, #Saumon
    0.04, #Requin-Martin
    50, #Requin-Martin Shiny
    3.2, #Morue
    3, #Turbot
    4, #Carpe Koi
    1.4, #Raie Manta
    2.5599, #Pieuvre
    0.5, #Requin-Marteau
    1.5, #Requin-Scie
    0.5, #Requin Mako
    0.3, #Requin Blanc
    0.3, #Cachalot
    0.6, #Orque
    0.8, #Béluga
    0.3, #Baleine Bleue
    0.2, #Chtulhu
)
##############################################################################################################################
 
# Création des textes fixes       
TextTuto = F45.render("Cliquez pour pêcher", True, (255,255,255), None)
TextOuBlack = F32.render("ou", True, (255,255,255), None)
     
# Fonction de jeu principale
def main():
    # Attribution des variables de jeu importantes
    global prise
    global clic
    global clic_relache
    global money
    global AnchoisCounter
    SpriteCanne = [None, SCanne1, SCanne2, SCanne3, SCanne4, SCanne5, SCanne6]
    Background = BBackground1
    running=True
    clock = pygame.time.Clock()
    clock.tick(60)
    etat="default"
    PlaylistProgress = 0
    SonEnCours = Playlist[PlaylistProgress]
    pygame.mixer.music.load(SonEnCours[0])
    pygame.mixer.music.play()
    SonTitre = SonEnCours[1]
    PisteVague.play(SonVagues, -1)
    while running:
        # Cette partie permet d'écrire dans le fichier texte de sauvegarde pendant la partie
        données = [str(money), str(canne.quality), str(AnchoisCounter),"","TRICHE INTERDITE !!!!!!","Ordre des données pour pouvoir tricher plus facilement (et valeur initiale):","Argent (0)", "Niveau de la canne à pêche de 1 à 6 (1)","Compteur d'anchois (0)", "","Vous devez fermer le jeu avant de modifier les données", "","Merci de jouer à notre jeu :)"]
        with open("save.txt", "w") as s:
            s.write('\n'.join(données))
            
        # Cette partie permet de gérer la playlist aléatoire en chargeant le son suivant quand le précédant est fini
        if not pygame.mixer.music.get_busy():
            if PlaylistProgress >= len(Playlist)-1:
                PlaylistProgress = 0
            else :
                PlaylistProgress += 1
            pygame.mixer.music.unload()
            SonEnCours = Playlist[PlaylistProgress]
            SonTitre = SonEnCours[1]
            pygame.mixer.music.load(SonEnCours[0])
            pygame.mixer.music.play()
         
        # Cette partie gère les inputs du joueur   
        for event in pygame.event.get() :
            clic_relache = False
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clic = True
                clic_relache = False
            if event.type == pygame.MOUSEBUTTONUP and clic == True:
                clic = False
                clic_relache = True
            elif event.type == pygame.MOUSEBUTTONUP:
                clic = False
                clic_relache = False
        
        # Création des textes mouvants
        TextMoney = F32.render((str(round(money))+" $"),True,(0,0,0),None)
        TextMusique = F32.render(("En lecture - " + SonTitre), True, (255, 255, 255), None)
        TextAnchoisCounter = F32.render(("Anchois pêchés en tout : " + str(AnchoisCounter)), True, (255,255,255), None)
        
        # Changement du background et du prix selon le niveau de la canne à pêche
        if canne.quality != 6:
            Background = BBackground1
            BPeche = BPeche1
        else :
            Background = BBackground2
            BPeche = BPeche2
        if canne.quality < 2:
            prix = 500
        elif canne.quality < 3:
            prix = 2000
        elif canne.quality < 4:
            prix = 5000
        elif canne.quality < 5:
            prix = 15000
        elif canne.quality < 6 :
            prix = 100000
        
        #Début des différents états du jeu, ces fonctions s'exécutent selon l'état du jeu
        #Les états transit se jouent une seule fois avant de reprendre la boucle
        
        #Etat default : écran de base entre les prises, affiche la canne à pêche, le bouton pour l'améliorer, l'argent du joueur et la musique en cours de lecture
        if etat=="default":
            Background.draw()
            screen.blit(SMusique,(20,25))
            screen.blit(TextMusique,(70,30))
            UCanne = élément_visuel(SpriteCanne[canne.quality], (800, 150), 1.1)
            UCanne.draw()
            URideau = élément_visuel(SRideau,(-90,650),0.75)
            URideau.draw()
            UMoney.draw()
            screen.blit(TextMoney,(30,95))
            screen.blit(TextTuto, (60, 400))
            # Afficher le bouton d'amélioration dans le cas où la canne n'est pas niveau 6
            if canne.quality != 6:
                BAmeliorer.update()
                TextPrix = F32.render(((str(prix))+" $"), True, (0, 0, 0), None)
                screen.blit(TextPrix,(1070,106))
                if BAmeliorer.clicked:
                    if money>=prix:
                        SonAchat.play()
                        etat="TransitAmelioration"
            BPecher.update()
            # Passer à l'état de transition pêche si le joueu clique au milieu de l'écran
            if BPecher.clicked:
                clic_relache = False
                SonPeche.play()
                etat = "TransitPeche"
        
        # état transitpeche : permet d'animer le rideau de transition entre l'état défault et l'état pêche, de piocher une prise au hasard selon les probas d'animer le poisson de chargement aléatoirement.
        if etat == "TransitPeche":
            # Monter le rideau de pêche pour qu'il couvre l'écran
            yrideau=650
            # Cette boucle va faire monter le rideau petit à petit tout en continuant à afficher l'écran de pêche principal
            while yrideau > -370:
                yrideau-=30
                if yrideau> -280:
                    Background.draw()
                else:
                    BPeche.draw()
                screen.blit(SMusique,(20,25))
                screen.blit(TextMusique,(70,30))
                UCanne = élément_visuel(SpriteCanne[canne.quality], (800, 150), 1.1)
                UCanne.draw()
                UMoney.draw()
                screen.blit(TextMoney,(30,95))
                if canne.quality != 6:
                    BAmeliorer.update()
                    TextPrix = F32.render(((str(prix))+" $"), True, (0, 0, 0), None)
                    screen.blit(TextPrix,(1070,106))
                URideau = élément_visuel(SRideau,(-90,yrideau),0.75)
                URideau.draw()
                pygame.display.flip()
            
            # L'écran est couvert par le rideau, on en profite pour piocher le poisson attrapé
            canne.fish()
            prise.caught()
            if prise != Chtulhu:
                if prise == Anchois:
                        AnchoisCounter+=1
                if prise.rarity == 1:
                    rarity = URarete1
                if prise.rarity == 2:
                    rarity = URarete2
                if prise.rarity == 3:
                    rarity = URarete3
                if prise.rarity == 4:
                    rarity = URarete4
                if prise.rarity == 5:
                    rarity = URarete5
                if prise.rarity == 6:
                    rarity = URarete6
                if prise.rarity == 7:
                    rarity = URarete7
                if prise.rarity == 8:
                    rarity = URarete8
                if prise.rarity >= 4:
                    blackmarket=True
                else:
                    blackmarket=False
                # Après avoir récupéré les informations sur la prise, on prépare les textes de l'écran pêche
                TextPrise = F60.render(str(prise.name), True, (255, 255, 255), None)
                TextVendre = F45.render(("Vendre : " + str(round(prise.sell_price))+" $"), True, (0,0,0), None)
                TextPoids = F32.render((str(prise.weight) + " kg"),True, (255,255,255), None)
                #Cette partie va définir le sprite et la taille du poisson de chargement selon les informations de la prise attrapée pour donner un indice discret au joueur
                URideau = élément_visuel(SRideau,(-90,-370),0.75)
                URideau.draw()
                xpoisson = -100
                ypoisson = random.uniform(100,400)
                vitesse = random.choice((5,7,10,15,20))
                tailles = (0.5, 0.7, 0.85, 1, 1.2, 1.35, 1.5, 2)
                taille = tailles[prise.rarity-1] #La taille varie selon la rareté du poisson
                if prise.est_or: #Le sprite prend une version jaune si la prise est en or
                    SPoissonChargement = pygame.transform.scale(SPoissonChargementOR, (int(SPoissonChargementOR.get_width() * taille), int(SPoissonChargementOR.get_height() * taille)))
                else:
                    SPoissonChargement = pygame.transform.scale(SPoissonChargementN, (int(SPoissonChargementN.get_width() * taille), int(SPoissonChargementN.get_height() * taille)))
                while xpoisson < 1400:
                    xpoisson+=vitesse
                    URideau.draw()
                    screen.blit(SPoissonChargement, (xpoisson, ypoisson))
                    pygame.display.flip()
                
                # Après passage du poisson de chargement on relève le rideau et on affiche l'écran de pêche
                while yrideau > -1070:
                    yrideau-=40
                    BPeche.draw()
                    prise.draw()
                    rarity.draw()
                    screen.blit(TextPrise, (770,160))
                    screen.blit(TextPoids, (890,370))
                    BVendre.update()
                    screen.blit(TextVendre, (745,460))
                    if prise == Anchois:
                        screen.blit(TextAnchoisCounter,(720,560))
                    if blackmarket:
                        BVendreBlack.update()
                        screen.blit(TextOuBlack,(950,560))
                    UMoney.draw()
                    screen.blit(TextMoney,(30,95))
                    URideau = élément_visuel(SRideau,(-90,yrideau),0.75)
                    URideau.draw()
                    pygame.display.flip()
                BVendre.clicked = False
                etat = "peche"
            
            # Si la prise est Cthulu, lancer la fin du jeu
            else:
                SonCthulhu.play()
                etat = "Cthulhu"
                
        # Etat de pêche, dessine toutes les infos et les boutons de l'écran de pêche
        if etat =="peche":
            for event in pygame.event.get() :
                clic_relache = False
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clic = True
                    clic_relache = False
                if event.type == pygame.MOUSEBUTTONUP and clic == True:
                    clic = False
                    clic_relache = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    clic = False
                    clic_relache = False
            BPeche.draw()
            prise.draw()
            rarity.draw()
            screen.blit(TextPrise, (770,160))
            screen.blit(TextPoids, (890,370))
            BVendre.update()
            screen.blit(TextVendre, (745,460))
            if prise == Anchois:
                screen.blit(TextAnchoisCounter,(720,560))
            if blackmarket:
                BVendreBlack.update()
                screen.blit(TextOuBlack,(950,560))
            UMoney.draw()
            screen.blit(TextMoney,(30,95))
            URideau = élément_visuel(SRideau,(-90,-1070),0.75)
            URideau.draw()
            # Si la prise est vendue, on met à jouur l'argent et on passe à l'état TransitRetour
            if BVendre.clicked:
                clic_relache = False
                money+=round(prise.sell_price)
                etat="TransitRetour"
            # Si la prise est vendue au marché noir, 1 chance sur 2 de quitte ou double le prix de vente, jouer un son selon la réussite et passage à l'état TransitRetour
            if BVendreBlack.clicked:
                clic_relache = False
                reussite=random.choice((True,False))
                if reussite:
                    money+=(round(prise.sell_price)*2)
                    SonWin.play()
                else:
                    SonLose.play()
                etat="TransitRetour"
        
        # Cette état fait le lien entre l'état de pêche et l'état default, on lève le rideau en affichant l'écran de pêche en arrière plan
        if etat == "TransitRetour":
            TextMoney = F32.render((str(round(money))+" $"),True,(0,0,0),None)
            yrideau=-1070
            while yrideau < -100:
                yrideau +=40
                BPeche.draw()
                prise.draw()
                rarity.draw()
                screen.blit(TextPrise, (770,160))
                screen.blit(TextPoids, (890,370))
                BVendre.update()
                screen.blit(TextVendre, (745,460))
                if prise == Anchois:
                    screen.blit(TextAnchoisCounter,(720,560))
                if blackmarket:
                    BVendreBlack.update()
                    screen.blit(TextOuBlack,(950,560))
                UMoney.draw()
                screen.blit(TextMoney,(30,95))
                URideau = élément_visuel(SRideau,(-90,yrideau),0.75)
                URideau.draw()
                pygame.display.flip()
            # Ici le rideau couvre totalement l'écran, on change l'écran affiché derrière pour mettre les infos de l'écran default
            while yrideau < 650:
                yrideau +=40
                Background.draw()
                screen.blit(SMusique,(20,25))
                screen.blit(TextMusique,(70,30))
                UCanne = élément_visuel(SpriteCanne[canne.quality], (800, 150), 1.1)
                UCanne.draw()
                UMoney.draw()
                screen.blit(TextMoney,(30,95))
                if canne.quality != 6:
                    BAmeliorer.update()
                    TextPrix = F32.render(((str(prix))+" $"), True, (0, 0, 0), None)
                    screen.blit(TextPrix,(1070,106))
                URideau = élément_visuel(SRideau,(-90,yrideau),0.75)
                URideau.draw()
                pygame.display.flip()
            etat="default"
        
        # Lorsque l'on améliore la canne à pêche, on transit comme poour la pêche mais vers l'écran "amélioré ""   
        if etat == "TransitAmelioration":
            money-=prix
            yrideau = 650
            while yrideau > -300:
                yrideau-=60
                Background.draw()
                screen.blit(SMusique,(20,25))
                screen.blit(TextMusique,(70,30))
                UCanne = élément_visuel(SpriteCanne[canne.quality], (800, 150), 1.1)
                UCanne.draw()
                UMoney.draw()
                screen.blit(TextMoney,(30,95))
                if canne.quality != 6:
                    BAmeliorer.update()
                    TextPrix = F32.render(((str(prix))+" $"), True, (0, 0, 0), None)
                    screen.blit(TextPrix,(1070,106))
                URideau = élément_visuel(SRideau,(-90,yrideau),0.75)
                URideau.draw()
                pygame.display.flip()
            while yrideau > -1070:
                yrideau-=60
                BAmelioration.draw()
                UCanne = élément_visuel(SpriteCanne[(canne.quality+1)], (400, 250), 0.9)
                UCanne.draw()
                URideau = élément_visuel(SRideau,(-90,yrideau),0.75)
                URideau.draw()
                pygame.display.flip()
            etat="Amélioré"
        
        # Ecran "amélioré" pour afficher la nouvelle canne à pêche, retour si le joueur clique au milieu de l'écran (réutilisation du bouton pêche)
        if etat == "Amélioré":
            BAmelioration.draw()
            UCanne = élément_visuel(SpriteCanne[(canne.quality+1)], (400, 250), 0.9)
            UCanne.draw()
            URideau = élément_visuel(SRideau,(-90,yrideau),0.75)
            URideau.draw()
            BPecher.update()
            if BPecher.clicked:
                BPecher.clicked=False
                etat = "TransitRetour2"
         
        #Transition de l'écran "amélioré" à default         
        if etat == "TransitRetour2":
            while yrideau < -300:
                yrideau+=60
                BAmelioration.draw()
                UCanne = élément_visuel(SpriteCanne[(canne.quality+1)], (400, 250), 0.9)
                UCanne.draw()
                URideau = élément_visuel(SRideau,(-90,yrideau),0.75)
                URideau.draw()
                BPecher.update()
                pygame.display.flip()
            canne.quality+=1
            if canne.quality != 6:
                Background = BBackground1
                BPeche = BPeche1
            else :
                Background = BBackground2
                BPeche = BPeche2
                Playlist.insert(PlaylistProgress+1,Doomsnight)
            if canne.quality < 2:
                    prix = 500
            elif canne.quality < 3:
                    prix = 2000
            elif canne.quality < 4:
                    prix = 5000
            elif canne.quality < 5:
                    prix = 15000
            elif canne.quality < 6 :
                    prix = 100000
            while yrideau <650:
                yrideau+=60
                Background.draw()
                screen.blit(SMusique,(20,25))
                screen.blit(TextMusique,(70,30))
                UCanne = élément_visuel(SpriteCanne[canne.quality], (800, 150), 1.1)
                UCanne.draw()
                UMoney.draw()
                screen.blit(TextMoney,(30,95))
                if canne.quality != 6:
                    BAmeliorer.update()
                    TextPrix = F32.render(((str(prix))+" $"), True, (0, 0, 0), None)
                    screen.blit(TextPrix,(1070,106))
                URideau = élément_visuel(SRideau,(-90,yrideau),0.75)
                URideau.draw()
                pygame.display.flip()
            URideau = élément_visuel(SRideau,(-90,650),0.75)
            clic_relache=False
            BPecher.update()
            
            etat="default"
                
                
        # Etat Cthulu pour terminer le jeu si le monstre est pêché    
        if etat=="Cthulhu":
            pygame.mixer.music.stop()
            ending()
            return
            
        pygame.display.flip()

# Lance un écran fixe de Chtulu avec une musique tristoune si on lance le programme alors que le fichier save.txt a été corrompu
if ERREUR:
    i = 0
    done = False
    while not done:
        clock.tick(60)
        i += 1
        if i > 200:
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)
        BlendSurface(SBCthulhu, i/200) 
        pygame.display.flip()
    LastSquid.play()
    running=True
    while running:
        # Les clics ne sont pas important ici mais cette partie permet simplement de vider la mémoire vive de pygame
        for event in pygame.event.get() :
            clic_relache = False
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clic = True
                clic_relache = False
            if event.type == pygame.MOUSEBUTTONUP and clic == True:
                clic = False
                clic_relache = True
            elif event.type == pygame.MOUSEBUTTONUP:
                clic = False
                clic_relache = False

#Si le fichier save.txt n'est pas corrompu le jeu se lance normalement
else:
    main()
    
# Merci de jouer à notre jeu, bonne chance pour vos prochaines prises !!!
