sentence = input()

sentence = sentence.upper()
list_value = []
list_keys = []
dic = {}

for i in range(len(sentence)):
    if sentence[i] in dic:
        dic[sentence[i]] += 1
    else:
        dic[sentence[i]] = 1

list_value = list(dic.values())
list_keys = list(dic.keys())
maximun = [k for k,v in dic.items() if max(dic.values()) == v]

if len(list_value) == 1:
    print(list_keys[0])
else:
    if len(maximun) > 1:
        print('?')
    else:
        print(maximun[0])