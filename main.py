from turtle import Screen
from player import Player
from car import Cars
from level import Level
import random
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.tracer(0)
player_turtle = Player()
car_manager = Cars()
score = Scoreboard()
player_level = Level()
screen.listen()
screen.onkey(fun=player_turtle.up, key="Up", )
screen.onkey(fun=player_turtle.down, key="Down")
screen.onkey(fun=player_turtle.go_right, key="Right", )
screen.onkey(fun=player_turtle.go_left, key="Left")



is_game_on = True
while is_game_on:
    time.sleep(0.3)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car_i in car_manager.car_list:
        if player_turtle.distance(car_i) < 20:
            is_game_on = False
            player_turtle.game_over()
            player_turtle.goto(0, 0)
            screen.addshape("game_over.gif")
            screen.bgpic("game_over.gif")
            #screen.mainloop()


    if player_turtle.ycor() > 280:
        score.increase_score()
        score.update_scoreboard()
        player_turtle.goto(0, -280)
        if score.score == 3 :
            car_manager.increase_speed()
            player_level.increase_level()

        if score.score == 6:
            car_manager.increase_speed()
            player_level.increase_level()
        if score.score == 9:
            car_manager.increase_speed()
            player_level.increase_level()

screen.exitonclick()