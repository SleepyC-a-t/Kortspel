import pygame as pg
from sys import exit
import random as rn
import math

def main():
    pg.init()
    pg.mixer.init()
    #screen width
    x = 1250
    #screen height
    y = 600
    screen = pg.display.set_mode((x,y))
    mode = "battle"
    frame_rate = 60
    momentum1 = 0
    momentum2 = 0
    hp1 = 100
    hp1_past = 99
    hp2 = 100
    hp2_past = 99
    sidemomentum1 = -1
    sidemomentum2 = 1
    radius = 25
    timer = 0
    parry = False
    starting_positions = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    starting_height = [75, 85, 95, 105, 115, 125, 135, 145]
    starting_height2 = [80, 90, 100, 110, 120, 130, 140, 150]
    parry_height = [5, 10, 15, 20, 25]
    angle = 0
    orbit_damage = 0.1
    pg.display.set_caption('Battle Balls')
    orbit_di = True

    def button(width:int, height:int, colour:str, placementx:int, placementy:int):
        """width, height, colour, x, y, returns surface and surface pos"""
        background = pg.Surface((width, height))
        background.fill(colour)
        background_pos = background.get_rect()
        background_pos.center = (placementx, placementy)

        return background, background_pos
    
    def create_circle(radius, colour, xpos, ypos):
        size = radius * 2

        surface = pg.Surface((size, size), pg.SRCALPHA)
        pg.draw.circle(surface, colour, (radius, radius), radius)

        rect = surface.get_rect(center=(xpos, ypos))

        return surface, rect
    
    def hit(Rectpos, secondrectpos, tolerance=radius*2):
        return abs(Rectpos.centery-secondrectpos.centery) <= tolerance
    
    def collision(Rectpos, secondrectpos):
        if Rectpos.colliderect(secondrectpos):
            return True
        else:
            return False
        
    def text(font:str, fontsize:int, message:str, colour:str, xpos:int, ypos:int):
        """font, size, message, colour (x, y, z), x, y, returns text and text pos"""
        message = str(message)
        textfont = pg.font.Font(font, fontsize)
        texti = textfont.render(message, 1, (colour))
        textpos = texti.get_rect()
        textpos.center = (xpos, ypos)
        return texti, textpos
    
    def orbit(planet, point_of_orbit_x:int, point_of_orbit_y:int, distance_maintain:int, angle, speed, clockwise=True):
        """rect_pos, orbit around (x, y), radius, starting_angle, speed of orbit"""
        if clockwise == True:
            angle+=speed
        else:
            angle-=speed

        planet.centerx = point_of_orbit_x + math.cos(angle) * distance_maintain
        planet.centery = point_of_orbit_y + math.sin(angle) * distance_maintain

        

        return angle


    background, backgroundpos = button(x, y, "white", x//2, y//2)
    wall_left, wallpos_left = button(10, 410, "black", x//2-200, y//2)
    wall_right, wallpos_right = button(10, 410, "black", x//2+200, y//2)
    wall_top, wallpos_top = button(410, 10, "black", x//2, y//2-200)
    wall_bottom, wallpos_bottom = button(410, 10, "black", x//2, y//2+200)

    blue_win, blue_win_pos = text(None, 64, "Blue won", (10, 10, 10), x//2, y//2)
    red_win, red_win_pos = text(None, 64, "Red won", (10, 10, 10), x//2, y//2)
    

    ball, ballpos = create_circle(radius, (10, 10, 150), x//2-30-rn.choice(starting_positions), y//2-rn.choice(starting_height))
    ball2, ball2pos = create_circle(radius, (200, 10, 10), x//2+30+rn.choice(starting_positions), y//2-rn.choice(starting_height2))

    orbiter, orbiter_pos = create_circle(16, (200,10,10), ball2pos.x+20, ball2pos.y)

    blue, blue_pos = text(None, 48, "Blue", (10, 10, 10), x//2-500, y//2-250)

        
    clock = pg.time.Clock()

    while True:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        if mode == "battle":

            
            if hp1 != hp1_past:
                health1, health1pos = text(None, 48, round(hp1), (10, 10, 10), x//2-500, y//2-200)
                hp1_past = hp1

            if hp2 != hp2_past:
                health2, health2pos = text(None, 48, hp2, (10, 10, 10), x//2+500, y//2-250)
                hp2_past = hp2

            momentum1 += frame_rate/(frame_rate*6)
            
            ballpos.y +=momentum1

            if collision(ballpos, wallpos_bottom):
                ballpos.bottom = wallpos_bottom.top
                momentum1 -= momentum1*2.1

            ballpos.x +=sidemomentum1

            if collision(ballpos, wallpos_left):
                ballpos.left = wallpos_left.right+1
                sidemomentum1 -= sidemomentum1*2.1

            if collision(ballpos, wallpos_right):
                ballpos.right = wallpos_right.left+1
                sidemomentum1 -= sidemomentum1*2.1

            if collision(ballpos, wallpos_top):
                ballpos.top = wallpos_top.bottom
                momentum1 -= momentum1*2

            momentum2 += frame_rate/(frame_rate*6)

            ball2pos.y +=momentum2
                
            if collision(ball2pos, wallpos_bottom):
                ball2pos.bottom = wallpos_bottom.top
                momentum2 -= momentum2*2.1

            ball2pos.x +=sidemomentum2

            if collision(ball2pos, wallpos_left):
                ball2pos.left = wallpos_left.right+1
                sidemomentum2 -= sidemomentum2*2.1

            if collision(ball2pos, wallpos_right):
                ball2pos.right = wallpos_right.left+1
                sidemomentum2 -= sidemomentum2*2.1

            if collision(ball2pos, wallpos_top):
                ball2pos.top = wallpos_top.bottom
                momentum2 -= momentum2*2

            

            
            dx = ball2pos.centerx - ballpos.centerx
            dy = ball2pos.centery - ballpos.centery

            distance = (dx**2 + dy**2) ** 0.5

            if distance <= radius * 2:

                nx = dx / distance
                ny = dy / distance

                sidemomentum1 = -nx * 4
                momentum1 = -ny * 4

                sidemomentum2 = nx * 4
                momentum2 = ny * 4

            if timer >= 0 and timer < frame_rate*0.5:
                sword1, swordpos1 = button(10, 100, "gray", ballpos.centerx, ballpos.centery-70)
                #sword2, swordpos2 = button(10, 100, "gray", ball2pos.centerx, ball2pos.centery-70)
            elif timer > frame_rate*0.5 and timer < frame_rate:
                sword1, swordpos1 = button(100, 10, "gray", ballpos.centerx+70, ballpos.centery)
                #sword2, swordpos2 = button(100, 10, "gray", ball2pos.centerx-70, ball2pos.centery)
            elif timer > frame_rate and timer < frame_rate*1.5:
                sword1, swordpos1 = button(10, 100, "gray", ballpos.centerx, ballpos.centery+70)
                #sword2, swordpos2 = button(10, 100, "gray", ball2pos.centerx, ball2pos.centery+70)
            elif timer > frame_rate*1.5 and timer < frame_rate*2:
                sword1, swordpos1 = button(100, 10, "gray", ballpos.centerx-70, ballpos.centery)
                #sword2, swordpos2 = button(100, 10, "gray", ball2pos.centerx+70, ball2pos.centery)
            elif timer > frame_rate*2:
                timer = 0
                
            #if collision(swordpos1, swordpos2):
            #    parry = True
            #    momentum1+=rn.choice(parry_height)
            #    momentum2+=rn.choice(parry_height)
            #else:
            #    parry = False

            if collision(orbiter_pos, swordpos1):
                parry = True
                
                if orbit_di == True:
                    orbit_di = False
                else:
                    orbit_di = True

            else:
                parry = False

            if parry == False:
                if collision(swordpos1, ball2pos):
                    hp2-=1
                    if sidemomentum2<0:
                        sidemomentum2-=1
                    
                        

                    else:
                        sidemomentum2+=1

                    if momentum2 < 0:
                        momentum2+=3

                    else:
                        momentum2-=3

                #if collision(swordpos2, ballpos):
                #    hp1-=1
                #    if sidemomentum1<0:
                #        sidemomentum1-=1

                #    else:
                #        sidemomentum1+=1

                #    if momentum1 < 0:
                #        momentum1+=3

                #    else:
                #        momentum1-=3

                if collision(orbiter_pos, ballpos):
                    hp1-=orbit_damage
                    orbit_damage+=0.025

            

            angle = orbit(orbiter_pos, ball2pos.centerx, ball2pos.centery, 60, angle, 0.1, orbit_di)

            

            if momentum1 <= 0.5 and collision(ballpos, wallpos_bottom):
                momentum1 -= (momentum1+3)*2

            if momentum2 <= 0.5 and collision(ball2pos, wallpos_bottom):
                momentum2 -= (momentum2+3)*2

            if sidemomentum1<0 and sidemomentum1>-1:
                sidemomentum1-=2
            elif sidemomentum1>0 and sidemomentum1<1:
                sidemomentum1+=2

            

            screen.blit(background, backgroundpos)
            screen.blit(wall_left, wallpos_left)
            screen.blit(wall_right, wallpos_right)
            screen.blit(wall_top, wallpos_top)
            screen.blit(wall_bottom, wallpos_bottom)
            if hp1>0:
                screen.blit(ball, ballpos)
                screen.blit(sword1, swordpos1)

            if hp2>0:
                screen.blit(ball2, ball2pos)
                #screen.blit(sword2, swordpos2)
                screen.blit(orbiter, orbiter_pos)
            
            screen.blit(health1, health1pos)
            screen.blit(health2, health2pos)
            screen.blit(blue, blue_pos)
            

            timer+=1

            if hp1<1 or hp2<1:
                mode = "victory"
                hp1_past = 100
                hp2_past = 100

            pg.display.update()

        if mode == "victory":
            if hp1 != hp1_past:
                health1, health1pos = text(None, 48, round(hp1), (10, 10, 10), x//2-500, y//2-200)
                hp1_past = hp1
            if hp2 != hp2_past:
                health2, health2pos = text(None, 48, hp2, (10, 10, 10), x//2+500, y//2-250)
                hp2_past = hp2
            if hp1>hp2:
                screen.blit(blue_win, blue_win_pos)
            elif hp2>hp1:
                screen.blit(red_win, red_win_pos)

            pg.display.update()
        
        clock.tick(frame_rate)

if __name__ == "__main__":
    main()