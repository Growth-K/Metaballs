import pygame
import random
import class_object as co

def main():
    pygame.init()
    X = 1200
    Y = 600
    black = (0,0,0)
    white = (255,255,255)
    green = (0,255,0)
    red = (255,0,0)
    screen = pygame.display.set_mode([X, Y])
    pygame.display.set_caption('Hand Tracking Game')
    running = True
    screen.fill(black)
    # heart equation: x2+(5y4−|x|−−√)2=1.
    step = 15
    radius = 100
    circle_arr = []
    
    for x in range(6):
        pos_x = random.randint(radius, X - radius)
        pos_y = random.randint(radius, Y - radius)
        speed_x = random.randint(1, 15)
        speed_y = random.randint(1, 15)
        radius = random.randint(20,60)
        circle_arr.append(co.circle(pos_x, pos_y, speed_x, speed_y, radius))
    while running:
        #draw_grid(screen, X, Y, step)
        for circles in circle_arr:
            circles.x += circles.speed_x
            circles.y += circles.speed_y
            if(circles.x + circles.radius >= X or circles.x - circles.radius <= 0):
                circles.speed_x *= -1
            if(circles.y + circles.radius >= Y or circles.y - circles.radius <= 0):
                circles.speed_y *= -1
        point_array = []
        for i in range(0, X, step):
            point_array.append([])
            for j in range(0, Y, step):
                x = i
                y = j
                #point_1 = ((x + pos_x) ** 2) + (((y + pos_y) * -1) - ((x + pos_x) ** 2) ** 0.33) ** 2 - size
                point_1 = -1
                for circle in circle_arr:
                    point_1 += circle.get_radius_by_dist(x, y)
                point_array[len(point_array) - 1].append([point_1,x,y])
                
        R = 0
        G = 200
        B = 100
        for row in range(len(point_array) - 1):
            for column in range(len(point_array[0]) - 1):
                point_1 = point_array[row][column][0]
                point_2 = point_array[row + 1][column][0]
                #print(len(point_array), point_array[row + 1])
                point_3 = point_array[row][column + 1][0]
                point_4 = point_array[row + 1][column + 1][0]
                # pygame.draw.circle(screen, green, (point_array[row][column][1], point_array[row][column][2]), 2)
                # pygame.draw.circle(screen, red, (point_array[row + 1][column][1], point_array[row + 1][column][2]), 2)
                # pygame.draw.circle(screen, white, (point_array[row][column + 1][1], point_array[row][column + 1][2]), 2)
                # pygame.draw.circle(screen, (0,0,255), (point_array[row + 1][column + 1][1], point_array[row + 1][column + 1][2]), 2)
                x = point_array[row][column][1]
                y = point_array[row][column][2]
                if(point_1 >= 0 and point_2 >= 0 and point_3 >= 0 and point_4 >= 0):
                    pass
                    #pygame.draw.rect(screen, red, pygame.Rect(x, y, step, step))
                elif(point_1 < 0 and point_2 < 0 and point_3 < 0 and point_4 < 0):
                    pass

                elif(point_2 != point_1 and point_4 != point_3 and point_3 != point_1 and point_4 != point_2):
                    point_1 += 1
                    point_2 += 1
                    point_3 += 1
                    point_4 += 1
                    x_edge_1 = x + ((1 - point_1)) / (point_2 - point_1) * step
                    x_edge_2 = x + ((1 - point_3)) / (point_4 - point_3) * step
                    y_edge_1 = y + ((1 - point_1)) / (point_3 - point_1) * step
                    y_edge_2 = y + ((1 - point_2)) / (point_4 - point_2) * step
                    point_1 -= 1
                    point_2 -= 1
                    point_3 -= 1
                    point_4 -= 1
                    #print(x, y, point_1, point_2, ((1 - point_1) / (point_2 - point_1)) * (step), x_edge_1)
                    # pygame.draw.circle(screen, green, (x_edge_1, y), 2)
                    # pygame.draw.circle(screen, green, (x_edge_2, y), 2)
                    # pygame.draw.circle(screen, green, (x, y_edge_1), 2)
                    # pygame.draw.circle(screen, green, (x, y_edge_2), 2)
                    G += 2
                    R += 2
                    B += 2
                    if(G > 255): G = 0
                    if(R > 255): R = 0
                    if(B > 255): B = 0

                    color = (R,G,B)
                    if(point_1 >= 0):
                        if(point_2 >= 0):
                            if(point_3 >= 0):
                                pygame.draw.line(screen, color, (x_edge_2, y + step), (x + step, y_edge_2), 3)
                                #option 11
                            elif(point_4 >= 0):
                                pygame.draw.line(screen, color, (x, y_edge_1), (x_edge_2, y + step), 3)
                                #option 12
                            else:
                                pygame.draw.line(screen, color, (x, y_edge_1), (x + step, y_edge_2), 3)
                                #option 6
                        elif(point_3 >= 0):
                            if(point_4 >= 0):
                                pygame.draw.line(screen, color, (x_edge_1, y), (x + step, y_edge_2), 3)
                                #option 14
                            else:
                                pygame.draw.line(screen, color, (x_edge_1, y), (x_edge_2, y + step), 3)
                                #option 5
                        elif(point_4 >= 0):
                            pygame.draw.line(screen, color, (x_edge_1, y), (x + step, y_edge_2), 3)
                            pygame.draw.line(screen, color, (x, y_edge_1), (x_edge_2, y + step), 3)
                            #option 9
                        else:
                            pygame.draw.line(screen, color, (x, y_edge_1), (x_edge_1, y), 3)
                            #option 1
                    elif(point_2 >= 0):

                        if(point_3 >= 0):
                            if(point_4 >= 0):
                                pygame.draw.line(screen, color, (x, y_edge_1), (x_edge_1, y), 3)
                                pass
                                #option 13
                            else:
                                pygame.draw.line(screen, color, (x, y_edge_1), (x_edge_1, y), 3)
                                pygame.draw.line(screen, color, (x_edge_2, y + step), (x + step, y_edge_2), 3)
                                pass
                                #option 10
                        elif(point_4 >= 0):
                            pygame.draw.line(screen, color, (x_edge_1, y), (x_edge_2, y + step), 3)
                            pass
                            #OPTION 7
                        else:
                            pygame.draw.line(screen, color, (x_edge_1, y), (x + step, y_edge_2), 3)
                            pass 
                            #option 2
                    elif(point_3 >= 0):
                        if(point_4 >= 0):
                            pygame.draw.line(screen, color, (x, y_edge_1), (x + step, y_edge_2), 3)
                            pass
                            #option 8
                        else:
                            pygame.draw.line(screen, color, (x, y_edge_1), (x_edge_2, y + step), 3)
                            pass
                            #option 4
                    else:
                        pygame.draw.line(screen, color, (x_edge_2, y + step), (x + step, y_edge_2),3)
                        pass
                        #option 3
            

        for event in pygame.event.get():
                #close when x is pressed
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    #if q is hit
                    if event.key == pygame.K_q:
                        running = False
        pygame.display.flip()
        screen.fill(black)


def draw_grid(screen, X, Y, step):
    
    for x in range(0, X, step):
        pygame.draw.line(screen, (0,127,0), (x, 0), (x, Y))
    for y in range(0, Y, step):
        pass
        pygame.draw.line(screen, (0,127,0), (0, y), (X, y))




if __name__ == "__main__": main()