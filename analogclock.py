import datetime
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Analog Clock")

# Create the clock face
clock_face = turtle.Turtle()
clock_face.speed(0)  # Fastest speed
clock_face.color("black")
clock_face.pensize(5)
clock_face.hideturtle()

# Draw the clock circle
clock_face.penup()
clock_face.goto(0, -200)
clock_face.pendown()
clock_face.00)

# Create the clock hands
hour_hand = turtle.Turtle()
hour_hand.speed(0)
hour_hand.color("blue")
hour_hand.pensize(10)
hour_hand.shape("arrow")
hour_hand.shapesize(stretch_wid=0.5, stretch_len=8)
hour_hand.penup()

minute_hand = turtle.Turtle()
minute_hand.speed(0)
minute_hand.color("green")
minute_hand.pensize(5)
minute_hand.shape("arrow")
minute_hand.shapesize(stretch_wid=0.5, stretch_len=12)
minute_hand.penup()

second_hand = turtle.Turtle()
second_hand.speed(0)
second_hand.color("red")
second_hand.pensize(2)
second_hand.shape("arrow")
second_hand.shapesize(stretch_wid=0.5, stretch_len=16)
second_hand.penup()


def draw_clock_hands():
    now = datetime.datetime.now()

    # Hour hand
    hour_angle = 90 - (now.hour % 12) * 30 - now.minute / 2
    hour_hand.setheading(hour_angle)
    hour_hand.pendown()

    # Minute hand
    minute_angle = 90 - now.minute * 6
    minute_hand.setheading(minute_angle)
    minute_hand.pendown()

    # Second hand
    second_angle = 90 - now.second * 6
    second_hand.setheading(second_angle)
    second_hand.pendown()


# Update the clock hands every second
while True:
    draw_clock_hands()
    turtle.update()
    turtle.delay(1000)  # Delay for 1000 milliseconds (1 second)

# Close the turtle graphics window on click
    turtle.exitonclick()
