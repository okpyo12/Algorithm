from itertools import product

def solution(users, emoticons):
    answer = []
    sales = [0.6,0.7,0.8,0.9]
    for user in users:
        user[0] = 1 - user[0] / 100
    emoticons.sort(reverse=True)
    prod = product(sales, repeat=len(emoticons))
    for i in prod:
        plus = 0
        total = 0
        for j in range(len(users)):
            price = 0
            for k in range(len(emoticons)):
                if users[j][0] >= i[k]:
                    price += emoticons[k]*i[k]
            if price >= users[j][1]:
                plus += 1
            else:
                total += price
        answer.append([plus,total])
    answer.sort(key=lambda x : (-x[0],-x[1]))
    return answer[0]