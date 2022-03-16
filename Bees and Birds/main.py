import pygame as pg; from pygame.locals import *
import sys;
from myColors import Colors as cls;from myEvents import Get
from myScreen import Screen
import random;


def newScaleByWidth(Surface,newWidth):
    A=newWidth/Surface.get_width()
    newHeight=Surface.get_height()*A
    newSurface=pg.transform.scale(Surface,[newWidth,newHeight])

    return newSurface

def newScaleByHeight(Surface,newHeight):
    A=newHeight/Surface.get_height()
    newWidth=Surface.get_width()*A
    newSurface=pg.transform.scale(Surface,[newWidth,newHeight])

    return newSurface


def Drawer():
    if Menu.page!=3:
        scr.fill(colorSet[Menu.ColorTheme]['bg'])
        Menu.draw()
    else:
        scr.fill(clss['Purple']['Lavender'])
        Game.draw()
        

def CheckEvents():
    if Menu.page!=3:
        Menu.check()
    else:
        Game.check()
    
def getHeld():
    global heldKeys
    for i in cks:
        if i[0]=='KeyDown' and i not in heldKeys:
            heldKeys.append(i)
        elif i[0]=='KeyUp':
            for c in heldKeys:
                if i[3]==c[3]:
                    heldKeys.remove(c)
    
    


