T = int(input())

for t in range(T):
    money = int(input())
    Quarter = money // 25
    Dime = (money - Quarter * 25) // 10
    Nickel = (money - (Quarter * 25 + Dime * 10)) // 5
    Penny = (money - (Quarter * 25 + Dime * 10 + Nickel * 5)) // 1
    print(Quarter, Dime, Nickel, Penny)