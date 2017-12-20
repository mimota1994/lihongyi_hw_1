#matrix/input.shape=24,240
def transfer(matrix):
    x_9=[]
    y_10=[]
    for i in matrix:
        for j in range(0,11):
            x_9.append(i[j:j+9])
            y_10.append(i[j+9])

    return x_9,y_10
        