class Menu:
    def getPage1():
        slc0,slc1,slc2='','',''
        color0=color1=color2=colorSet[Menu.ColorTheme]['font0']
        if Menu.selec==0:
            slc0+="#"
            color0=colorSet[Menu.ColorTheme]['font1']
        elif Menu.selec==1:
            slc1+="#"
            color1=colorSet[Menu.ColorTheme]['font1']
        elif Menu.selec==2:
            slc2+="#"
            color2=colorSet[Menu.ColorTheme]['font1']
        
        mfpa0=font1.render(slc0+Menu.sts[0],1,color0)
        mfpa1=font1.render(slc1+Menu.sts[1],1,color1)
        mfpa2=font1.render(slc2+Menu.sts[2],1,color2)
        
        paX=max([mfpa0.get_width(),mfpa1.get_width(),mfpa2.get_width()])
        paY=sum([mfpa0.get_height(),mfpa1.get_height(),mfpa2.get_height()])       
        
        Menu.pagea=pg.surface.Surface((paX,paY))
        Menu.pagea.set_colorkey([0,0,0])
        Menu.pagea.blit(mfpa0,[0,0])
        Menu.pagea.blit(mfpa1,[0,mfpa0.get_height()])
        Menu.pagea.blit(mfpa2,[0,mfpa0.get_height()+mfpa1.get_height()])

    def getPage2():
        slc1,slc2='',''
        color0=color1=color2=colorSet[Menu.ColorTheme]['font0']

        if Menu.selec==1:
            slc1+="#"
            color1=colorSet[Menu.ColorTheme]['font1']
        elif Menu.selec==2:
            slc2+="#"
            color2=colorSet[Menu.ColorTheme]['font1']

        mfpb0=font1.render(Menu.sts[3],1,color0)
        mfpb1=font1.render(slc1+Menu.sts[4],1,color1)
        mfpb2=font1.render(slc2+Menu.sts[5],1,color2)

        pbX=mfpb0.get_width()
        pbY=mfpb0.get_height()+mfpb1.get_height()

        Menu.pageb=pg.surface.Surface((pbX,pbY))
        Menu.pageb.set_colorkey((0,0,0))

        Menu.pageb.blit(mfpb0,[0,0])
        Menu.pageb.blit(mfpb1,[0,mfpb0.get_height()])
        Menu.pageb.blit(mfpb2,[mfpb0.get_width()-mfpb2.get_width(),
                            mfpb0.get_height()])


    def getPage3():
        slc0,slc1,slc2,slc3,slc4,slc5='','','','','',''

        color0=color1=color2=color3=color4=color5=colorSet[Menu.ColorTheme]['font0']

        colorch=colorSet[Menu.ColorTheme]['font1']
        if Menu.selec==0:
            color0=colorch
            slc0='#'
        elif Menu.selec==1:
            color1=colorch
            slc1='#'
        elif Menu.selec==2:
            color2=colorch
            slc2='#'
        elif Menu.selec==3:
            color3=colorch
            slc3='#'
        elif Menu.selec==4:
            color4=colorch
            slc4='#'
        elif Menu.selec==5:
            color5=colorch
            slc5='#'


        mfpc0=font1.render(slc0+Menu.sts[6],1,color0)#Time
        mfpc1=font1.render(Menu.sts[7],1,color0)#Day
        mfpc2=font1.render(Menu.sts[8],1,color0)#Night

        mfpc3=font1.render(slc1+Menu.sts[9],1,color1)#FPS
        mfpc14=font1.render(f'{fps}',1,color1)

        mfpc4=font1.render(slc2+Menu.sts[10],1,color2)#Sounds
        mfpc7=font1.render(Menu.sts[12],1,color2)#Off  
        mfpc8=font1.render(Menu.sts[13],1,color2)#On

        mfpc5=font1.render(slc3+Menu.sts[11],1,color3)#Music
        mfpc12=font1.render(Menu.sts[12],1,color3)#Off  
        mfpc13=font1.render(Menu.sts[13],1,color3)#On 
        
        mfpc9=font1.render(slc4+Menu.sts[14],1,color4)#Color Theme
        mfpc10=font1.render(Menu.sts[15],1,color4)#Dark
        mfpc11=font1.render("  "+Menu.sts[16],1,color4)#Light

        mfpc15=font1.render(slc5+Menu.sts[17],1,color5)

        
        Menu.pagec=pg.surface.Surface((
            mfpc9.get_width() + mfpc11.get_width(),
            mfpc0.get_height()*6+25
        ))
        
        #Menu.pagec=pg.surface.Surface((500,500))
        #print(Menu.pagec)
        
        Menu.pagec.set_colorkey((0,0,0))

        if Menu.Sounds=='On':
            sounds = mfpc7
        else:           
            sounds = mfpc8

        if Menu.Music=='On':
            music=mfpc12
        else:
            music=mfpc13

        if Menu.ColorTheme=='Light':
            colortheme=mfpc11
        else:
            colortheme=mfpc10
        
        if Menu.Time=='Day':
            Time=mfpc1
        else:
            Time=mfpc2

        fX=Menu.pagec.get_width()
        Menu.pagec.blit(mfpc0,[0,0])
        Menu.pagec.blit(Time,[fX-Time.get_width(),0])

        Menu.pagec.blit(mfpc3,[0,mfpc0.get_height()])
        Menu.pagec.blit(mfpc14,[fX-mfpc14.get_width()
        ,mfpc0.get_height()])

        Menu.pagec.blit(mfpc4,[0,mfpc0.get_height()*2])
        Menu.pagec.blit(sounds,[fX-sounds.get_width()
        ,mfpc0.get_height()*2])

        Menu.pagec.blit(mfpc5,[0,mfpc0.get_height()*3])
        Menu.pagec.blit(music,[fX-music.get_width()
        ,mfpc0.get_height()*3])

        Menu.pagec.blit(mfpc9,[0,mfpc0.get_height()*4])
        Menu.pagec.blit(colortheme,[fX-colortheme.get_width(),mfpc0.get_height()*4])

        Menu.pagec.blit(mfpc15,[fX/2-mfpc15.get_width()/2,mfpc0.get_height()*5+25])

        
    def init():
        Menu.ColorTheme='Dark'
        Menu.Time='Day'
        Menu.Sounds='On'
        Menu.Music='On'

        Menu.page=0;Menu.selec=0
        Menu.sts=['Play Game','Settings','Quit',
             'Are You Sure?',
             'Yes','No',
             'Time','Day','Night',
             'FPS',
             'Sounds','Music','Off','On',
             'Color Theme','Dark','Light'
             ,'Back']

        Menu.getPage1()
        #Menu.getPage2()

        


    def draw():
        if Menu.page==0:

            paDem=[X/2-Menu.pagea.get_width()/1.5
            ,Y/2-Menu.pagea.get_height()/2]
            scr.blit(Menu.pagea,paDem)
        elif Menu.page==1:
            paDem=[X/2-Menu.pageb.get_width()/1.5
            ,Y/2-Menu.pageb.get_height()/2]

            scr.blit(Menu.pageb,paDem)

        elif Menu.page==2:
            paDem=[X/2-Menu.pagec.get_width()/2
            ,Y/2-Menu.pagec.get_height()/2]

           
            scr.blit(Menu.pagec,paDem)


    
    def check():
        global fps
        for i in cks:
            if Menu.page==0 and i[0]=='KeyDown':
                if i[3]=='UP' and Menu.selec!=0:
                    Menu.selec-=1
                    Menu.getPage1()
                elif i[3]=='DOWN' and Menu.selec!=2:
                    Menu.selec+=1
                    Menu.getPage1()
                elif i[3] in ['RETURN','ENTER'] and Menu.selec==2:
                    Menu.selec=1;Menu.page=1
                    Menu.getPage2()
                elif i[3] in ['RETURN','ENTER'] and Menu.selec==1:
                    Menu.selec=0;Menu.page=2
                    Menu.getPage3()
                elif i[3] in ['RETURN','ENTER'] and Menu.selec==0:
                    Menu.selec=None;Menu.page=3
                    

            elif Menu.page==1 and i[0]=='KeyDown':
                
                if i[3]=='RIGHT' and Menu.selec==1:
                    Menu.selec=2
                    Menu.getPage2()
                elif i[3]=='LEFT' and Menu.selec==2:
                    Menu.selec=1
                    Menu.getPage2()
                elif i[3] in ['RETURN' , 'ENTER']:
                    if Menu.selec==1:
                        pg.quit()
                        sys.exit()
                    elif Menu.selec==2:
                        Menu.page=0;Menu.selec=0;
                        Menu.getPage1()    

            elif Menu.page==2 and i[0]=='KeyDown':
                if i[3]=='UP' and Menu.selec!=0:
                    Menu.selec-=1
                    Menu.getPage3()
                elif i[3]=='DOWN' and Menu.selec!=5:
                    Menu.selec+=1
                    Menu.getPage3()
                elif i[3] in ['ENTER','RETURN'] and Menu.selec==5:
                    Menu.selec=0;Menu.page=0
                    Menu.getPage1()
                elif i[3] in ['LEFT','RIGHT']:
                    
                    if Menu.selec==0:
                        if Menu.Time=='Day':
                            Menu.Time='Night'
                        else:
                            Menu.Time='Day'    
                    elif Menu.selec==1:
                        if i[3]=='RIGHT' and fps!=75:
                            fps+=5
                        elif i[3]=='LEFT' and fps!=15:
                            fps-=5

                                  
                    elif Menu.selec==2:
                        if Menu.Sounds=='On':
                            Menu.Sounds='Off'
                        else:
                            Menu.Sounds='On'             
                    elif Menu.selec==3:
                        if Menu.Music=='On':
                            Menu.Music='Off'
                        else:
                            Menu.Music='On'        
                    elif Menu.selec==4:
                        if Menu.ColorTheme=='Light':
                            Menu.ColorTheme='Dark'
                        else:
                            Menu.ColorTheme='Light'

                    Menu.getPage3()


