H, M = input().split()

H, M = int(H), int(M)

M = M-45
if M < 0:
    H = H -1
if H < 0:
    H = 24+H
if 60+M >= 60:
    print(H, M)
else:
    print(H, 60+M)