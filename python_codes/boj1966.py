for _ in range(int(input())):
    queue = []
    n, target = map(int, input().split())
    for i, p in enumerate(priorities:=list(map(int, input().split()))):
        queue.append((i, p))
    cnt = 0
    
    while queue:
        if queue[0][1] == max(priorities):
            cnt += 1
            if queue[0][0] == target:
                print(cnt)
                break
            priorities.remove(queue[0][1])
        else:
            queue.append(queue[0])
        
        del queue[0]