class Game:
    def init():
        Images.init()
        Bee.init()
        ViewPort.init()
        Objects.init()


    def draw():
        Objects.draw()
        Bee.draw()
        

    def check():
        Objects.check()
        Bee.check()


class Bee:
    def init():
        Bee.size = [Images.Dict['Bee'][0].get_width(),
        Images.Dict['Bee'][0].get_height()]

        Bee.pos = [X/2-Bee.size[0]/2,Y/2-Bee.size[1]/2]
        Bee.Rect = [Bee.pos[0],Bee.pos[1],Bee.size[0],Bee.size[1]]

       
        
        Bee.Index = 0
        Bee.Mood = 0
        Bee.Speed = sum(Bee.size)/15
        Bee.flipx = 0
        
        Bee.getBeeRects() 

    def getBeeRects():
        Bee.Rect=[Bee.pos[0],Bee.pos[1],Bee.size[0],Bee.size[1]]

        br = Bee.Rect


        Bee.rRect = [br[0]+br[2],br[1],Bee.Speed,br[3]]

        Bee.lRect = [br[0]-Bee.Speed,br[1],Bee.Speed,br[3]]

        Bee.uRect = [br[0],br[1]-Bee.Speed,br[2],Bee.Speed]

        Bee.dRect = [br[0],br[1]+br[3],br[2],Bee.Speed]


    def draw():
        surface=Images.Dict['Bee'][Bee.Index+Bee.Mood]
        if Bee.flipx:
            surface = pg.transform.flip(surface,1,0)
        scr.blit(surface,Bee.pos)
        
    def ifCol(Rect,RectList):
        xRect = pg.Rect(Rect)
        for i in RectList:

            if xRect.colliderect(i):
                print(i)
                return 1
        return 0;

    def check():
        Bee.getBeeRects()
        for i in heldKeys:
            if i[3]=='UP':
                if not Bee.ifCol(Bee.uRect,Objects.rects):
                    Bee.pos[1]-=Bee.Speed


            if i[3]=='DOWN':
                if not Bee.ifCol(Bee.dRect,Objects.rects):
                    Bee.pos[1]+=Bee.Speed

            if i[3]=='RIGHT':
                if not Bee.ifCol(Bee.rRect,Objects.rects):
                    Bee.pos[0]+=Bee.Speed  

                Bee.flipx=0       

            if i[3]=='LEFT':
                if not Bee.ifCol(Bee.lRect,Objects.rects):
                    Bee.pos[0]-=Bee.Speed

                Bee.flipx=1

         
