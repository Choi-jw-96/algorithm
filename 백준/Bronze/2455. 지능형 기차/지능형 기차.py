passenger = 0
passenger_list = []

for _ in range(4):
    out_p, in_p = map(int, input().split())
    passenger += in_p - out_p
    passenger_list.append(passenger)

print(max(passenger_list))