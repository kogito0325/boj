hour, minute, second = map(int, input().split())

second += int(input())
minute += second // 60
second %= 60
hour += minute // 60
minute %= 60
hour %= 24

print(hour, minute, second)