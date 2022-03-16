import pygame as pg;from pygame.locals import *;


class Screen:
    def init(Type,Scale):
        Screen.Type=Type
        Screen.Scale=Scale
        rsize=pg.display.get_desktop_sizes()[0]
        Screen.rsize=rsize
        if Type=='Fullscreen':
            X,Y=rsize
            canvas=pg.display.set_mode((X,Y),FULLSCREEN)

        elif Type=='Scaled':
            X=rsize[0]*Scale[0];X=int(X)
            Y=rsize[1]*Scale[1];Y=int(Y)
            
            canvas=pg.display.set_mode((X,Y))

        elif Type=='StaticFullscreen':
            surface = pg.surface.Surface([Scale[0],Scale[1]])
            
            canvas=pg.display.set_mode(rsize,FULLSCREEN)
            Screen.mood=Scale[2]
            Screen.canvas=canvas;
            Screen.surface=surface;
            return [canvas,surface]

        
        return [canvas,[X,Y]]



    def update(Surface):
        if Screen.Type=='StaticFullscreen':
            if Screen.mood=='Stretched':
                Surface2=pg.transform.scale(Surface,Screen.rsize)
                Screen.canvas.blit(Surface2,[0,0])

            pg.display.update()
            


if __name__=='__main__':
    def getEvents():
        global run

        for i in pg.event.get():
            if i.type==QUIT or i.type==KEYDOWN and i.key==K_ESCAPE:
                run=0

    run=1
    pg.init()
    scr,[X,Y]=Screen.init('Fullscreen',[0.8,0.6])
    print(scr,X,Y)

    while run:
        getEvents()
        