class ViewPort:
    def init():
        0

    def draw():
        0

    def check():
        0

class Images:
    def init():
        dirt0='images/dirt0.png'
        dirt1='images/dirt1.png'
        dirt2='images/dirt2.png'
        dirt3='images/dirt3.png'
        dirt4='images/dirt4.png'
        dirt5='images/dirt5.png'

        stone0='images/stone0.png'
        stone1='images/stone1.png'
        stone2='images/stone2.png'
        stone3='images/stone3.png'
        stone4='images/stone4.png'
        stone5='images/stone5.png'

        water0='images/water0.png'
        water1='images/water1.png'
        water2='images/water2.png'
        water3='images/water3.png'
        water4='images/water4.png'
        water5='images/water5.png'

        fire0='images/fire0.png'
        fire1='images/fire1.png'
        fire2='images/fire2.png'
        fire3='images/fire3.png'
        fire4='images/fire4.png'
        fire5='images/fire5.png'

        bee0='images/bee0.png'
        bee1='images/bee1.png'
        bee2='images/bee2.png'
        bee3='images/bee3.png'

        cloud0='images/cloud0.png'
        cloud1='images/cloud1.png'

        flower0='images/flower0.png'
        flower1='images/flower1.png'

        Images.Dict={
            'Dirt':[dirt0,dirt1,dirt2,dirt3],
            'Stone':[stone0,stone1,stone2,stone3],
            'Water':[water0,water1,water2,water3,water4,water5],
            'Fire':[fire0,fire1,fire2,fire3,fire4,fire5],
            'Bee':[bee0,bee1,bee2,bee3],
            'Cloud':[cloud0,cloud1],
            'Flower':[flower0,flower1]
        }

        for i in Images.Dict:
            C=-1
            for c in Images.Dict[i]:
                C+=1
                if i in ['Stone','Dirt','Water']:
                    iterWidth=50
                elif i == 'Bee':
                    iterWidth=25

                elif i == 'Cloud':
                    iterWidth=None
                    
                elif i == 'Flower':
                    iterWidth=30


                
                surface=pg.image.load(c)
                if iterWidth==None:
                    iterWidth=surface.get_width()
                newSurface=newScaleByWidth(surface,iterWidth)

                Images.Dict[i][C]=newSurface
                


    
