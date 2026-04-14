import pygame as pg
import random
from sys import exit
#loop needed to run
def main():
    #starts the pygame module
    pg.init()
    #starts music player for pygame
    pg.mixer.init()
    #screen size
    #width
    x = 1250
    #height
    y = 600
    #defines screen
    screen = pg.display.set_mode((x, y))
    #name for game window
    pg.display.set_caption('Kortspel')

    dragging = False
    volume = 1.0
    singleplayer = True
    bot = 1
    bot1 = 0
    dif = 2
    mode = "Texas Hold'em"
    mode1 = None
    fold_poker = False
    info = False

    #below is functions used in the code
    def hover_logic(background_pos, background, colour_before, colour_after):
        """background position, background, colour without mouse, colour with mouse, returns background"""
        
        if background_pos.collidepoint(mouse_pos):
            background.fill(colour_after)
        else:
            background.fill(colour_before)
        
        return background
    
    def button(width, height, colour, placementx, placementy):
        """width, height, colour, x, y, returns surface and surface pos"""
        background = pg.Surface((width, height))
        background.fill(colour)
        background_pos = background.get_rect()
        background_pos.center = (placementx, placementy)

        return background, background_pos
    
    def text(font, fontsize, message, colour, xpos, ypos):
        """font, size, message, colour (x, y, z), x, y, returns text and text pos"""
        message = str(message)
        textfont = pg.font.Font(font, fontsize)
        texti = textfont.render(message, 1, (colour))
        textpos = texti.get_rect()
        textpos.center = (xpos, ypos)
        return texti, textpos
    
    def click(surface):
        """surface (pos), returns true or false"""
        for event in events:
            if event.type == pg. MOUSEBUTTONDOWN:
                if surface.collidepoint(mouse_pos):
                    return True
                else:
                    return False
    
    #main fonts
    fortuner_font = ('fortuner.otf')
    
    #below is the buttons and text

    #background for main menu
    background_menu = pg.image.load('Graphics/Background_menu2.png')

    #title background
    background_title, background_title_pos = button(500, 60, "dimgray", x//2, y//2-180)

    #start button background
    background_start, background_start_pos = button(130, 40, "dimgray", x//2, y//2-80)

    #menu button
    background_meny, background_meny_pos = button(120, 40, "dimgray", x//2, y//2)

    #exit button
    background_exit, background_exit_pos = button(160, 40, "dimgray", x//2, y//2+80)

    #text for title
    text_titel, textpos_titel = text(fortuner_font, 60, "Vändtia och mer!", (10, 10, 10), x//2, y//2-180)

    #text for start button
    text_start, textpos_start = text(fortuner_font, 40, "Start", (10, 10, 10), x//2, y//2-80)

    #text for menu button
    text_meny, textpos_meny = text(fortuner_font, 36, "Meny", (10, 10, 10), x//2, y//2)

    #text for exit button
    text_avsluta, textpos_avsluta = text(fortuner_font, 36, "Avsluta", (10, 10, 10), x//2, y//2+80)

    #background for pop up menu, identical to background 3 so it will be removed, background 3 remains
    background3, background3_pos = button(1000, 500, "dimgray", x//2, y//2)

    #multiplayer button
    background_start_fler, background_start_fler_pos = button(400, 200, "lightgray", x//2+250, y//2-20)

    #singleplayer button
    background_start_ensam, background_start_ensam_pos = button(400, 200, "lightgray", x//2-250, y//2-20)

    #exit button for start menu
    background_start_exit, background_start_exit_pos = button(200, 75, "lightgray", x//2, y//2+150)

    #exit button for settings
    background_menu_exit, background_menu_exit_pos = button(200, 75, "lightgray", x//2, y//2+150)

    #singleplayer button for vänd10
    background_start_ensam_vänd10, background_start_ensam_vänd10_pos = button(400, 200, "lightgray", x//2-250, y//2-20)

    #singleplayer button for poker
    background_start_ensam_poker, background_start_ensam_poker_pos = button(400, 200, "lightgray", x//2+250, y//2-20)

    #text for singleplayer button
    text_start_ensam, textpos_start_ensam = text(fortuner_font, 36, "Ensamspelare", (10, 10, 10), x//2-250, y//2-20)

    #text for multiplayer button
    text_start_flera, textpos_start_flera = text(fortuner_font, 36, "Fleraspelare", (10, 10, 10), x//2+250, y//2-20)

    #text for exit button for start
    text_start_exit, textpos_start_exit = text(fortuner_font, 36, "Avbryt", (10, 10, 10), x//2, y//2+150)
    
    #text for options titel
    text_menu_work, textpos_menu_work = text(fortuner_font, 60, "Alternativ", (10, 10, 10), x//2, y//2-180)

    #text for start select titel
    text_start_game, textpos_start_game = text(fortuner_font, 60, "Välj speltyp", (10, 10, 10), x//2, y//2-180)

    #text for vänd-10 button
    text_start_ensam_vänd10, textpos_start_ensam_vänd10 = text(fortuner_font, 36, "Vändtia", (10, 10, 10), x//2-250, y//2-20)

    #text for poker button
    text_start_ensam_poker, textpos_start_ensam_poker = text(fortuner_font, 36, "Poker", (10, 10, 10), x//2+250, y//2-20)

    #text for singleplayer select titel
    text_start_game_titel, textpos_start_game_titel = text(fortuner_font, 60, "Välj spelläge", (10, 10, 10), x//2, y//2-180)

    #sound button for settings
    background_menu_sound, background_menu_sound_pos = button(400, 200, "lightgray", x//2+250, y//2-20)

    #text for sound options
    text_menu_sound, textpos_menu_sound = text(fortuner_font, 36, "Ljud", (10, 10, 10), x//2+250, y//2-20)

    #image button for settings
    background_menu_image, background_menu_image_pos = button(400, 200, "lightgray", x//2-250, y//2-20)

    #text for image options
    text_menu_image, textpos_menu_image = text(fortuner_font, 36, "Bild", (10, 10, 10), x//2-250, y//2-20)

    #text for sound titel
    text_options_sound, textpos_options_sound = text(fortuner_font, 60, "Musik", (10, 10, 10), x//2, y//2-180)

    #text for image titel
    text_options_image, textpos_options_image = text(fortuner_font, 60, "Välj bildinställningar", (10, 10, 10), x//2, y//2-180)

    #music 1 button for sound
    background_menu_sound1, background_menu_sound1_pos = button(300, 175, "lightgray", x//2-275, y//2-100)

    #music 2 button for sound
    background_menu_sound2, background_menu_sound2_pos = button(300, 175, "lightgray", x//2+275, y//2-100)

    #text for music 1 sound
    text_menu_sound1, textpos_menu_sound1 = text(fortuner_font, 36, "Musik 1", (10, 10, 10,), x//2-275, y//2-100)
    
    #text for music 2 sound
    text_menu_sound2, textpos_menu_sound2 = text(fortuner_font, 36, "Musik 2", (10, 10, 10), x//2+275, y//2-100)

    #background for starting game menu
    background_starting, background_starting_pos = button(1150, 500, "dimgray", x//2, y//2)

    #exit button for starting
    background_starting_exit, background_starting_exit_pos = button(160, 40, "lightgray", x//2-460, y//2+200)

    #text for exit button starting
    text_starting_exit, textpos_starting_exit = text(fortuner_font, 36, "Avbryt", (10, 10, 10), x//2-460, y//2+200)

    #text for starting game poker titel
    text_starting_poker_titel, textpos_starting_poker_titel = text(fortuner_font, 60, "Poker", (10, 10, 10), x//2, y//2-210)

    #text for starting game vänd10 titel
    text_starting_vänd10_titel, textpos_starting_vänd10_titel = text(fortuner_font, 60, "Vändtia", (10, 10, 10), x//2, y//2-210)

    #under development for multiplayer menus
    text_starting_multi_development, textpos_starting_multi_development = text(fortuner_font, 120, "Under utveckling", (10, 10, 10), x//2, y//2)

    #text for bots button
    text_starting_single_bots, textpos_starting_single_bots = text(fortuner_font, 36, "Bottar", (10, 10, 10), x//2-460, y//2-210)

    #text for bots difficulity
    text_dif_titel, textpos_dif_titel = text(fortuner_font, 36, "Svårighetsgrad", (10, 10, 10), x//2-345, y//2-80)

    #button for +, -
    button_starting_single_minus, button_starting_single_minus_pos = button(50, 50, "lightgray", x//2-520, y//2-160)
    button_starting_single_plus, button_starting_single_plus_pos = button(50, 50, "lightgray", x//2-400, y//2-160)

    #text for +, -
    text_starting_single_minus, textpos_starting_single_minus = text(fortuner_font, 60, "-", (10, 10, 10), x//2-520, y//2-160)
    text_starting_single_plus, textpos_starting_single_plus = text(fortuner_font, 60, "+", (10, 10, 10), x//2-400, y//2-160)

    #button for bot amount single
    background_starting_single_botnr, background_starting_single_botnr_pos = button(70, 50, "lightgray", x//2-460, y//2-160)

    #buttons for bot difficulity
    background_starting_single_dif, background_starting_single_dif_pos = button(300, 50, "lightgray", x//2-345, y//2-30)
    #buttons for +, -
    background_starting_single_dif_plus, background_starting_single_dif_plus_pos = button(50, 50, "lightgray", x//2-170, y//2-30)
    background_starting_single_dif_minus, background_starting_single_dif_minus_pos = button(50, 50, "lightgray", x//2-520, y//2-30)

    #text for bot difficulity
    text_starting_single_easydif, textpos_starting_single_easydif = text(fortuner_font, 48, "Lätt", (10, 10, 10), x//2-345, y//2-30)
    text_starting_single_mediumdif, textpos_starting_single_mediumdif = text(fortuner_font, 48, "Balanserad", (10, 10, 10), x//2-345, y//2-30)
    text_starting_single_harddif, textpos_starting_single_harddif = text(fortuner_font, 48, "Svår", (10, 10, 10), x//2-345, y//2-30)

    #text2 for +, -
    text_starting_single_plusdif, textpos_starting_single_plusdif = text(fortuner_font, 48, "+", (10, 10, 10), x//2-170, y//2-30)
    text_starting_single_minusdif, textpos_starting_single_minusdif = text(fortuner_font, 48, "-", (10, 10, 10), x//2-520, y//2-30)

    #button for poker game modes
    background_fold_down, background_fold_down_pos = button(280, 50, "lightgray", x//2, y//2-160)
    background_fold_down1, background_fold_down1_pos = button(280, 50, "lightgray", x//2, y//2-109)
    background_fold_down2, background_fold_down2_pos = button(280, 50, "lightgray", x//2, y//2-58)
    background_fold_down3, background_fold_down3_pos = button(280, 50, "lightgray", x//2, y//2-7)

    #text för poker game modes
    text_fold_down1, textpos_fold_down1 = text(fortuner_font, 36, "Texas Hold'em", (10, 10, 10), x//2, y//2-109)
    text_fold_down2, textpos_fold_down2 = text(fortuner_font, 36, "Omaha Hold'em", (10, 10, 10), x//2, y//2-58)
    text_fold_down3, textpos_fold_down3 = text(fortuner_font, 34, "Seven-Card Stud", (10, 10, 10), x//2, y//2-7)

    #exit button for starting
    background_starting_start, background_starting_start_pos = button(160, 40, "lightgray", x//2+460, y//2+200)

    #text for exit button starting
    text_starting_start, textpos_starting_start = text(fortuner_font, 36, "Starta", (10, 10, 10), x//2+460, y//2+200)

    #text for vändtia regler
    text_fold_down11, textpos_fold_down11 = text(fortuner_font, 36, "Utan stege", (10, 10, 10), x//2, y//2-109)
    text_fold_down22, textpos_fold_down22 = text(fortuner_font, 36, "Med stege", (10, 10, 10), x//2, y//2-58)

    #button for info single
    background_starting_info, background_starting_info_pos = button(170, 50, "lightgray", x//2+460, y//2-160)

    #text for info single
    text_starting_info, textpos_starting_info = text(fortuner_font, 50, "Info", (10, 10, 10), x//2+460, y//2-160)

    #background for info page
    background_info, background_info_pos = button(900, 450, "dimgray", x//2, y//2)

    #background exit info
    background_info_exit, background_info_exit_pos = button (50, 50, "red", x//2+425, y//2-200)

    #makes it so you can select frame rate (the speed that the code runs), is selected at the end of the game loop
    clock = pg.time.Clock()

    #used AI for this due to being unsure of how to implement a sliding bar, but now I understand the principal on how to add it in future programs
    slider_rect = pg.Rect(x//2 - 200, y//2+40, 400, 10)  #bar
    handle_rect = pg.Rect(0, 0, 20, 30)               #handle
    handle_rect.center = (slider_rect.right, slider_rect.centery)

    #used to determine which loop inside of the main loop that needs to run
    start = "menu"
    #used to change music
    music = "standard"
    #used to switch music when new music is selected
    past_music = "annoying"
    #main game loop
    while True:
        #mouse tracking
        mouse_pos = pg.mouse.get_pos()
        #event handling, may only call pg.event.get() once in the main loop, calling it multiple times clears it out
        #that causes the code to not handle certain events correctly
        events = pg.event.get()

        #logic for lobby music
        if music != past_music:
            pg.mixer.music.fadeout(500)

            if music == "standard":
                pg.mixer.music.load("Audio/lobby_music.mp3")
                pg.mixer.music.set_volume(volume)
            elif music == "annoying":
                pg.mixer.music.load("Audio/annoying.mp3")
                pg.mixer.music.set_volume(volume)

            pg.mixer.music.play(-1)

            previous_state = start
            past_music = music

        #handle if the x is pressed top left of the screen, and then closes it
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.MOUSEBUTTONDOWN and handle_rect.collidepoint(mouse_pos):
                dragging = True
            if event.type == pg.MOUSEBUTTONDOWN and slider_rect.collidepoint(mouse_pos):
                dragging = True

            if event.type == pg.MOUSEBUTTONUP:
                dragging = False
        
        #is in main menu
        if start == "menu":
            #draw main menu background background
            screen.blit(background_menu, (0, 0))

            hover_logic(background_start_pos, background_start, "dimgray", "lightgray")
            hover_logic(background_meny_pos, background_meny, "dimgray", "lightgray")
            hover_logic(background_exit_pos, background_exit, "dimgray", "lightgray")

            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if background_start_pos.collidepoint(mouse_pos):
                        print("Start button clicked!")
                        start = "start"
                        break
                    elif background_meny_pos.collidepoint(mouse_pos):
                        print("Menu button clicked!")
                        start = "options"
                        break
                    elif background_exit_pos.collidepoint(mouse_pos):
                        pg.quit()
                        exit()

            #draw buttons
            screen.blit(background_start, background_start_pos)
            screen.blit(background_meny, background_meny_pos)
            screen.blit(background_exit, background_exit_pos)
            screen.blit(background_title, background_title_pos)
            screen.blit(text_titel, textpos_titel)

            #draw text ON TOP of buttons
            #for the text to be visible, it needs to be blited on the screen AFTER the main button base was added
            screen.blit(text_start, textpos_start)
            screen.blit(text_meny, textpos_meny)
            screen.blit(text_avsluta, textpos_avsluta)

            #update screen
            pg.display.update()

        #selected button is the start button
        elif start == "start":
            hover_logic(background_start_ensam_pos, background_start_ensam, "lightgray", "white")
            hover_logic(background_start_fler_pos, background_start_fler, "lightgray", "white")
            hover_logic(background_start_exit_pos, background_start_exit, "lightgray", "white")
            
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if background_start_ensam_pos.collidepoint(mouse_pos):
                        print("Ensam")
                        start = "gamemode"
                        singleplayer = True
                        break
                    elif background_start_fler_pos.collidepoint(mouse_pos):
                        print("Fler")
                        start = "gamemode"
                        singleplayer = False
                        break
                    elif background_start_exit_pos.collidepoint(mouse_pos):
                        print("Exit")
                        start = "menu"
                        break
                    elif not background3_pos.collidepoint(mouse_pos):
                        print("Exit")
                        start = "menu"
                        break

            screen.blit(background_menu, (0, 0))
            screen.blit(background3, background3_pos)
            screen.blit(background_start_ensam, background_start_ensam_pos)
            screen.blit(background_start_fler, background_start_fler_pos)
            screen.blit(background_start_exit, background_start_exit_pos)
            screen.blit(text_start_ensam, textpos_start_ensam)
            screen.blit(text_start_flera, textpos_start_flera)
            screen.blit(text_start_exit, textpos_start_exit)
            screen.blit(text_start_game_titel, textpos_start_game_titel)
            pg.display.update()

        #selected button meny
        elif start == "options":
            screen.blit(background_menu, (0, 0))
            screen.blit(background3, background3_pos)

            hover_logic(background_menu_exit_pos, background_menu_exit, "lightgray", "white")
            hover_logic(background_menu_image_pos, background_menu_image, "lightgray", "white")
            hover_logic(background_menu_sound_pos, background_menu_sound, "lightgray", "white")
            
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if background_menu_exit_pos.collidepoint(mouse_pos):
                        print("Lämnar meny")
                        start = "menu"
                        break
                    elif not background3_pos.collidepoint(mouse_pos):
                        print("Exit")
                        start = "menu"
                        break
                    elif background_menu_sound_pos.collidepoint(mouse_pos):
                        print("Ljud")
                        start = "sound"
                        break
                    elif background_menu_image_pos.collidepoint(mouse_pos):
                        print("Bild")
                        start = "image"
                        break
            screen.blit(background_menu_exit, background_menu_exit_pos)
            screen.blit(text_start_exit, textpos_start_exit)
            screen.blit(text_menu_work, textpos_menu_work)
            screen.blit(background_menu_sound, background_menu_sound_pos)
            screen.blit(background_menu_image, background_menu_image_pos)
            screen.blit(text_menu_sound, textpos_menu_sound)
            screen.blit(text_menu_image, textpos_menu_image)
            pg.display.update()

        #selected sound in options
        elif start == "sound":

            hover_logic(background_menu_exit_pos, background_menu_exit, "lightgray", "white")
            hover_logic(background_menu_sound1_pos, background_menu_sound1, "lightgray", "white")
            hover_logic(background_menu_sound2_pos, background_menu_sound2, "lightgray", "white")

            if dragging == True:
                # Move handle with mouse (but clamp to slider)
                handle_rect.centerx = max(slider_rect.left, min(mouse_pos[0], slider_rect.right))

                # Convert position → volume (0 to 1)
                volume = (handle_rect.centerx - slider_rect.left) / slider_rect.width

                # Apply volume immediately
                pg.mixer.music.set_volume(volume)

            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if background_menu_exit_pos.collidepoint(mouse_pos):
                        print("Lämnar meny")
                        start = "options"
                        break
                    elif not background3_pos.collidepoint(mouse_pos):
                        print("Exit")
                        start = "menu"
                        break
                    elif background_menu_sound1_pos.collidepoint(mouse_pos):
                        print("Musik 1")
                        music = "standard"
                    elif background_menu_sound2_pos.collidepoint(mouse_pos):
                        print("Musik 2")
                        music = "annoying"

            screen.blit(background_menu, (0,0))
            screen.blit(background3, background3_pos)
            screen.blit(background_menu_exit, background_menu_exit_pos)
            screen.blit(text_start_exit, textpos_start_exit)
            screen.blit(text_options_sound, textpos_options_sound)
            screen.blit(background_menu_sound1, background_menu_sound1_pos)
            screen.blit(background_menu_sound2, background_menu_sound2_pos)
            screen.blit(text_menu_sound1, textpos_menu_sound1)
            screen.blit(text_menu_sound2, textpos_menu_sound2)
            
            pg.draw.rect(screen, "darkgray", slider_rect)
            pg.draw.rect(screen, "white", handle_rect)

            pg.display.update()

        #selected image in options
        elif start == "image":

            hover_logic(background_menu_exit_pos, background_menu_exit, "lightgray", "white")

            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if background_menu_exit_pos.collidepoint(mouse_pos):
                        print("Lämnar meny")
                        start = "options"
                        break
                    elif not background3_pos.collidepoint(mouse_pos):
                        print("Exit")
                        start = "menu"
                        break

            screen.blit(background_menu, (0,0))
            screen.blit(background3, background3_pos)
            screen.blit(background_menu_exit, background_menu_exit_pos)
            screen.blit(text_start_exit, textpos_start_exit)
            screen.blit(text_options_image, textpos_options_image)

            pg.display.update()

        #selected game mode is singleplayer
        elif start == "gamemode":
            screen.blit(background_menu, (0, 0))
            screen.blit(background3, background3_pos)

            hover_logic(background_menu_exit_pos, background_menu_exit, "lightgray", "white")
            hover_logic(background_start_ensam_poker_pos, background_start_ensam_poker, "lightgray", "white")
            hover_logic(background_start_ensam_vänd10_pos, background_start_ensam_vänd10, "lightgray", "white")
        
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if background_menu_exit_pos.collidepoint(mouse_pos):
                        print("Lämnar meny")
                        start = "start"
                        break
                    elif not background3_pos.collidepoint(mouse_pos):
                        print("Exit")
                        start = "menu"
                        break
                    elif background_start_ensam_poker_pos.collidepoint(mouse_pos):
                        print("Poker")
                        mode = "Texas Hold'em"
                        start = "poker"
                        break
                    elif background_start_ensam_vänd10_pos.collidepoint(mouse_pos):
                        print("Vänd10")
                        mode = "Utan stege"
                        start = "vänd10"
                        break
            screen.blit(background_menu_exit, background_menu_exit_pos)
            screen.blit(text_start_exit, textpos_start_exit)
            screen.blit(text_start_game, textpos_start_game)
            screen.blit(background_start_ensam_poker, background_start_ensam_poker_pos)
            screen.blit(background_start_ensam_vänd10, background_start_ensam_vänd10_pos)
            screen.blit(text_start_ensam_poker, textpos_start_ensam_poker)
            screen.blit(text_start_ensam_vänd10, textpos_start_ensam_vänd10)

            pg.display.update()
        
        elif start == "poker" and singleplayer == True:
            if info != True:
                hover_logic(background_starting_exit_pos, background_starting_exit, "lightgray", "white")
                hover_logic(button_starting_single_minus_pos, button_starting_single_minus, "lightgray", "white")
                hover_logic(button_starting_single_plus_pos, button_starting_single_plus, "lightgray", "white")
                hover_logic(background_starting_single_dif_plus_pos, background_starting_single_dif_plus, "lightgray", "white")
                hover_logic(background_starting_single_dif_minus_pos, background_starting_single_dif_minus, "lightgray", "white")
                hover_logic(background_fold_down_pos, background_fold_down, "lightgray", "white")
                hover_logic(background_starting_start_pos, background_starting_start, "lightgray", "white")
                hover_logic(background_starting_info_pos, background_starting_info, "lightgray", "white")

            if info != True:

                if click(button_starting_single_minus_pos):
                    if bot > 1:
                        bot-=1
            
                if click(button_starting_single_plus_pos):
                    if bot <9:
                        bot+=1

                if click(background_starting_exit_pos):
                    print("Exit")
                    bot = 1
                    dif = 2
                    start = "menu"

                if click(background_starting_single_dif_minus_pos):
                    if dif >1:
                        dif-=1

                if click(background_starting_single_dif_plus_pos):
                    if dif <3:
                        dif+=1

                if click(background_fold_down_pos):
                    if fold_poker == True:
                        fold_poker = False
                    else:
                        fold_poker = True

                if click(background_starting_start_pos):
                    print("Start")

                if click(textpos_starting_info):
                    info = True
            
            #text for bot amount single
            if bot != bot1:
                bot1 = bot
                text_starting_single_botnr, textpos_starting_single_botnr = text(fortuner_font, 60, bot, (10, 10, 10), x//2-460, y//2-160)

            if mode != mode1:
                mode1 = mode
                text_fold_down, textpos_fold_down = text(fortuner_font, 34, mode, (10, 10, 10), x//2, y//2-160)

            screen.blit(background_menu, (0, 0))
            screen.blit(background_starting, background_starting_pos)
            screen.blit(background_starting_exit, background_starting_exit_pos)
            screen.blit(text_starting_exit, textpos_starting_exit)
            screen.blit(text_starting_poker_titel, textpos_starting_poker_titel)
            screen.blit(text_starting_single_bots, textpos_starting_single_bots)
            screen.blit(button_starting_single_minus, button_starting_single_minus_pos)
            screen.blit(button_starting_single_plus, button_starting_single_plus_pos)
            screen.blit(text_starting_single_minus, textpos_starting_single_minus)
            screen.blit(text_starting_single_plus, textpos_starting_single_plus)
            screen.blit(background_starting_single_botnr, background_starting_single_botnr_pos)
            screen.blit(text_starting_single_botnr, textpos_starting_single_botnr)
            screen.blit(background_starting_single_dif, background_starting_single_dif_pos)
            screen.blit(background_starting_single_dif_plus, background_starting_single_dif_plus_pos)
            screen.blit(background_starting_single_dif_minus, background_starting_single_dif_minus_pos)
            if dif == 1:
                screen.blit(text_starting_single_easydif, textpos_starting_single_easydif)
            elif dif == 2:
                screen.blit(text_starting_single_mediumdif, textpos_starting_single_mediumdif)
            elif dif == 3:
                screen.blit(text_starting_single_harddif, textpos_starting_single_harddif)
            screen.blit(text_starting_single_plusdif, textpos_starting_single_plusdif)
            screen.blit(text_starting_single_minusdif, textpos_starting_single_minusdif)
            screen.blit(background_fold_down, background_fold_down_pos)
            screen.blit(text_fold_down, textpos_fold_down)
            screen.blit(text_dif_titel, textpos_dif_titel)
            screen.blit(background_starting_start, background_starting_start_pos)
            screen.blit(text_starting_start, textpos_starting_start)
            screen.blit(background_starting_info, background_starting_info_pos)
            screen.blit(text_starting_info, textpos_starting_info)

            #if info == True:


            if fold_poker == True:
                hover_logic(background_fold_down1_pos, background_fold_down1, "lightgray", "white")
                hover_logic(background_fold_down2_pos, background_fold_down2, "lightgray", "white")
                hover_logic(background_fold_down3_pos, background_fold_down3, "lightgray", "white")
                hover_logic(background_starting_info_pos, background_starting_info, "lightgray", "white")
                if click(background_fold_down1_pos):
                    mode = "Texas Hold'em"
                    print("Test1")
                    fold_poker = False

                if click(background_fold_down2_pos):
                    mode = "Omaha Hold'em"
                    print("Test2")
                    fold_poker = False

                if click(background_fold_down3_pos):
                    mode = "Seven-Card Stud"
                    print("Test3")
                    fold_poker = False

                

                screen.blit(background_fold_down1, background_fold_down1_pos)
                screen.blit(background_fold_down2, background_fold_down2_pos)
                screen.blit(background_fold_down3, background_fold_down3_pos)
                screen.blit(text_fold_down1, textpos_fold_down1)
                screen.blit(text_fold_down2, textpos_fold_down2)
                screen.blit(text_fold_down3, textpos_fold_down3)

            if info == True:
                hover_logic(background_info_exit_pos, background_info_exit, "darkred", "crimson")
                screen.blit(background_info, background_info_pos)
                screen.blit(background_info_exit, background_info_exit_pos)

            pg.display.update()

        elif start == "vänd10" and singleplayer == True:
            hover_logic(background_starting_exit_pos, background_starting_exit, "lightgray", "white")
            hover_logic(button_starting_single_minus_pos, button_starting_single_minus, "lightgray", "white")
            hover_logic(button_starting_single_plus_pos, button_starting_single_plus, "lightgray", "white")
            hover_logic(background_starting_single_dif_plus_pos, background_starting_single_dif_plus, "lightgray", "white")
            hover_logic(background_starting_single_dif_minus_pos, background_starting_single_dif_minus, "lightgray", "white")
            hover_logic(background_fold_down_pos, background_fold_down, "lightgray", "white")
            hover_logic(background_starting_start_pos, background_starting_start, "lightgray", "white")
            hover_logic(background_starting_info_pos, background_starting_info, "lightgray", "white")

            if click(button_starting_single_minus_pos):
                if bot > 1:
                    bot-=1
            
            if click(button_starting_single_plus_pos) == True:
                if bot <4:
                    bot+=1

            if click(background_starting_exit_pos) == True:
                print("Exit")
                bot = 1
                dif = 2
                start = "menu"

            if click(background_starting_single_dif_minus_pos):
                if dif >1:
                    dif-=1

            if click(background_starting_single_dif_plus_pos):
                if dif <3:
                    dif+=1

            if click(background_fold_down_pos):
                if fold_poker == True:
                    fold_poker = False
                else:
                    fold_poker = True

            if click(background_starting_start_pos):
                print("Start")

            if click(textpos_starting_info):
                info = True

            #text for bot amount single
            if bot != bot1:
                bot1 = bot
                text_starting_single_botnr, textpos_starting_single_botnr = text(fortuner_font, 60, bot, (10, 10, 10), x//2-460, y//2-160)

            if mode != mode1:
                mode1 = mode
                text_fold_down, textpos_fold_down = text(fortuner_font, 36, mode, (10, 10, 10), x//2, y//2-160)

            screen.blit(background_menu, (0, 0))
            screen.blit(background_starting, background_starting_pos)
            screen.blit(background_starting_exit, background_starting_exit_pos)
            screen.blit(text_starting_exit, textpos_starting_exit)
            screen.blit(text_starting_vänd10_titel, textpos_starting_vänd10_titel)
            screen.blit(text_starting_single_bots, textpos_starting_single_bots)
            screen.blit(button_starting_single_minus, button_starting_single_minus_pos)
            screen.blit(button_starting_single_plus, button_starting_single_plus_pos)
            screen.blit(text_starting_single_minus, textpos_starting_single_minus)
            screen.blit(text_starting_single_plus, textpos_starting_single_plus)
            screen.blit(background_starting_single_botnr, background_starting_single_botnr_pos)
            screen.blit(text_starting_single_botnr, textpos_starting_single_botnr)
            screen.blit(background_starting_single_dif, background_starting_single_dif_pos)
            screen.blit(background_starting_single_dif_plus, background_starting_single_dif_plus_pos)
            screen.blit(background_starting_single_dif_minus, background_starting_single_dif_minus_pos)
            if dif == 1:
                screen.blit(text_starting_single_easydif, textpos_starting_single_easydif)
            elif dif == 2:
                screen.blit(text_starting_single_mediumdif, textpos_starting_single_mediumdif)
            elif dif == 3:
                screen.blit(text_starting_single_harddif, textpos_starting_single_harddif)
            screen.blit(text_starting_single_plusdif, textpos_starting_single_plusdif)
            screen.blit(text_starting_single_minusdif, textpos_starting_single_minusdif)
            screen.blit(background_fold_down, background_fold_down_pos)
            screen.blit(text_fold_down, textpos_fold_down)
            screen.blit(text_dif_titel, textpos_dif_titel)
            screen.blit(background_starting_start, background_starting_start_pos)
            screen.blit(text_starting_start, textpos_starting_start)
            screen.blit(text_starting_start, textpos_starting_start)
            screen.blit(background_starting_info, background_starting_info_pos)
            screen.blit(text_starting_info, textpos_starting_info)

            

            if fold_poker == True:
                hover_logic(background_fold_down1_pos, background_fold_down1, "lightgray", "white")
                hover_logic(background_fold_down2_pos, background_fold_down2, "lightgray", "white")
                screen.blit(background_fold_down1, background_fold_down1_pos)
                screen.blit(background_fold_down2, background_fold_down2_pos)
                screen.blit(text_fold_down11, textpos_fold_down11)
                screen.blit(text_fold_down22, textpos_fold_down22)

                if click(background_fold_down1_pos):
                    fold_poker = False
                    mode = "Utan stege"

                if click(background_fold_down2_pos):
                    fold_poker = False
                    mode = "Med stege"

                

            pg.display.update()

        elif start == "poker" and singleplayer == False:
            hover_logic(background_starting_exit_pos, background_starting_exit, "lightgray", "white")

            if click(background_starting_exit_pos) == True:
                print("Exit")
                start = "menu"

            screen.blit(background_menu, (0, 0))
            screen.blit(background_starting, background_starting_pos)
            screen.blit(background_starting_exit, background_starting_exit_pos)
            screen.blit(text_starting_exit, textpos_starting_exit)
            screen.blit(text_starting_poker_titel, textpos_starting_poker_titel)

            screen.blit(text_starting_multi_development, textpos_starting_multi_development)

            pg.display.update()

        elif start == "vänd10" and singleplayer == False:
            hover_logic(background_starting_exit_pos, background_starting_exit, "lightgray", "white")

            if click(background_starting_exit_pos) == True:
                print("Exit")
                start = "menu"

            screen.blit(background_menu, (0, 0))
            screen.blit(background_starting, background_starting_pos)
            screen.blit(background_starting_exit, background_starting_exit_pos)
            screen.blit(text_starting_exit, textpos_starting_exit)
            screen.blit(text_starting_vänd10_titel, textpos_starting_vänd10_titel)

            screen.blit(text_starting_multi_development, textpos_starting_multi_development)

            pg.display.update()

        #frame rate
        clock.tick(60)

if __name__ == '__main__' : main()