print("Please Enter numbers in range 1 to 10 !")
while True:
    m = int(input("Enter row:"))
    n = int(input("Enter col:"))
    multiplication_table = [["x",1,2,3,4,5,6,7,8,9,10,11],
                            [1,"-","-","-","-","-","-","-","-","-","-","-"],
                            [2,"-","-","-","-","-","-","-","-","-","-","-"],
                            [3,"-","-","-","-","-","-","-","-","-","-","-"],
                            [4,"-","-","-","-","-","-","-","-","-","-","-"],
                            [5,"-","-","-","-","-","-","-","-","-","-","-"],
                            [6,"-","-","-","-","-","-","-","-","-","-","-"],
                            [7,"-","-","-","-","-","-","-","-","-","-","-"],
                            [8,"-","-","-","-","-","-","-","-","-","-","-"],
                            [9,"-","-","-","-","-","-","-","-","-","-","-"],
                            [10,"-","-","-","-","-","-","-","-","-","-","-"],
                            [11,"-","-","-","-","-","-","-","-","-","-","-"],]

    for i in range(m):
        for j in range(n):
            multiplication_table[i+1][j+1] = (multiplication_table[i+1][0]) * (multiplication_table[0][j+1])

    for i in range(m):
        for j in range(n):
            print(multiplication_table[i][j], end=" ")
        print()
    break