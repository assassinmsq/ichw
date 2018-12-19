"""Tile.py: to tile.

__author__ = "Ma Siqi"
__pkuid__  = "1800011760"
__email__  = "1800011760@pku.edu.cn"
"""

from turtle import Turtle

HORIZONTAL = 0
VERTICAL = 1


def draw_line(ttl, x1, y1, x2, y2):
    '''
    draw lines
    Args:
        ttl: turtle
        x1: x-coordinate of starting point
        y1: y-coordinate of starting point
        x2: x-coordinate of end point
        y2: y-coordinate of end point
    '''
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.penup()


def draw_board(ttl, width=50):
    '''
    draw board
    Args:
        ttl: turtle
        width: width of oen tile
    '''
    global W, H
    ttl.color('blue')
    w_bias = W // 2 * width
    h_bias = H // 2 * width
    for j in range(H + 1):
        x, y = -w_bias, j * width - h_bias
        ttl.penup()
        ttl.goto(x, y)
        ttl.pendown()
        ttl.fd(width * W)
    ttl.lt(90)
    for j in range(W + 1):
        y, x = -h_bias, j * width - w_bias
        ttl.penup()
        ttl.goto(x, y)
        ttl.pendown()
        ttl.fd(width * H)
    for i in range(W):
        for j in range(H):
            x, y = width // 2 + i * width - w_bias, width // 2 + j * width - h_bias
            ttl.penup()
            ttl.goto(x, y)
            ttl.pendown()
            ttl.write(i + j * W)  
            

def draw_rectangle(ttl, x1, y1, x2, y2, width=50):
    '''
    draw rectangle
    Args:
        ttl: turtle
        x1: x-coordinate of one corner
        y1: y-coordinate of same corner above
        x2: x-coordinate of opposite corner
        y2: y-coordinate of same corner above
        width: width of one tile        
    '''
    global W, H
    ttl.color('black')
    ttl.pensize(3)
    w_bias = W // 2 * width
    h_bias = H // 2 * width
    draw_line(ttl, x1 * width - w_bias, y1 * width - h_bias, x1 * width - w_bias, y2 * width - h_bias)
    draw_line(ttl, x1 * width - w_bias, y2 * width - h_bias, x2 * width - w_bias, y2 * width - h_bias)
    draw_line(ttl, x2 * width - w_bias, y2 * width - h_bias, x2 * width - w_bias, y1 * width - h_bias)
    draw_line(ttl, x2 * width - w_bias, y1 * width - h_bias, x1 * width - w_bias, y1 * width - h_bias)
    

def draw_solution(ttl, sol):
    '''
    draw solutions
    Args:
        ttl: turtle
        sol: solution
    '''
    global w, h, W, H
    for x1, y1, direction in sol:
        if direction == HORIZONTAL:
            x2 = x1 + w
            y2 = y1 - h
        else:
            x2 = x1 + h
            y2 = y1 - w
        draw_rectangle(ttl, x1, y1, x2, y2)
        

def solve(heights, history, res):
    '''
    solution starting from the upper left corner.
    Args:
        heights: heights of the blank tiles.
        history: tiles put so far.
        res: the list to store the solutions.
    '''
    if all(x == 0 for x in heights):
        res.append(history)
    max_height = max_ind = -1
    for i, x in enumerate(heights):
        if x > max_height:
            max_height, max_ind = x, i
    # put the tile horizontally
    if max_ind + w <= len(heights) and all(height >= h for height in heights[max_ind:max_ind + w]):
        new_heights = [height for height in heights]
        for j in range(w):
            new_heights[max_ind + j] -= h
        new_history = [his for his in history]
        new_history.append((max_ind, heights[max_ind], HORIZONTAL))
        solve(new_heights, new_history, res)
    # put the tile vertically
    if w != h and max_ind + h <= len(heights) and all(height >= w for height in heights[max_ind:max_ind + h]):
        new_heights = [height for height in heights]
        for j in range(h):
            new_heights[max_ind + j] -= w
        new_history = [his for his in history]
        new_history.append((max_ind, heights[max_ind], VERTICAL))
        solve(new_heights, new_history, res)


def transform(x, y, direction):
    '''
    transform the tile representation to the standard format.
    Args:
        x: x-coordinate of the upper left corner
        y: y-coordinate of the upper left corner
        direction: HORIZONTAL or VERTICAL
    Returns:
        the transformed representation.
    '''
    global W, H, w, h
    if direction == HORIZONTAL:
        return tuple((j * W + i) for j in range(y - h, y) for i in range(x, x + w))
    else:
        return tuple((j * W + i) for j in range(y - w, y) for i in range(x, x + h))


def main():
    global W, H, w, h
    W = input('Wall width:')
    H = input('Wall height:')
    w = input('Tile width:')
    h = input('Tile height:')
    W, H, w, h = map(int, (W, H, w, h))
    init_heights = [H for _ in range(W)]
    res = []
    solve(init_heights, [], res)
    printable_res = [[transform(*step) for step in solution] for solution in res]
    print(printable_res, len(printable_res))
    if len(res) > 0:
        index = int(input('Input Number of 0 ~ {}'.format(len(res) - 1)))
        t = Turtle()
        draw_board(t)
        draw_solution(t, res[index])
        t.screen.exitonclick()
    else:
        print('No Solution')


if __name__ == '__main__':
    main()
