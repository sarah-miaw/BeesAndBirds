import pygame as pg; from pygame.locals import *;

class Get:
    def init():
        
        Get.listKeys ={
            'CommandKeys':[
            [K_RETURN,'RETURN','Secondary'],
            
            [K_TAB,'TAB','Main'],                 
            [K_SPACE,'SPACE','Main'],
            [K_UP,'UP','Main'],
            [K_DOWN,'DOWN','Main'],
            [K_RIGHT,'RIGHT','Main'],
            [K_LEFT,'LEFT','Main'],
            [K_ESCAPE,'ESCAPE','Main'],
            [K_KP_ENTER,'ENTER','Main'],
            [K_CAPSLOCK,'CAPSLOCK','Main'],
            [K_NUMLOCK,'NUMLOCK','Main'],
            [K_SCROLLLOCK,'SCROLLLOCK','Main'],
            [K_RALT,'RALT','Main'],
            [K_LALT,'LALT','Main'],
            [K_RSHIFT,'RSHIFT','Main'],
            [K_LSHIFT,'LSHIFT','Main'],
            [K_RCTRL,'RCTRL','Main'],
            [K_LCTRL,'LCTRL','Main'],
            [K_BACKSPACE,'BACKSPACE','Main'],
            [K_PAGEUP,'PAGEDOWN','Main'],
            [K_PAGEDOWN,'PAGEDOWN','Main'],
            [K_HOME,'HOME','Main'],
            [K_END,'END','Main'],
            [K_INSERT,'INSERT','Main'],
            [K_DELETE,'DELETE','Main'],
            [K_PAUSE,'PAUSE','Main'],
            [K_F1,'F1','Main'],
            [K_F2,'F2','Main'],
            [K_F3,'F3','Main'],
            [K_F4,'F4','Main'],
            [K_F5,'F5','Main'],
            [K_F6,'F6','Main'],
            [K_F7,'F7','Main'],
            [K_F8,'F8','Main'],
            [K_F9,'F9','Main'],
            [K_F10,'F10','Main'],
            [K_F11,'F11','Main'],
            [K_F12,'F12','Main'],      
            ],

            'TypeKeys':[
            [K_1,'1','Main'],
            [K_2,'2','Main'],
            [K_3,'3','Main'],
            [K_4,'4','Main'],
            [K_5,'5','Main'],
            [K_6,'6','Main'],
            [K_7,'7','Main'],
            [K_8,'8','Main'],
            [K_9,'9','Main'],
            [K_0,'0','Main'],

            [K_KP_1,'1','Secondary'],
            [K_KP_2,'2','Secondary'],
            [K_KP_3,'3','Secondary'],
            [K_KP_4,'4','Secondary'],
            [K_KP_5,'5','Secondary'],
            [K_KP_6,'6','Secondary'],
            [K_KP_7,'7','Secondary'],
            [K_KP_8,'8','Secondary'],
            [K_KP_9,'9','Secondary'],
            [K_KP_0,'0','Secondary'],

            [K_a,'a','main'],
            [K_b,'b','main'],
            [K_c,'c','main'],
            [K_d,'d','main'],
            [K_e,'e','main'],
            [K_f,'f','main'],
            [K_g,'g','main'],
            [K_h,'h','main'],
            [K_i,'i','main'],
            [K_j,'j','main'],            
            [K_k,'k','main'],
            [K_l,'l','main'],
            [K_m,'m','main'],
            [K_n,'n','main'],
            [K_o,'o','main'],
            [K_p,'p','main'],
            [K_q,'q','main'],
            [K_r,'r','main'],
            [K_s,'s','main'],
            [K_t,'t','main'],
            [K_u,'u','main'],
            [K_v,'v','main'],
            [K_w,'w','main'],
            [K_x,'x','main'],
            [K_y,'y','main'],
            [K_z,'z','main'],           
            
            [K_KP_DIVIDE,'/','Secondary'],
            [K_KP_MULTIPLY,'*','Secondary'],
            [K_KP_PLUS,'+','Secondary'],
            [K_KP_MINUS,'-','Secondary'],
            
            [K_COMMA,',','main'],
            [K_PERIOD,'.','main'],
            [K_KP_PERIOD,'.','Secondary'],
            [K_SLASH,'/','main'],      
            [K_BACKSLASH,'\\','main'],
            [K_PLUS,'+','main'],
            [K_MINUS,'-','main'],
            [K_EQUALS,'=','main'],
            [K_SEMICOLON,';','main'],  
            [K_RIGHTBRACKET,'[','main'],
            [K_LEFTBRACKET,']','main'], 
            [K_BACKQUOTE,'`','main'],
            [K_QUOTE,"'",'main'],


            ],

        }

    def keys(event):
        if event.type in [KEYDOWN,KEYUP]:
            for i in Get.listKeys:
                for c in Get.listKeys[i]:
                    
                    if event.key==c[0]:
                        return i,c[0],c[1],c[2];

    def mouse(event):
        0

    def iteration(EventList):
        List=[]

        for i in EventList:
            c=Get.keys(i)
            if c!=None:
                
                if i.type==KEYDOWN:
                    List.append(['KeyDown',c[0],c[1],c[2],c[3]])
                if i.type==KEYUP:
                    List.append(['KeyUp',c[0],c[1],c[2],c[3]])

        return List;

    