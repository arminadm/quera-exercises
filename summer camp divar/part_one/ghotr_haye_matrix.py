# 100/100
#Armin Darabi Mahboub

def main():
    n = int(input())
    rows = n
    cols = n
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    for row in range(n):
        row_detail = input()
        for col in range(n):
            matrix[row][col] = int(row_detail.split(' ')[col])
    
    main_train = []
    for i in range(n):
        main_train.append(matrix[i][i])
    sub_train = []
    for i in range(n):
        sub_train.append(matrix[i][n - i - 1])

    total_train = main_train + sub_train
    counter = 0
    for eachBlock in total_train:
        if eachBlock % 3 == 1:
            counter += eachBlock
    print(counter)

if __name__ == '__main__':
    main()