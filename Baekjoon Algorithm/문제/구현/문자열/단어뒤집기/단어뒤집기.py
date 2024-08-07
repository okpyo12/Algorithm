import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    str = sys.stdin.readline().rstrip()
    words = list(str.split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    answer = " ".join(reverse_words)
    print(answer)