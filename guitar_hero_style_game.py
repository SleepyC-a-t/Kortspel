import pygame as pg
import random
from sys import exit

def main():
    pg.init()
    pg.mixer.init()
    x = 300
    y = 600
    falling = 0
    frame = 120
    falling_speed = y*1.1
    music = 'Audio_Game'
    timer = 220.0
    past_music = None
    volume = 0.2
    score = 0
    max_score = 0
    scoreold = None
    maxi_score = None
    distance = [100, 200, 300, 400, 500, 600]
    final_check = True
    combo = 0
    high_combo = 0

    def button(width: int, height: int, colour: str, placementx: int, placementy: int, alpha=255):
        """width, height, colour, x, y, returns surface and surface pos"""
        background = pg.Surface((width, height), pg.SRCALPHA)
        background.fill((*pg.Color(colour)[:3], alpha))
        background_pos = background.get_rect()
        background_pos.center = (placementx, placementy)

        return background, background_pos
    
    def click(Rect: int):
        """Rect (pos), returns true or false"""
        for event in events:
            if event.type == pg. MOUSEBUTTONDOWN:
                if Rect.collidepoint(mouse_pos):
                    return True
        return False
    
    def fall(Rectpos: int):
        Rectpos.y += falling_speed*dt

    def back(Rectpos: int, height: int, ypos=y):
        if Rectpos.y >= ypos:
            Rectpos.y = height
            return True
        return False

    def hit(Rectpos, secondrectpos, tolerance=40):
        return abs(Rectpos.centery-secondrectpos.centery) <= tolerance
        
    def text(font, fontsize, message, colour, xpos, ypos):
        """font, size, message, colour (x, y, z), x, y, returns text and text pos"""
        message = str(message)
        textfont = pg.font.Font(font, fontsize)
        texti = textfont.render(message, 1, (colour))
        textpos = texti.get_rect()
        textpos.center = (xpos, ypos)
        return texti, textpos
    
    def force(Rectpos, height):
        Rectpos.y = height
        

    background_box, backgroundpos_box = button(x//6, y//24, "black", x//2, falling)
    background = pg.image.load('Background.png')
    background_leftbox, backgroundpos_leftbox = button(x//6, y//24, "black", x//2-x//6-x//20, falling)
    background_rightbox, backgroundpos_rightbox = button(x//6, y//24, "black", x//2+x//6+x//20, falling)
    line1, line1pos = button(x//5, y, "white", x//2, y//2, 128)
    lineleft, lineleftpos = button(x//5, y, "white", x//2-x//6-x//20, y//2, 128)
    lineright, linerightpos = button(x//5, y, "white", x//2+x//6+x//20, y//2, 128)
    scoring, scoringpos = button(x//5, y//60, "dimgray", x//2, y//2+y//3, 230)
    scoringleft, scoringleftpos = button(x//5, y//60, "dimgray", x//2-x//6-x//20, y//2+y//3, 230)
    scoringright, scoringrightpos = button(x//5, y//60, "dimgray", x//2+x//6+x//20, y//2+y//3, 230)
    scroingleft_invis, scoringleftpos_invis = button(x//5, y//16, "dimgray", x//2-x//6-x//20, backgroundpos_leftbox.centery, 0)
    scroingcenter_invis, scoringcenterpos_invis = button(x//5, y//16, "dimgray", x//2, backgroundpos_box.centery, 0)
    scroingright_invis, scoringrightpos_invis = button(x//5, y//16, "dimgray", x//2+x//6+x//20, backgroundpos_rightbox.centery, 0)
    background_end, backgroundpos_end = button(x*0.8, y*0.9, "dimgray", x//2, y//2, 230)
    text_max, textpos_max = text(None, 30, "Max possible score", (10, 10, 10), x//2, y//2*0.2)
    text_actual, textpos_actual = text(None, 30, "Actual score", (10, 10, 10), x//2, y//2*0.4)
    text_highcombo, textpos_highcombo = text(None, 30, "Highest combo", (10, 10, 10), x//2, y*0.3)
    background_box1, backgroundpos_box1 = button(x//6, y//24, "black", x//2, falling)
    background_leftbox1, backgroundpos_leftbox1 = button(x//6, y//24, "black", x//2-x//6-x//20, 0-600)
    background_rightbox1, backgroundpos_rightbox1 = button(x//6, y//24, "black", x//2+x//6+x//20, 0-600)
    text_left, textpos_left = text(None, 30, "D", (10, 10, 10), x//2-x//6-x//20, y//2+y//3)
    text_center, textpos_center = text(None, 30, "F", (10, 10, 10), x//2, y//2+y//3)
    text_right, textpos_right = text(None, 30, "J", (10, 10, 10), x//2+x//6+x//20, y//2+y//3)
    

    MUSIC_END = pg.USEREVENT + 1
    pg.mixer.music.set_endevent(MUSIC_END)

    song_finished = False

    screen = pg.display.set_mode((x,y))
    pg.display.set_caption("Testspel")
    clock = pg.time.Clock()

    while True:
        
        
        mouse_pos = pg.mouse.get_pos()
        events = pg.event.get()
        if music != past_music:
            #pg.mixer.music.fadeout(1)
            past_music = music

            if music == "Audio_Game":
                pg.mixer.music.load("Audio_Game2.mp3")
                pg.mixer.music.set_volume(volume)

            pg.mixer.music.play(0)
        dt = clock.tick(frame) / 1000
        timer -=dt

        if timer != timer+frame:
            time, timepos = text(None, 60, int(timer), (10, 10, 10), x//2, y*0.9)
        
        for event in events:
            if event.type == MUSIC_END:
                song_finished = True
        

        scoringleftpos_invis.center = backgroundpos_leftbox.center
        scoringcenterpos_invis.center = backgroundpos_box.center
        scoringrightpos_invis.center = backgroundpos_rightbox.center
        
        
        
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        if song_finished == False:
            for event in events:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_f:
                        if hit(scoringcenterpos_invis, scoringpos):
                            score+=100
                            max_score+=100
                            combo+=1
                            force(backgroundpos_box, 0-random.choice(distance))
                        else:
                            score-=10
                            combo = 0
            
                    elif event.key == pg.K_d:
                        if hit(scoringleftpos_invis, scoringleftpos):
                            score+=100
                            max_score+=100
                            combo+=1
                            force(backgroundpos_leftbox, 0-random.choice(distance))
                        else:
                            score-=10
                            combo = 0
        
                    elif event.key == pg.K_j:
                        if hit(scoringrightpos_invis, scoringrightpos):
                            score+=100
                            max_score+=100
                            combo+=1
                            force(backgroundpos_rightbox, 0-random.choice(distance))
                        else:
                            score-=10
                            combo = 0
            
            if hit(scoringrightpos_invis, scoringrightpos):
                background_rightbox.fill("green")
            else:
                background_rightbox.fill("black")

            if hit(scoringleftpos_invis, scoringleftpos):
                background_leftbox.fill("green")
            else:
                background_leftbox.fill("black")

            if hit(scoringcenterpos_invis, scoringpos):
                background_box.fill("green")
            else:
                background_box.fill("black")
                        
        if score != scoreold:
            scoreold = score
            scorebox, scoreboxpos = text(None, 60, score, (10, 10, 10), x//2, y//2-y//3-y//8)
            text_currentcombo, textpos_currentcombo = text(None, 60, combo, (10, 10, 10), x//2+x//3+x//15, y//2-y//3-y//8)
        if max_score != maxi_score:
            maxi_score = max_score
            scoremaxbox, scoremaxboxpos = text(None, 60, max_score, (10, 10, 10), x//2, y//2*0.3)
        if song_finished == False:
            fall(backgroundpos_box)
            fall(backgroundpos_leftbox)
            fall(backgroundpos_rightbox)
            if back(backgroundpos_box, 0-random.choice(distance)):
                #score-=1
                max_score+=100
                combo = 0
            if back(backgroundpos_leftbox, 0-random.choice(distance)):
                #score-=1
                max_score+=100
                combo = 0
            if back(backgroundpos_rightbox, 0-random.choice(distance)):
                #score-=1
                max_score+=100
                combo = 0

            if combo > high_combo:
                high_combo = combo
            
            
            
            screen.blit(background, (0,0))
            screen.blit(line1, line1pos)
            screen.blit(lineleft, lineleftpos)
            screen.blit(lineright, linerightpos)
            screen.blit(background_box, backgroundpos_box)
            screen.blit(background_leftbox, backgroundpos_leftbox)
            screen.blit(background_rightbox, backgroundpos_rightbox)
            screen.blit(scoring, scoringpos)
            screen.blit(scoringleft, scoringleftpos)
            screen.blit(scoringright, scoringrightpos)
            screen.blit(scorebox, scoreboxpos)
            screen.blit(scroingleft_invis, scoringleftpos_invis)
            screen.blit(scroingcenter_invis, scoringcenterpos_invis)
            screen.blit(scroingright_invis, scoringrightpos_invis)
            screen.blit(text_currentcombo, textpos_currentcombo)
            screen.blit(time, timepos)
            screen.blit(text_left, textpos_left)
            screen.blit(text_center, textpos_center)
            screen.blit(text_right, textpos_right)

            pg.display.update()
        elif song_finished == True:

            if final_check == True and score !=0:
                grade = score/max_score
                if grade == 1:
                    final_grade = "S+"
                elif grade >= 0.95:
                    final_grade = "S"
                elif grade >= 0.85:
                    final_grade = "A"
                elif grade >= 0.75:
                    final_grade = "B"
                elif grade >= 0.65:
                    final_grade = "C"
                elif grade >= 0.55:
                    final_grade = "D"
                elif grade >= 0.45:
                    final_grade = "E"
                elif grade >= 0.35:
                    final_grade = "F"
                else:
                    final_grade = "F-"
                final_check = False
                gradefinal, gradefinalpos = text(None, 60, final_grade, (10, 10, 10), x//2, y//2)
                scoreboxpos, scoreboxpos = text(None, 60, score, (10, 10, 10), x//2, y*0.25)
                textcombo, textcombopos = text(None, 60, high_combo, (10, 10, 10), x//2, y*0.35)
            elif score <= 0:
                final_check = False
                final_grade = "F-----"
                gradefinal, gradefinalpos = text(None, 60, final_grade, (10, 10, 10), x//2, y//2)
                scoreboxpos, scoreboxpos = text(None, 60, score, (10, 10, 10), x//2, y*0.25)
                textcombo, textcombopos = text(None, 60, high_combo, (10, 10, 10), x//2, y*0.35)

            screen.blit(background, (0,0))
            screen.blit(background_end, backgroundpos_end)
            screen.blit(scoremaxbox, scoremaxboxpos)
            screen.blit(text_max, textpos_max)
            screen.blit(scorebox, scoreboxpos)
            screen.blit(text_actual, textpos_actual)
            screen.blit(gradefinal, gradefinalpos)
            screen.blit(textcombo, textcombopos)
            screen.blit(text_highcombo, textpos_highcombo)

            pg.display.update()

if __name__ == '__main__' : main()