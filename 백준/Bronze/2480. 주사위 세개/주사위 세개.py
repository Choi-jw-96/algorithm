Dice_1, Dice_2, Dice_3 = map(int, input().split())
D_list = [Dice_1, Dice_2, Dice_3]
mny = 0
if Dice_1 == Dice_2 == Dice_3:
    mny = 10000 + (Dice_1 * 1000)
elif Dice_1 != Dice_2 and Dice_1 != Dice_3 and Dice_2 != Dice_3:
    D = 0
    for N in range(3):
        if D < D_list[N]:
            D = D_list[N]
    mny = D * 100
else:
    if Dice_1 == Dice_2:
        mny = 1000 + (Dice_1 * 100)
    elif Dice_1 == Dice_3:
        mny = 1000 + (Dice_1 * 100)
    else:
        mny = 1000 + (Dice_2 * 100)
print(mny)