# -*- coding: utf-8 -*-




#5. 3
 (Greedy MST)
'''🎯 Idea:

You enter number of cities and connection costs (edges).
Computer uses Prim’s Greedy algorithm to find cheapest connections. '''

import heapq
from collections import defaultdict

def prim_mst(graph, start=0):
    visited = set()
    pq = [(0, start, -1)]
    total = 0
    mst = []

    while pq:
        w, u, parent = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if parent != -1:
            mst.append((parent, u, w))
            total += w
        for v, wt in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (wt, v, u))

    return mst, total

if __name__ == "__main__":
    print("=== City Connector (Prim's Algorithm) ===")
    n = int(input("Enter number of cities (nodes): "))
    graph = defaultdict(list)

    e = int(input("Enter number of roads (edges): "))
    print("\n👉 Enter each road as:  u v cost")
    print("Example:  0 1 4  (means road between city 0 and city 1 costs 4)\n")

    for i in range(e):
        while True:
            try:
                u, v, w = map(int, input(f"Road {i+1}: ").split())
                if u < 0 or v < 0 or u >= n or v >= n:
                    print(f"⚠️ Invalid city index. Enter values between 0 and {n-1}. Try again.")
                    continue
                graph[u].append((v, w))
                graph[v].append((u, w))
                break
            except ValueError:
                print("⚠️ Please enter three integers: u v cost (e.g., 0 1 4). Try again.")

    mst, total = prim_mst(graph)

    print("\n✅ Minimum connections to connect all cities:")
    for u, v, w in mst:
        print(f"  City {u} ↔ City {v} : Cost {w}")
    print("Total cost of connection:", total)
