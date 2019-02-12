import pygame

class TankObj(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.degree = 0
        self.original = pygame.Surface([20, 15], pygame.SRCALPHA)
        self.original.fill(color)
        
        self.image = pygame.Surface([20, 15], pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
    
    def rotate(self):
        temp = self.rect
        self.degree += 5
        self.image = pygame.transform.rotozoom(self.original, self.degree, 1)
        self.rect = temp
#         x, y = self.rect.center  # Save its current center.
#         print(x, y)
#         self.rect = self.image.get_rect()  # Replace old rect with new rect.
#         self.rect.center = (x, y)  # Put the new rect's center at old center.