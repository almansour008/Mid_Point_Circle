import turtle

# تعريف الدالة التي ترسم الدائرة
def drawCircle(xc,yc,radius):
    # إعداد النافذة للرسم
    window = turtle.Screen()
    window.title("Midpoint Circle Algorithm1")
    pen = turtle.Turtle()
    pen.color("red")
    pen.speed(10)

    # حساب نقط الدائرة باستخدام خوارزمية نقطة المنتصف
    x = 0
    y = radius
    p = 1 - radius

    # الرسم باستخدام خوارزمية نقطة المنتصف
    while x <= y:
        pen.penup()
        pen.goto(xc + x, yc + y)
        pen.pendown()
        pen.color("blue")
        pen.dot()
        pen.penup()
        pen.goto(xc - x, yc + y)
        pen.pendown()
        pen.color("green")
        pen.dot()
        pen.penup()
        pen.goto(xc + x, yc - y)
        pen.pendown()
        pen.color("red")
        pen.dot()
        pen.penup()
        pen.goto(xc - x, yc - y)
        pen.pendown()
        pen.color("pink")
        pen.dot()
        pen.penup()
        pen.goto(xc + y, yc + x)
        pen.pendown()
        pen.color("red")
        pen.dot()
        pen.penup()
        pen.goto(xc - y, yc + x)
        pen.pendown()
        pen.color("blue")
        pen.dot()
        pen.penup()
        pen.goto(xc + y, yc - x)
        pen.pendown()
        pen.color("yellow")
        pen.dot()
        pen.penup()
        pen.goto(xc - y, yc - x)
        pen.color("black")
        pen.pendown()
        pen.dot()

        if p < 0:
            p += 2 * x + 3
        else:
            p += 2 * (x - y) + 5
            y -= 1
        x += 1

    turtle.done()

# استدعاء الدالة لرسم الدائرة

#==========================================
0

import matplotlib.pyplot as plt

def drawCircle1(center_x, center_y, radius):
    # قائمة لتخزين النقاط التي تشكل الدائرة
    points = []

    x = 0
    y = radius
    p = 1 - radius

    # حساب النقاط التي تشكل الدائرة باستخدام خوارزمية نقطة المنتصف
    while x <= y:
        points.append((x + center_x, y + center_y))
        points.append((-x + center_x, y + center_y))
        points.append((x + center_x, -y + center_y))
        points.append((-x + center_x, -y + center_y))
        points.append((y + center_x, x + center_y))
        points.append((-y + center_x, x + center_y))
        points.append((y + center_x, -x + center_y))
        points.append((-y + center_x, -x + center_y))

        if p < 0:
            p += 2 * x + 3
        else:
            p += 2 * (x - y) + 5
            y -= 1
        x += 1

    # رسم النقاط على الرسم البياني
    for point in points:
        plt.scatter(*point, color='black')

    # ضبط محور الإحداثيات ليكون متساوي الطول
    plt.axis('equal')
    plt.title("Midpoint Circle Algorithm`1")
    plt.show()

# تعيين مركز الدائرة ونصف القطر
x = int(input("Enter center x coordinate: "))
y = int(input("Enter center y coordinate: "))
radius = int(input("Enter radius: "))

drawCircle1(x, y, radius)
drawCircle(x,y,radius)



