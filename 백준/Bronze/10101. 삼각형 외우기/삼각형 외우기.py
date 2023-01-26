#10101
triangle_1 = int(input())
triangle_2 = int(input())
triangle_3 = int(input())

if triangle_1 + triangle_2 + triangle_3 == 180:
    if triangle_1 and triangle_2 and  triangle_3 == 60:
        print("Equilateral")
    elif triangle_1 != triangle_2 and triangle_1 != triangle_3 and triangle_3 != triangle_2:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")