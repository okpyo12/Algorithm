num1, num2 = input().split()

if num1[2] > num2[2]:
    print(num1[::-1])
elif num1[2] < num2[2]:
    print(num2[::-1])
else:
    if num1[1] > num2[1]:
        print(num1[::-1])
    elif num1[1] < num2[1]:
        print(num2[::-1])
    else:
        if num1[0] > num2[0]:
            print(num1[::-1])
        elif num1[0] < num2[0]:
            print(num2[::-1])