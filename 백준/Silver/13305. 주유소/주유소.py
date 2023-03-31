n = int(input())

load = list(map(int, input().split()))
city = list(map(int, input().split()))

min_price = []
price = 0
add_price = 0
min_i = city.index(min(city[:n-1]))

for i in range(len(load)):
    if min_i >= i:
        price = sum(load[i:min_i]) * city[i] + sum(load[min_i:]) * city[min_i]
        min_price.append(price + add_price)
        add_price += min(city[:i+1]) * load[i]
    else:    
        break
print(min(min_price))