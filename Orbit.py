#this code will attempt to simulate how objects of different mass affect eachother, starting with 2 objects in a 2d space
#this project will focus on the 2d plane due to the technical limitations of the pygame module, since it's designed to handle 2d, not 3d
import pygame as pg
import math
from sys import exit

def main():
    pg.init()
    pg.mixer.init()
    #screen width
    x = 1200
    #screen height
    y = 1200
    screen = pg.display.set_mode((x,y))
    #frame rate
    frame = 1
    clock = pg.time.Clock()
    pg.display.set_caption("Gravity_Simulation")
    mode = "sim"
    angle1 = 0
    angle2 = 0

    def create_circle(radius:int, colour, xpos:int, ypos:int):
        size = radius * 2

        surface = pg.Surface((size, size), pg.SRCALPHA)
        pg.draw.circle(surface, colour, (radius, radius), radius)

        rect = surface.get_rect(center=(xpos, ypos))

        return surface, rect
    
    def create_square(width:int, height:int, colour:str, placementx:int, placementy:int):
        """width, height, colour, x, y, returns surface and surface pos"""
        background = pg.Surface((width, height))
        background.fill(colour)
        background_pos = background.get_rect()
        background_pos.center = (placementx, placementy)

        return background, background_pos
    
    def click(surface:int):
        """surface (pos), returns true or false"""
        for event in events:
            if event.type == pg. MOUSEBUTTONDOWN:
                if surface.collidepoint(mouse_pos):
                    return True
        return False
    
    def object_distance(rect1_pos, rect2_pos):
        """first object, second object"""
        x1value = rect1_pos.x
        y1value = rect1_pos.y
        x2value = rect2_pos.x
        y2value = rect2_pos.y
        distans = math.sqrt(((x2value-x1value)**2)+((y2value-y1value)**2))
        return distans
    
    def orbit(planet, point_of_orbit_x:int, point_of_orbit_y:int, distance_maintain:int, angle, speed, clockwise=True):
        """rect_pos, orbit around (x, y), radius, starting_angle, speed of orbit"""
        if clockwise == True:
            angle+=speed
        else:
            angle-=speed

        planet.centerx = point_of_orbit_x + math.cos(angle) * distance_maintain
        planet.centery = point_of_orbit_y + math.sin(angle) * distance_maintain

        

        return angle

    background_rect, background_rect_pos = create_square(x, y, "dimgray", x//2, y//2)

    body_1, body_1_pos = create_circle(10, (10, 10, 10), x//2-20, y//2)
    body_2, body_2_pos = create_circle(10, (10, 10, 10), x//2+20, y//2)

    button_calc, button_calc_pos = create_square(x//8, y//12, "lightgray", x//2, y//2+y//3+x//9)

    while True:

        events = pg.event.get()
        mouse_pos = pg.mouse.get_pos()

        


        if mode == "sim":

            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            if click(button_calc_pos):
                distance = object_distance(body_1_pos, body_2_pos)
                print(distance)

            angle1 = orbit(body_2_pos, body_1_pos.centerx, body_1_pos.centery, 40, angle1, 0.001)
            angle2 = orbit(body_1_pos, body_2_pos.centerx, body_2_pos.centery, 40, angle2, 0.001, False)

            screen.blit(background_rect, background_rect_pos)
            screen.blit(body_1, body_1_pos)
            screen.blit(body_2, body_2_pos)
            screen.blit(button_calc, button_calc_pos)

            pg.display.update()

        clock.tick(frame)

if __name__ == "__main__":
    main()