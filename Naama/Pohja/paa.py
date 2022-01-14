'''
Created on 24.5.2021

@author: Artturi
'''
import pygame
import os

class Donitsi(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image= pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arthur")
vec = pygame.math.Vector2

pygame.init()  
pygame.mixer.quit()
 
KERMA = (255, 253, 238)
FPS = 100

silma_leveys, silma_korkeus = int(WIDTH * 0.08), int(HEIGHT * 0.08)
naama_leveys, naama_korkeus = WIDTH, HEIGHT

NAAMA_IMAGE = pygame.image.load(os.path.join('Assets', 'cartturi2.png'))
SILMA_IMAGE = pygame.image.load(os.path.join('Assets', 'silma2.png'))

SILMA = pygame.transform.scale(SILMA_IMAGE, (silma_leveys, silma_korkeus))
NAAMA = pygame.transform.scale(NAAMA_IMAGE, (naama_leveys, naama_korkeus))


def piirra_ikkuna():
    WIN.fill((KERMA))

def piirra_naama(naama):
    WIN.blit(NAAMA,(0, 0))
    
def oikea_silma(silma):
    keskipiste = vec(WIDTH * 0.633, HEIGHT * 0.4845)
    suunta(keskipiste, silma)
    
def vasen_silma(silma):
    keskipiste = vec(WIDTH * 0.372, HEIGHT * 0.48)
    suunta(keskipiste, silma)
    
def suunta(keskipiste, silma):
    
    hiiri_x, hiiri_y = pygame.mouse.get_pos()

    liikkuma = 0.026
    uusi_suunta = keskipiste
    etaisyys_x = keskipiste.x - hiiri_x
    etaisyys_y = keskipiste.y - hiiri_y
   
    if hiiri_x >= keskipiste.x and hiiri_y >= keskipiste.y:
        uusi_suunta = keskipiste - vec(etaisyys_x * liikkuma, etaisyys_y * liikkuma) 
    if hiiri_x < keskipiste.x and hiiri_y < keskipiste.y:
        uusi_suunta = keskipiste - vec(etaisyys_x * liikkuma, etaisyys_y * liikkuma) 
    if hiiri_x < keskipiste.x and hiiri_y >= keskipiste.y:
        uusi_suunta = keskipiste - vec(etaisyys_x * liikkuma, etaisyys_y * liikkuma) 
    if hiiri_x >= keskipiste.x and hiiri_y < keskipiste.y:
        uusi_suunta = keskipiste - vec(etaisyys_x * liikkuma, etaisyys_y * liikkuma) 

    silma.x, silma.y = uusi_suunta
    
    WIN.blit(SILMA,(silma.x - silma_leveys/2, silma.y - silma_korkeus/2))
   
    
def main():
    silma = pygame.Rect(WIDTH/2 - silma_korkeus/2, HEIGHT/2 - silma_korkeus/2, silma_leveys, silma_korkeus)
    naama = pygame.Rect(0, 0, WIDTH, HEIGHT)
    clock = pygame.time.Clock()
    running = True
    while running:

        clock.tick(FPS)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:            
                running = False
                
       
        
        pygame.mouse.set_visible(True)
        hiiri_liikkuu = pygame.mouse.get_focused()
        if hiiri_liikkuu == True:
            
            piirra_ikkuna()
            oikea_silma(silma)
            vasen_silma(silma)
            piirra_naama(naama)
            #donitsi_ryhma.draw(WIN)
                        
        pygame.display.update()
       
    pygame.quit() 
    
if __name__== "__main__":
    main()
