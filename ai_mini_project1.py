# -*- coding: utf-8 -*-




#ASSIGNMENT 1- “Maze Explorer Game”
'''🎯 Idea:

You’re in a maze represented by a grid.
You choose the algorithm (DFS or BFS), and the computer finds the path from Start (S) to Goal (G).
You can change walls and re-run the search.'''

from collections import deque

def print_grid(grid, path=None):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if path and (r, c) in path:
                print("•", end=" ")
            else:
                print(grid[r][c], end=" ")
        print()

def dfs(grid, start, goal):
    stack = [start]
    visited = set()
    parent = {}
    while stack:
        node = stack.pop()
        if node == goal:
            break
        if node in visited: continue
        visited.add(node)
        r, c = node
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr,nc) not in visited:
                parent[(nr,nc)] = node
                stack.append((nr,nc))
    # reconstruct path
    path = []
    node = goal
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    return path[::-1]

def bfs(grid, start, goal):
    q = deque([start])
    visited = {start}
    parent = {}
    while q:
        node = q.popleft()
        if node == goal: break
        r,c = node
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc = r+dr,c+dc
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] != '#' and (nr,nc) not in visited:
                visited.add((nr,nc))
                parent[(nr,nc)] = node
                q.append((nr,nc))
    path = []
    node = goal
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    return path[::-1]

if __name__ == "__main__":
    grid = [
        ['S', '.', '.', '#', '.'],
        ['.', '#', '.', '#', '.'],
        ['.', '#', '.', '.', '.'],
        ['.', '.', '#', '.', 'G']
    ]
    start = (0,0)
    goal = (3,4)
    print("Maze:")
    print_grid(grid)
    algo = input("Choose algorithm (dfs/bfs): ").lower()
    path = dfs(grid, start, goal) if algo == 'dfs' else bfs(grid, start, goal)
    print("\nPath found:")
    print_grid(grid, path)
