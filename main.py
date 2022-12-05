# step 0: Initial setup
from turtle import Screen, Turtle
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Feed the snake!')

# step 1: Create a snake body
# each turtle is 20 pixels tall x 20 pixels wide
# we will use 3 turtles side by side to form a snake
# challenge 1: design a snake with 3x turtles
snakelist = []
initx = 0
inity = 0
xcoor = initx
ycoor = inity
following_distance = 21
# for i in range(0, 3):
#     t = Turtle(shape='square')
#     t.shapesize(1, 1, 1)
#     t.color('white')
#     t.goto(xcoor, ycoor)
#     xcoor -= following_distance
#     snakelist.append(t)
# print(snakelist)

# instead, we could store the positions in a list of tuples and use
# them to draw our snake pieces
initx = 0
inity = 0
# starting_positions = [(initx, inity), (initx - (following_distance) * 1, inity), (initx - (following_distance) * 2)]
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(position)


screen.exitonclick()