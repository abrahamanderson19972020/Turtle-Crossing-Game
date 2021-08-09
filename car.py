from turtle import Turtle
import random

COLORS = ["blue", "green", "yellow", "red", "purple", "coral", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class Cars:
    def __init__(self):
        self.car_list = list()
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.setheading(180)
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
