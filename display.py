import pygame
import sys



def display(image_paths):
    pygame.init()

    #these are good default values
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Prediction Visualizations")
    images = [pygame.image.load(path).convert_alpha() for path in image_paths]

    #this is good for default res
    scale_factor = 0.3  

    #scale down images 
    scaled_images = [pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor))) for image in images]

    #pygame stuff 
    running = True
    index = 0
    clock = pygame.time.Clock()  
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        screen.blit(scaled_images[index], (screen_width // 2 - scaled_images[index].get_width() // 2, screen_height // 2 - scaled_images[index].get_height() // 2))
        pygame.display.flip()
        index = (index + 1) % len(scaled_images)
        clock.tick(5)  
    pygame.quit()
    sys.exit()

