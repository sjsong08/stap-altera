import pygame, sys, random, pickle


class CarRClass(pygame.sprite.Sprite):
    def __init__(self):
        global angler
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("carr.gif")
        self.rect=self.image.get_rect()
        self.rect.center=[55,672]
        self.rotate=pygame.transform.rotate(self.image,angler)
        self.mask=pygame.mask.from_surface(self.rotate)

    def angle(self,angler):
        self.rotate=pygame.transform.rotate(self.image,angler)

    def movel(self):
        global carrspeed,angler
        if carr.rect.centerx!=55 and carrspeed==-5:
            carr.rect.centerx+=carrspeed
            if carr.rect.centerx==165 :
                angler=0
            if carr.rect.centerx==160 :
                angler=5
            if carr.rect.centerx==155 :
                angler=10   
            if carr.rect.centerx==150 :
                angler=15   
            if carr.rect.centerx==145 :
                angler=20    
            if carr.rect.centerx==140 :
                angler=25    

            if carr.rect.centerx==135 :
                angler=30    
            if carr.rect.centerx==130 :
                angler=35    
            if carr.rect.centerx==125 :
                angler=40    
            if carr.rect.centerx==120 :
                angler=45    
            if carr.rect.centerx==115 :
                angler=50  
            if carr.rect.centerx==110 :
                angler=55
            if carr.rect.centerx==105 :
                angler=50
            if carr.rect.centerx==100 :
                angler=45   
            if carr.rect.centerx==95 :
                angler=40   
            if carr.rect.centerx==90 :
                angler=35    
            if carr.rect.centerx==85 :
                angler=30    

            if carr.rect.centerx==80 :
                angler=25    
            if carr.rect.centerx==75 :
                angler=20    
            if carr.rect.centerx==70 :
                angler=15    
            if carr.rect.centerx==65 :
                angler=10    
            if carr.rect.centerx==60 :
                angler=5
            if carr.rect.centerx==55 :
                angler=0                   
    def mover(self):
        global carrspeed,angler
        if carr.rect.centerx!=165 and carrspeed==+5:

            carr.rect.centerx+=carrspeed
            if carr.rect.centerx==165 :
                angler=0
            if carr.rect.centerx==160 :
                angler=-5
            if carr.rect.centerx==155 :
                angler=-10   
            if carr.rect.centerx==150 :
                angler=-15   
            if carr.rect.centerx==145 :
                angler=-20    
            if carr.rect.centerx==140 :
                angler=-25    

            if carr.rect.centerx==135 :
                angler=-30    
            if carr.rect.centerx==130 :
                angler=-35    
            if carr.rect.centerx==125 :
                angler=-40    
            if carr.rect.centerx==120 :
                angler=-45    
            if carr.rect.centerx==115 :
                angler=-50  
            if carr.rect.centerx==110 :
                angler=-55
            if carr.rect.centerx==105 :
                angler=-50
            if carr.rect.centerx==100 :
                angler=-45   
            if carr.rect.centerx==95 :
                angler=-40   
            if carr.rect.centerx==90 :
                angler=-35    
            if carr.rect.centerx==85 :
                angler=-30    

            if carr.rect.centerx==80 :
                angler=-25    
            if carr.rect.centerx==75 :
                angler=-20    
            if carr.rect.centerx==70 :
                angler=-15    
            if carr.rect.centerx==65 :
                angler=-10    
            if carr.rect.centerx==60 :
                angler=-5
            if carr.rect.centerx==55 :
                angler=0

