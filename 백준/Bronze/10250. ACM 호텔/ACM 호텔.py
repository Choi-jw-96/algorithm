T = int(input())

for t in range(T):
    H, W, num = map(int, input().split())


    if num % H == 0:
        room = (num // H) 
        
    else:
        room = (num // H) + 1

    floor = num - (H * (room - 1))

    if room < 10:
        print(f'{floor}0{room}')
    else:
        print(f'{floor}{room}')