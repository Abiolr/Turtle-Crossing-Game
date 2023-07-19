import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# making the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating a Player object called player
player = Player()

# creating a CarManger object called car_manager
car_manager = CarManager()

# creating a Scoreboard object called scoreboard
scoreboard = Scoreboard()

# telling the screen to listen for specific keys (Up key)
screen.listen()
screen.onkey(player.go_up, "Up") # go_up function created in player class

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # calling two functions from the CarManager class
    car_manager.create_cars()
    car_manager.move_cars()

    # detecting collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detecting successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    
screen.exitonclick()