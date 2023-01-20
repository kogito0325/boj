shortest_to_x, shortest_to_y, shortest_to_w, shortest_to_h = map(int, input().split())

shortest_to_w = shortest_to_w - shortest_to_x
shortest_to_h = shortest_to_h - shortest_to_y

print(min(shortest_to_x, shortest_to_y, shortest_to_w, shortest_to_h))