class Objects:
    
    def init():
        flowHeight=Images.Dict['Flower'][0].get_height()
        Objects.Dict={
            'Dirt':[
                [0,550],[50,550],[100,550],
                [150,550],[200,550],
                
                [450,550],[500,550],[550,550],
                [600,550],[650,550],[700,550],
                [750,550]

            ],
            'Water':[
                [300,550],[350,550],[400,550],[250,550]
            ],
            'Flower':[
                [150,550-flowHeight],
                [450,550-flowHeight],
                [100,550-flowHeight],
                [700,550-flowHeight],           
            ],

            'Stone':[
                [0,0],[50,0],[100,0],
                [150,0],[200,0],[250,0],
                [300,0],[350,0],[400,0],
                [450,0],[500,0],[550,0],
                [600,0],[650,0],[700,0],
                [750,0]
                ,
                [750,50],[750,100],[750,150],[750,200],[750,250],
                [750,300],[750,350],[750,400],[750,450],[750,500],

                [0,50],[0,100],[0,150],[0,200],[0,250],
                [0,300],[0,350],[0,400],[0,450],[0,500],

            ]
        }

        Objects.rects = []

        for i in Objects.Dict:
            for c in Objects.Dict[i]:
                if i!='Flower':
                    Objects.rects.append([c[0],c[1],50,50])
                else:
                    Objects.rects.append([c[0],c[1],30,flowHeight])

        #print(Objects.rects)


        for i in Objects.Dict:
            C=-1;
            for c in Objects.Dict[i]:
                pos=c
                surface=random.choice(Images.Dict[i])
                C+=1
                Objects.Dict[i][C]=[pos,surface]

    def draw():
        for i in Objects.Dict:
            for c in Objects.Dict[i]:
                scr.blit(c[1],c[0])
                
    def check():
        0







heldKeys=[]

pg.init();cls.init();Get.init()
mScreen,mSurface=Screen.init('StaticFullscreen',[800,600,'Stretched'])
clock=pg.time.Clock();fps=30
clss=cls.Dict

font0=pg.font.SysFont('david',80,1)
font1=pg.font.SysFont('comic sans ms',100,0)


rx,ry=mScreen.get_width(),mScreen.get_height()
X,Y=mSurface.get_width(),mSurface.get_height()

scr=mSurface

run=1;


colorSet={
    
            "Light":{"bg":clss['Blue']['DeepSkyBlue'],
                    "font0":clss['Purple']['Indigo'],
                    "font1":clss['Brown']['Sienna']},
            
             "Dark":{"bg":clss['Blue']['MidnightBlue'],
                    "font0":clss['Gray']['DarkSlateGray'],
                    "font1":clss['Brown']['Maroon']}
                 
                 }


Menu.init();Game.init()
pg.mouse.set_visible(0)
while run:
    cks=Get.iteration(pg.event.get()) 
    getHeld()  
    for i in cks:       
        if i[3]=='ESCAPE' and i[0]=='KeyDown':
            if Menu.page!=3:
                Menu.page=1;Menu.selec=1
                Menu.getPage2()
            else:
                Menu.page=0;Menu.selec=0
                Menu.getPage1()



    CheckEvents()
    Drawer()
    Screen.update(scr)
    clock.tick(fps)

    