class CarBClass(pygame.sprite.Sprite):
    def __init__(self):
        global angleb
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("carb.gif")
        self.rect=self.image.get_rect()
        self.rect.center=[385,672]
        self.mask=pygame.mask.from_surface(self.image)
        self.rotate=pygame.transform.rotate(self.image,angleb)
        self.mask=pygame.mask.from_surface(self.rotate)

    def angle(self,angleb):
        self.rotate=pygame.transform.rotate(self.image,angleb)

    def movel(self):
        global carbspeed, angleb
        if carb.rect.centerx!=275 and carbspeed==-5:
            
            carb.rect.centerx+=carbspeed
            if carb.rect.centerx==385 :
                angleb=0
            if carr.rect.centerx==380 :
                angleb=5
            if carb.rect.centerx==375 :
                angleb=10   
            if carb.rect.centerx==370 :
                angleb=15   
            if carb.rect.centerx==365 :
                angleb=20    
            if carb.rect.centerx==360 :
                angleb=25    

            if carb.rect.centerx==355 :
                angleb=30    
            if carb.rect.centerx==350 :
                angleb=35    
            if carb.rect.centerx==345 :
                angleb=40    
            if carb.rect.centerx==340 :
                angleb=45    
            if carb.rect.centerx==335 :
                angleb=50  
            if carb.rect.centerx==330 :
                angleb=55
            if carb.rect.centerx==325 :
                angleb=50
            if carb.rect.centerx==320 :
                angleb=45   
            if carb.rect.centerx==315 :
                angleb=40   
            if carb.rect.centerx==310 :
                angleb=35    
            if carb.rect.centerx==305 :
                angleb=30    

            if carb.rect.centerx==300 :
                angleb=25    
            if carb.rect.centerx==295 :
                angleb=20    
            if carb.rect.centerx==290 :
                angleb=15    
            if carb.rect.centerx==285 :
                angleb=10    
            if carb.rect.centerx==280 :
                angleb=5
            if carb.rect.centerx==275 :
                angleb=0  
    def mover(self):
        global carbspeed,angleb
        if carb.rect.centerx!=385 and carbspeed==+5:

            carb.rect.centerx+=carbspeed
            if carb.rect.centerx==385 :
                angleb=0
            if carr.rect.centerx==380 :
                angleb=-5
            if carb.rect.centerx==375 :
                angleb=-10   
            if carb.rect.centerx==370 :
                angleb=-15   
            if carb.rect.centerx==365 :
                angleb=-20    
            if carb.rect.centerx==360 :
                angleb=-25    

            if carb.rect.centerx==355 :
                angleb=-30    
            if carb.rect.centerx==350 :
                angleb=-35    
            if carb.rect.centerx==345 :
                angleb=-40    
            if carb.rect.centerx==340 :
                angleb=-45    
            if carb.rect.centerx==335 :
                angleb=-50  
            if carb.rect.centerx==330 :
                angleb=-55
            if carb.rect.centerx==325 :
                angleb=-50
            if carb.rect.centerx==320 :
                angleb=-45   
            if carb.rect.centerx==315 :
                angleb=-40   
            if carb.rect.centerx==310 :
                angleb=-35    
            if carb.rect.centerx==305 :
                angleb=-30    

            if carb.rect.centerx==300 :
                angleb=-25    
            if carb.rect.centerx==295 :
                angleb=-20    
            if carb.rect.centerx==290 :
                angleb=-15    
            if carb.rect.centerx==285 :
                angleb=-10    
            if carb.rect.centerx==280 :
                angleb=-5
            if carb.rect.centerx==275 :
                angleb=0            
