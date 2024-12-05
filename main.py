import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score= Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.uup, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.update()
    cars.create_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player) < 23.7:
            game_is_on = False


    if player.ycor()> 280:
        player.finish()
        cars.level_up()
        score.win()



screen.exitonclick()
