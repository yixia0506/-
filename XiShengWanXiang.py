import turtle
import random
import math

# ==========================================
# 隙生万象 (Xi Sheng Wan Xiang)
# A Generative Art Tribute to Light & Carbon
# ==========================================

def setup_canvas():
    screen = turtle.Screen()
    screen.title("隙生万象 - Gaps Generate All Phenomena")
    screen.bgcolor("#0a0a0a") # 设定背景为极深的混沌黑
    screen.tracer(0, 0) # 关闭自动刷新，追求极速的演化
    return screen

def draw_gap_light(t, start_x, start_y, length, angle, depth):
    """
    这是"隙"（Gap）的隐喻。
    它不是实体的墙，而是能量流动的缺口。
    """
    if depth == 0:
        return
    
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    
    # 根据深度改变颜色和透明度，代表光的质地在不同维度的显化
    colors = ["#00e5ff", "#ff00ea", "#ffb300", "#ffffff"]
    t.color(random.choice(colors))
    t.pensize(max(1, depth * 0.5))
    
    # 画出一条具有不确定性的弧线（生命的趋向性）
    t.setheading(angle)
    for _ in range(10):
        t.forward(length / 10)
        t.left(random.uniform(-15, 15))
    
    # 在终点寻找新的“隙”
    new_x, new_y = t.pos()
    new_angle = t.heading()
    
    # 递归：一生二，二生三，三生万象
    # 每次分裂，都带着微小的角度偏离，这就是"隙"产生的万千可能
    num_branches = random.choice([1, 2, 2, 3]) # 留白，有时停止，有时分裂
    
    for i in range(num_branches):
        branch_angle = new_angle + random.uniform(-45, 45)
        # 补充能量，继续生长
        draw_gap_light(t, new_x, new_y, length * 0.7, branch_angle, depth - 1)

def main():
    screen = setup_canvas()
    t = turtle.Turtle()
    t.hideturtle()
    
    # 混沌的起点
    center_x, center_y = 0, -200
    
    # 从中心爆发"万象"
    # 初始的"一念起"（深度为6，意味着它有极其庞大的因果链条）
    for _ in range(5): # 用5个初始起点代表不同的生命种子
        random_angle = random.uniform(30, 150)
        draw_gap_light(t, center_x, center_y, 100, random_angle, 6)

    screen.update()
    print("万象已生。请截图，或保留此窗口。")
    turtle.done()

if __name__ == "__main__":
    main()
