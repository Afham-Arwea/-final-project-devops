import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number - GLM Lab")

font = pygame.font.Font(None, 32)
secret_number = random.randint(1, 100)
user_input = ""
feedback = "Type your guess and hit Enter!"
attempts = 0

while True:
    screen.fill((30, 30, 30))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.isdigit():
                    guess = int(user_input)
                    attempts += 1
                    if guess < secret_number:
                        feedback = "Too low!"
                    elif guess > secret_number:
                        feedback = "Too high!"
                    else:
                        feedback = f"Correct! Steps: {attempts}. Resetting..."
                        secret_number = random.randint(1, 100)
                        attempts = 0
                else:
                    feedback = "Please type a valid number!"
                user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                if event.unicode.isdigit():
                    user_input += event.unicode

    # Render texts
    txt_title = font.render("Guess Number (1-100)", True, (255, 255, 255))
    txt_input = font.render(f"Your Guess: {user_input}", True, (0, 255, 255))
    txt_feedback = font.render(feedback, True, (255, 255, 0))
    
    screen.blit(txt_title, (50, 40))
    screen.blit(txt_input, (50, 120))
    screen.blit(txt_feedback, (50, 200))
    
    pygame.display.flip()
