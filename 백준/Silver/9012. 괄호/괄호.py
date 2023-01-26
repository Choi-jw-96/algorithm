T = int(input())

for t in range(T):
    VPS = input()
    VPS_list = []

    for vps in VPS:
        if vps == "(":
            VPS_list.append(vps)

        else:
            if len(VPS_list) != 0:                
                if VPS_list[len(VPS_list) - 1] == "(":
                    VPS_list.pop()
            else:
                VPS_list.append(vps)


    
    if len(VPS_list) == 0:
        print("YES")
    else:
        print("NO")
