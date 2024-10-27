# 生成迷宫，读入迷宫文件
maze = []

with open('迷宫_.txt','r') as f:
    for line in f:
        row = []
        line = line.replace('\n','')
        for l in line:
            row.append(l)
        maze.append(row)

for m in maze:
    for n in m:
        print(n,end='')
    print('\n')

# 解决迷宫
def is_valid_move(maze, visited, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '*' and (x, y) not in visited

def solve_maze(maze):
    stack = []
    visited = set()
    path = []
    start_x, start_y = -1, -1
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'P':
                start_x, start_y = i, j
                stack.append((i, j, [(i, j)]))  # 将起点加入栈，并记录路径
                break
        if start_x != -1:
            break

    while stack:
        x, y, current_path = stack.pop()
        if maze[x][y] == 'T':
            return current_path  # 找到终点，返回路径
        visited.add((x, y))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(maze, visited, nx, ny):
                new_path = list(current_path)
                new_path.append((nx, ny))
                stack.append((nx, ny, new_path))  # 将新位置加入栈，并更新路径

    return []  # 没有找到终点，返回空路径

def path_maze(path):
    for step in path[1:]:
        i,j = step[0],step[1]
        maze[i][j] = '$'

# 调用函数解决迷宫
path = solve_maze(maze)
if path:
    path_maze(path)
    for m in maze:
        for n in m:
            print(n, end='')
        print('\n')
else:
    print("迷宫无解。")
