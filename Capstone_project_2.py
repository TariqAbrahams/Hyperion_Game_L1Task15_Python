# Import Library.
import pygame
import random

# Initiates the "pygame" library
pygame.init()

# Width & Height of Game display window.
window_width = 1366
window_height = 768


# Displays the name of the game on the top bar of the window.
pygame.display.set_caption("Dragon Ball Food Hunt")
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
# Background image.
background1 = pygame.image.load('background1.jpg')
# Player:
player1 = pygame.image.load('player1.png')
# Enemies:
enemy1 = pygame.image.load('enemy1.png')
enemy2 = pygame.image.load('enemy2.png')
enemy3 = pygame.image.load('enemy3.png')
# Prize:
prize1 = pygame.image.load('prize1.png')


# Variables to return the player character height & width.
player_height = player1.get_height()
player_width = player1.get_width()

print("This is the height of the player image: " + str(player_height))
print("This is the width of the player image: " + str(player_width))

# Variables to return "enemy1" height & width
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

print("This is the height of the enemy1 image: " + str(enemy1_height))
print("This is the width of the enemy1 image: " + str(enemy1_width))

# Variables to return "enemy2" height & width
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

print("This is the height of the enemy2 image: " + str(enemy2_height))
print("This is the width of the enemy2 image: " + str(enemy2_width))

# Variables to return "enemy3" height & width
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

print("This is the height of the enemy3 image: " + str(enemy3_height))
print("This is the width of the enemy3 image: " + str(enemy3_width))

# Variables to return "prize1" height & width
prize1_height = prize1.get_height()
prize1_width = prize1.get_width()

print("This is the height of the prize1 image: " + str(prize1_height))
print("This is the width of the prize1 image: " + str(prize1_width))

# Player character starting position inside the game window.
player_x = 550
player_y = 250
velocity = 10

# Enemy 1 starting position on the game window.
enemy1_y = 800
enemy1_x = random.randint(0, window_width - enemy1_width)

# Enemy 2 starting position on the game window.
enemy2_y = - 500
enemy2_x = random.randint(0, window_width - enemy2_width)

# Enemy 3 starting position on the game window.
enemy3_x = - 1400
enemy3_y = random.randint(0, window_height - enemy3_height)

# Prize starting position on the game window.
prize1_x = 3000
prize1_y = random.randint(0, window_height - prize1_height)

# Boolean values to determine whether the directional keys is pressed or not.
KeyLeft = False
KeyRight = False
KeyUp = False
KeyDown = False

# Main Loop for the Game to be able to run successfully.
while 1:
    window.fill((0, 0, 0))  # Clears the screen.
    window.blit(background1, (0, 0))    # Adds a background to the game window
    window.blit(player1, (player_x, player_y))  # Draws the player character on to the game window, at a certain position
    window.blit(enemy1, (enemy1_x, enemy1_y))   # Draws the enemy character on to the game window, at a certain position
    window.blit(enemy2, (enemy2_x, enemy2_y))
    window.blit(enemy3, (enemy3_x, enemy3_y))
    window.blit(prize1, (prize1_x, prize1_y))   #Draws the prize object onto the game window, at a certain position

    # Updates the game window if any variables are added to the main loop.
    pygame.display.flip()

    # Used to loop through the events in the game.
    for event in pygame.event.get():
        
        # Checks if the user quit the game then exits
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Tests if the user is actually pressing the directional keys on the keyboard.
        if event.type == pygame.KEYDOWN:

            # Tests if the key pressed down is the correct key.
            if event.key == pygame.K_LEFT:
                KeyLeft = True
            if event.key == pygame.K_RIGHT:
                KeyRight = True
            if event.key == pygame.K_UP:
                KeyUp = True
            if event.key == pygame.K_DOWN:
                KeyDown = True

        # Tests if the user is not pressing any of the directional keys.
        if event.type == pygame.KEYUP:
            # Tests if the key is up or released is correct.
            if event.key == pygame.K_LEFT:
                KeyLeft = False
            if event.key == pygame.K_RIGHT:
                KeyRight = False
            if event.key == pygame.K_UP:
                KeyUp = False
            if event.key == pygame.K_DOWN:
                KeyDown = False

    # The following "IF" functions ensures that the player does not move out of the game window and their movement direction.
    if KeyLeft:
        if player_x > velocity:
            player_x -= 20  # Determines player movement speed.
    if KeyRight:
        if player_x < window_width - player_width:
            player_x += 20
    if KeyUp:
        if player_y > velocity:
            player_y -= 20
    if KeyDown:
        if player_y < window_height - player_height:
            player_y += 20

    # Bounding box for the player character.
    playerBox = pygame.Rect((player1.get_rect()))
    playerBox.top = player_y
    playerBox.left = player_x

    # Bounding box for enemy 1 character.
    enemy1Box = pygame.Rect((enemy1.get_rect()))
    enemy1Box.top = enemy1_y
    enemy1Box.left = enemy1_x
    enemy1_y -= 15   # Determines Enemy 1 movement speed.

    # Bounding box for enemy 2 character.
    enemy2Box = pygame.Rect((enemy2.get_rect()))
    enemy2Box.top = enemy2_y
    enemy2Box.left = enemy2_x
    enemy2_y += 15   # Determines Enemy 2 movement speed.

    # Bounding Box for enemy 3 character.
    enemy3Box = pygame.Rect((enemy3.get_rect()))
    enemy3Box.top = enemy3_y
    enemy3Box.left = enemy3_x
    enemy3_x += 15   # Determines Enemy 3 movement speed.

    # Bounding box for prize object.
    prize1Box = pygame.Rect((prize1.get_rect()))
    prize1Box.top = prize1_y
    prize1Box.left = prize1_x
    prize1_x -= 18  # Determines prize object movement speed.
    
    # Tests collision of the boxes above, if the player box collides with any of the enemy boxes you lose and the game will exit.
    if playerBox.colliderect(enemy1Box):
        print("You Lost to Freezer!!!")
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemy2Box):
        print("You Lost to Broly!!!")
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemy3Box):
        print("You Lost to Super Broly!!!")
        pygame.quit()
        exit(0)

    # If player box collides with the prize object box you win and the game will exit.
    if playerBox.colliderect(prize1Box):
        print("Congratulations Goku You Won, Enjoy your treat!!!")
        pygame.quit()
        exit(0)

# Source of pictures: https://www.freepngimg.com, and google.
