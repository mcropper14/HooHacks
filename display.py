import pygame
import sys

def display(image_paths1, image_paths2=None):
    pygame.init()
    
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Prediction Visualizations")

    
    background_image_path = "/home/cropthecoder/Downloads/sprites/pxArt.png"
    background_image = pygame.image.load(background_image_path).convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    images1 = [pygame.image.load(path).convert_alpha() for path in image_paths1]

    if image_paths2:
        images2 = [pygame.image.load(path).convert_alpha() for path in image_paths2]

    scale_factor = 0.3  
    scaled_images1 = [pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor))) for image in images1]

    if image_paths2:
        scaled_images2 = [pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor))) for image in images2]
    
    clock = pygame.time.Clock()  
    index1 = 0
    index2 = 0 if image_paths2 else None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))

        screen.blit(scaled_images1[index1], (screen_width // 4 - scaled_images1[index1].get_width() // 2, screen_height // 2 - scaled_images1[index1].get_height() // 2))

        if image_paths2:
            screen.blit(scaled_images2[index2], (screen_width // 2 + screen_width // 8 - scaled_images2[index2].get_width() // 2, screen_height // 2 - scaled_images2[index2].get_height() // 2))

        pygame.display.flip()

        index1 = (index1 + 1) % len(scaled_images1)
        if image_paths2:
            index2 = (index2 + 1) % len(scaled_images2)

        clock.tick(5)  

    pygame.quit()
    sys.exit()



