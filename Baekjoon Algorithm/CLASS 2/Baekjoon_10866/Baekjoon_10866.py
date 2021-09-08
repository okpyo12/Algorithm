import sys

N = int(sys.stdin.readline())
dequeue = []
for _ in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push_front':
        dequeue.insert(0,a[1])
    elif a[0] == 'push_back':
        dequeue.append(a[1])
    elif a[0] == 'pop_front':
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue[0])
            del dequeue[0]
    elif a[0] == 'pop_back':
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue[-1])
            dequeue.pop()
    elif a[0] == 'size':
        print(len(dequeue))
    elif a[0] == 'empty':
        if len(dequeue) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue[0])
    elif a[0] == 'back':
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue[-1])