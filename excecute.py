import deal,transfer,layers

path=r'C:\Users\mimota\OneDrive\python\机器学习\lihongyi_hw_1\train.csv'
matrix=deal.deal(path)
x_9,y_10=transfer.transfer(matrix)
layers.layer(x_9,y_10)

