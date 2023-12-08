from turtle import *
shape("turtle")
speed(200)

m = int(numinput("Drehwinkel","Wie groß soll ihr Drehwinkel sein?"))
for i in range (m):
	fd(100)
	rt(m)
done()