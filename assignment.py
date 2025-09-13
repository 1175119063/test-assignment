import turtle

def draw_circle_center(t, center, r, fill_color, outline_color=(0, 0, 0)):
    t.penup()
    t.goto(center[0], center[1] - r)  
    t.setheading(0)
    t.pendown()
    t.color(outline_color, fill_color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    turtle.colormode(255)  # 使用 0-255 的 RGB

    # 底部鞋子（放在最前以确保覆盖层次合适）
    draw_circle_center(t, (-50, -150), 28, (210, 0, 0), (0, 0, 0))  # 左鞋
    draw_circle_center(t, (50, -150), 28, (210, 0, 0), (0, 0, 0))   # 右鞋

    # 身体主体（粉色圆形）
    draw_circle_center(t, (0, 0), 100, (255, 105, 180), (0, 0, 0))

    # 手臂（简单圆形，粉色）
    draw_circle_center(t, (-120, -40), 22, (255, 105, 180), (0, 0, 0))
    draw_circle_center(t, (120, -40), 22, (255, 105, 180), (0, 0, 0))

    # 眼睛（两只白色圆形）
    draw_circle_center(t, (-28, 28), 12, (255, 255, 255), (0, 0, 0))
    draw_circle_center(t, (28, 28), 12, (255, 255, 255), (0, 0, 0))

    # 瞳孔
    draw_circle_center(t, (-28, 32), 5, (0, 0, 0), (0, 0, 0))
    draw_circle_center(t, (28, 32), 5, (0, 0, 0), (0, 0, 0))

    # 面颊（腮红）
    draw_circle_center(t, (-45, 2), 10, (255, 180, 200), (0, 0, 0))
    draw_circle_center(t, (45, 2), 10, (255, 180, 200), (0, 0, 0))

    # 嘴巴（简单弧线）
    t.penup()
    t.goto(-8, 5)
    t.setheading(-60)
    t.pendown()
    t.width(3)
    t.color((0, 0, 0))
    t.circle(16, 120)
    t.width(1)

    turtle.done()

if __name__ == "__main__":
    main()