class ObstacleRClass(pygame.sprite.Sprite):
    def __init__(self, image_file,location,type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file=image_file
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
        self.type=type
        self.mask=pygame.mask.from_surface(self.image)

    def update(self,speed):
        
        self.rect.bottom +=speed
        if self.rect.bottom>800:
            self.kill()

    def tupdate(self):
        global speed
        self.rect.bottom +=speed
        if self.rect.bottom>800:
            self.kill()


class ObstacleBClass(pygame.sprite.Sprite):
    def __init__(self, image_file,location,type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file=image_file
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
        self.type=type
        self.mask=pygame.mask.from_surface(self.image)
    def update(self,speed):
        
        self.rect.bottom +=speed
        if self.rect.bottom>800:
            self.kill()
    def tupdate(self):
        global speed
        self.rect.bottom +=speed
        if self.rect.bottom>800:
            self.kill()

            
class bottombar(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface=pygame.surface.Surface([1000,10])
        image_surface.fill([0,0,0])
        self.image=image_surface.convert()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location


class straightbar(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface=pygame.surface.Surface([5,1000])
        image_surface.fill([129,152,241])
        self.image=image_surface.convert()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
        
class straightbars(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface=pygame.surface.Surface([2,1000])
        image_surface.fill([129,152,241])
        self.image=image_surface.convert()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
        
def create_map():
    global obstaclesr
    global obstaclesb
    global obstacler
    global obstacleb
    global groupobsr
    global groupobsb
    global colr
    global colb
    locationsr=[]
    locationsb=[]
    for a in range(1):
        rowr=random.choice([33,143])
        
        locationr=[rowr,colr]
        if not (locationr in locationsr):
            locationsr.append(locationr)
            type=random.choice(["circler","blockr"])
            if type=="circler": imgr="circler.gif"
            elif type=="blockr": imgr="blockr.gif"
            obstacler=ObstacleRClass(imgr,locationr,type)
            obstaclesr.add(obstacler)
            groupobsr.append(obstacler)
    for b in range(1):
        rowb=random.choice([253,363])
        
        locationb=[rowb,colb]
        if not (locationb in locationsb):
            locationsb.append(locationb)
            type=random.choice(["circleb","blockb"])
            if type=="circleb": imgb="circleb.gif"
            elif type=="blockb": imgb="blockb.gif"
            obstacleb=ObstacleBClass(imgb,locationb,type)
            obstaclesb.add(obstacleb)
            groupobsb.append(obstacleb)
            
def animate():
    global point, point_font,point_surf
    screen.fill([30,51,160])
    obstaclesr.draw(screen)
    obstaclesb.draw(screen)
    
    
    screen.blit(point_surf,point_pos)
    screen.blit(bbar.image,bbar.rect)
    screen.blit(sbarm.image,sbarm.rect)
    screen.blit(sbarl.image,sbarl.rect)
    screen.blit(sbarr.image,sbarr.rect)
    
    screen.blit(carr.rotate,carr.rect)
    screen.blit(carb.rotate,carb.rect)
    pygame.display.flip()

def collision():
    global bbar,obstaclesr,obstaclesb,carr,carb,point,speed,done,point_pos,point_surf,max_score
    hitbarr=pygame.sprite.spritecollide(bbar,obstaclesr,False)    
    if hitbarr:
        if hitbarr[0].type=="circler" :
            
            max_score=open('score.txt','r')
            max_score_open=max_score.readlines()
            max_score.close()
            if int(max_score_open[0])<point:
                max_score=open('score.txt','w')
                max_score.write(str(point))
                max_score.close()
            
            max_score=open('score.txt','r')
            max_score_open=max_score.readlines()
            
            final_text1='Game Over'
            final_text2="Score : "+str(point)
            final_text3="Max score : "+max_score_open[0]
            ft1_font=pygame.font.Font(None,70)
            ft1_surf=ft1_font.render(final_text1,1,(255,255,255))
            ft2_font=pygame.font.Font(None,50)
            ft2_surf=ft2_font.render(final_text2,1,(255,255,255))
            ft3_font=pygame.font.Font(None,50)
            ft3_surf=ft3_font.render(final_text3,1,(255,255,255))
            screen.blit(ft1_surf,[screen.get_width()/2-\
                                  ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf,[screen.get_width()/2-\
                                  ft2_surf.get_width()/2,200])
            screen.blit(ft3_surf,[screen.get_width()/2-\
                                  ft3_surf.get_width()/2,300])
            max_score.close()
            pygame.display.flip()
            done=True

        elif hitbarr[0].type=="blockr" :
            hitbarr[0].kill()
            del groupobsr[0]
            speed+=0.02
  
    hitbarb=pygame.sprite.spritecollide(bbar,obstaclesb,False)    
    if hitbarb:
        if hitbarb[0].type=="circleb" :
            
            max_score=open('score.txt','r')
            max_score_open=max_score.readlines()
            max_score.close()
            if int(max_score_open[0])<point:
                max_score=open('score.txt','w')
                max_score.write(str(point))
                max_score.close()
            
            max_score=open('score.txt','r')
            max_score_open=max_score.readlines()
            
            final_text1='Game Over'
            final_text2="Score : "+str(point)
            final_text3="Max score : "+max_score_open[0]
            ft1_font=pygame.font.Font(None,70)
            ft1_surf=ft1_font.render(final_text1,1,(255,255,255))
            ft2_font=pygame.font.Font(None,50)
            ft2_surf=ft2_font.render(final_text2,1,(255,255,255))
            ft3_font=pygame.font.Font(None,50)
            ft3_surf=ft3_font.render(final_text3,1,(255,255,255))
            screen.blit(ft1_surf,[screen.get_width()/2-\
                                  ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf,[screen.get_width()/2-\
                                  ft2_surf.get_width()/2,200])
            screen.blit(ft3_surf,[screen.get_width()/2-\
                                  ft3_surf.get_width()/2,300])
            max_score.close()
            pygame.display.flip()
            done=True

        elif hitbarb[0].type=="blockb" :
            hitbarb[0].kill()
            del groupobsb[0]
            speed+=0.02
        
    hitr=pygame.sprite.spritecollide(carr,obstaclesr,False,pygame.sprite.collide_mask)    
    if hitr:
        if hitr[0].type=="blockr" :
            
            max_score=open('score.txt','r')
            max_score_open=max_score.readlines()
            max_score.close()
            if int(max_score_open[0])<point:
                max_score=open('score.txt','w')
                max_score.write(str(point))
                max_score.close()
            
            max_score=open('score.txt','r')
            max_score_open=max_score.readlines()
            
            final_text1='Game Over'
            final_text2="Score : "+str(point)
            final_text3="Max score : "+max_score_open[0]
            ft1_font=pygame.font.Font(None,70)
            ft1_surf=ft1_font.render(final_text1,1,(255,255,255))
            ft2_font=pygame.font.Font(None,50)
            ft2_surf=ft2_font.render(final_text2,1,(255,255,255))
            ft3_font=pygame.font.Font(None,50)
            ft3_surf=ft3_font.render(final_text3,1,(255,255,255))
            screen.blit(ft1_surf,[screen.get_width()/2-\
                                  ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf,[screen.get_width()/2-\
                                  ft2_surf.get_width()/2,200])
            screen.blit(ft3_surf,[screen.get_width()/2-\
                                  ft3_surf.get_width()/2,300])
            max_score.close()
            pygame.display.flip()
            done=True
          
            
        elif hitr[0].type=="circler" :
            point+=1
            speed+=0.02
            point_surf=point_font.render(str(point),1,(255,255,255))
            hitr[0].kill()
            del groupobsr[0]
            speed+=0.02
    
    hitb=pygame.sprite.spritecollide(carb,obstaclesb,False,pygame.sprite.collide_mask)    
    if hitb:
        if hitb[0].type=="blockb" :
            max_score=open('score.txt','r')
            max_score_open=max_score.readlines()
            max_score.close()
            if max_score_open[0]<point:
                max_score=open('score.txt','w')
                max_score.write(str(point))
                max_score.close()
            
            max_score=open('score.txt','r')
            max_score_open=max_score.readlines()
            
            final_text1='Game Over'
            final_text2="Score : "+str(point)
            final_text3="Max score : "+str(max_score_open[0])
            ft1_font=pygame.font.Font(None,70)
            ft1_surf=ft1_font.render(final_text1,1,(255,255,255))
            ft2_font=pygame.font.Font(None,50)
            ft2_surf=ft2_font.render(final_text2,1,(255,255,255))
            ft3_font=pygame.font.Font(None,50)
            ft3_surf=ft3_font.render(final_text3,1,(255,255,255))
            screen.blit(ft1_surf,[screen.get_width()/2-\
                                  ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf,[screen.get_width()/2-\
                                  ft2_surf.get_width()/2,200])
            screen.blit(ft3_surf,[screen.get_width()/2-\
                                  ft3_surf.get_width()/2,300])
            max_score.close()
            pygame.display.flip()
            done=True
            
            
            
        elif hitb[0].type=="circleb":
            point+=1
            speed+=0.02
            point_surf=point_font.render(str(point),1,(255,255,255))
            hitb[0].kill()
            del groupobsb[0]



pygame.init()
screen=pygame.display.set_mode([440,783])
clock=pygame.time.Clock()
angler=0
angleb=0
carr=CarRClass()
carb=CarBClass()
carrspeed=0
carbspeed=0

obstaclesr=pygame.sprite.Group()
obstaclesb=pygame.sprite.Group()
bbar=bottombar([0,783])
sbarm=straightbar([220,0])
sbarl=straightbars([110,0])
sbarr=straightbars([330,0])
map_position=0
groupobsr=[]
groupobsb=[]

colr=-130
colb=random.choice([-90,-50,-170,-210])
create_map()
running=True
point=0
speed=5

point_font=pygame.font.Font(None,70)
point_surf=point_font.render(str(point),1,(255,255,255))
point_pos=[355,15]
done=False

while running:
    clock.tick(60)
    

    if not done:

     #   print groupobsr[0].rect.center
     #   print groupobsb[0].rect.center

        
        if pygame.key.get_pressed()[ pygame.K_COMMA ] :
            if not carr.rect.centerx==55:
                carrspeed=-5
                anglerspeed=11
            elif carr.rect.centerx==55:
                carrspeed=0
                anglerspeed=0


        if pygame.key.get_pressed()[ pygame.K_PERIOD ] :
            
            if not carr.rect.centerx==165:
                
                carrspeed=+5
                anglerspeed=-11
            elif carr.rect.centerx==165:
                carrspeed=0
                anglerspeed=0


        if pygame.key.get_pressed()[ pygame.K_LEFT ] :
            
            if not carb.rect.centerx==275:
                carbspeed=-5
                anglebspeed=+11
            elif carb.rect.centerx==275:
                carbspeed=0
                anglebspeed=0


        if pygame.key.get_pressed()[ pygame.K_RIGHT ] :
            
            if not carb.rect.centerx==385:
                
                carbspeed=+5
                anglebspeed=-11
            elif carb.rect.centerx==385:
                carbspeed=0
                anglebspeed=0





        carr.movel()   
        carr.mover()    
        carb.movel()
        carb.mover()  
    
   
 
      

        carr.angle(angler)    
        carb.angle(angleb)
        obstaclesr.update(speed)
        obstaclesb.update(speed)
        map_position +=speed
        if map_position>300:
            create_map()
            map_position=0

        animate()


        collision()        
        
        


            
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
    
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_DOWN:
                done=False
                print done
                pygame.init()
                screen=pygame.display.set_mode([440,783])
                clock=pygame.time.Clock()
                angler=0
                angleb=0
                carrspeed=0
                carbspeed=0
                
                carr=CarRClass()
                carb=CarBClass()

                obstaclesr=pygame.sprite.Group()
                obstaclesb=pygame.sprite.Group()
                bbar=bottombar([0,783])
                sbarm=straightbar([220,0])
                sbarl=straightbars([110,0])
                sbarr=straightbars([330,0])
                map_position=0
                groupobsr=[]
                groupobsb=[]
                colr=-130
                colb=random.choice([-90,-50,-170,-210])
                create_map()
                running=True
                point=0
                speed=5
                point_font=pygame.font.Font(None,70)
                point_surf=point_font.render(str(point),1,(255,255,255))
                point_pos=[355,15]
                
                                
                

         
                        
               

    
        


    

        
print clock.get_fps()
print speed

pygame.quit()





                               
