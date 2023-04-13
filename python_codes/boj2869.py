import math

front, back, goal = map(int, input().split())

print(math.ceil((goal - front) / (front - back)) + 1)
