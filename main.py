import turtle

wn = turtle.Screen()
wn.title("")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# Grass
Grass = turtle.Turtle()
Grass.speed(0)
Grass.shape("square")
Grass.color("green")
Grass.shapesize(stretch_wid=8, stretch_len=80)
Grass.penup()
Grass.goto(-50, -211)

# Sun
Sun = turtle.Turtle()
Sun.speed(0)
Sun.shape("circle")
Sun.color("yellow")
Sun.shapesize(stretch_wid=5, stretch_len=7)
Sun.penup()
Sun.goto(-75, 200)

# Cloud
Cloud = turtle.Turtle()
Cloud.speed(0)
Cloud.shape("circle")
Cloud.color("white")
Cloud.shapesize(stretch_wid=2, stretch_len=4)
Cloud.penup()
Cloud.goto(150, 200)

# Cloud 2
Cloud_2 = turtle.Turtle()
Cloud_2.speed(0)
Cloud_2.shape("circle")
Cloud_2.color("white")
Cloud_2.shapesize(stretch_wid=2, stretch_len=4)
Cloud_2.penup()
Cloud_2.goto(175, 200)

# Cloud 3
Cloud_3 = turtle.Turtle()
Cloud_3.speed(0)
Cloud_3.shape("circle")
Cloud_3.color("white")
Cloud_3.shapesize(stretch_wid=2, stretch_len=4)
Cloud_3.penup()
Cloud_3.goto(200, 200)

# Cloud 4
Cloud_4 = turtle.Turtle()
Cloud_4.speed(0)
Cloud_4.shape("circle")
Cloud_4.color("white")
Cloud_4.shapesize(stretch_wid=2, stretch_len=4)
Cloud_4.penup()
Cloud_4.goto(-350, 200)

# Cloud 5
Cloud = turtle.Turtle()
Cloud.speed(0)
Cloud.shape("circle")
Cloud.color("white")
Cloud.shapesize(stretch_wid=2, stretch_len=4)
Cloud.penup()
Cloud.goto(-325, 200)

# Cloud 5
Cloud = turtle.Turtle()
Cloud.speed(0)
Cloud.shape("circle")
Cloud.color("white")
Cloud.shapesize(stretch_wid=2, stretch_len=4)
Cloud.penup()
Cloud.goto(-300, 200)
 



while True:
    wn.update()

