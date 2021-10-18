def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id2 = ''
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            new_id2 += i
        else:
            continue

    new_id3 = new_id2[0]
    for i in range(1, len(new_id2)):
        if new_id2[i] == '.':
            if new_id2[i-1] == '.':
                continue
            else:
                new_id3 += new_id2[i]
                continue
        else:
            new_id3 += new_id2[i]

    for i in range(len(new_id3)):
        if new_id3[0] == '.':
            new_id3 = new_id3[1:]
        elif new_id3[-1] == '.':
            new_id3 = new_id3[:-1]
    
    if len(new_id3) == 0:
        new_id3 += 'a'
    if len(new_id3) >= 16:
        new_id3 = new_id3[:15]

    for i in range(len(new_id3)):
        if new_id3[-1] == '.':
            new_id3 = new_id3[:-1]
    
    while len(new_id3) <= 2:
        new_id3 += new_id3[-1]
    answer = new_id3
    return answer
