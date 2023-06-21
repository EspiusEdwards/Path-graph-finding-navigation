#import common.py
from common import *
from GUI import *
def dfs(cell, draw_gui = None):
    if draw_gui:
        draw_grid, grid = draw_gui     
    INSTRUCTION = {"right":(1, 0), "down":(0, 1), "left":(-1, 0), "up":(0, -1)}
    stack = []
    count_node = 1
    stack.append((initial_x, initial_y))
    father = [[None for y in range(cell.h)] for x in range(cell.w)]
    visit = [[False for y in range(cell.h)] for x in range(cell.w)]
    while len(stack) > 0:
        current = stack.pop()
        visit[current[0]][current[1]] = True
        if cell.grid[current[0]][current[1]] == 3:
            if draw_gui:
                return print_path(father, INSTRUCTION, (initial_x, initial_y), current, count_node, grid)
            else:
                return print_path(father, INSTRUCTION, (initial_x, initial_y), current, count_node)
        for instruction in INSTRUCTION:
            new_x = current[0] + INSTRUCTION[instruction][0]
            new_y = current[1] + INSTRUCTION[instruction][1]
            if 0 <= new_x < cell.w and 0 <= new_y < cell.h and cell.grid[new_x][new_y] != 1 and not visit[new_x][new_y]:
                stack.append((new_x, new_y))
                count_node += 1
                if draw_gui:
                    if(grid[new_x][new_y].color != GREEN and grid[new_x][new_y].color != RED):
                        grid[new_x][new_y].make_queue()
                father[new_x][new_y] = instruction
        if draw_gui:
            if grid[current[0]][current[1]].color != GREEN and grid[current[0]][current[1]].color != RED:
                grid[current[0]][current[1]].make_visited()     
            draw_grid()
    return f"{sys.argv[1]} {sys.argv[2]} {count_node} \nNo solution found."
#print(dfs(cell))