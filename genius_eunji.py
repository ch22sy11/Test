def solution(n):
    count = 0
    for i in range(1, 1+n):
        i=str(i)
        if '3' in i:
            count = count + 1
        elif '6' in i:
            count = count + 1
        elif '9' in i:
            count = count + 1
        else: pass
    clap = count
    print(clap)

solution(30)

