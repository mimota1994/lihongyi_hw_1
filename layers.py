import numpy as np
#输入x_9是一个n行九列的矩阵，y_10是n维向量
def layer(x_9,y_10):
    #generate the initial weight and bias
    w=np.random.normal(-1,1,9).reshape(9,1)
    b=np.random.normal(-1,1)
    #print(w,b)

    x_9=np.array(x_9)
    y_10=np.array(y_10)

    a=x_9.shape[0]#n
    b=x_9.shape[1]#9
    '''
    #get the Y
    Y=[]
    for i in x_9:
        Y.append(np.sum(np.multiply(w,i))+b)
    #loss function
    loss=np.sum(np.square(Y-y_10))/2*(x_9.shape[1])
    '''
    #GD
    learn_rate=0.001
    loss=1#to go
    k=1
    while(k==1):
        #微分
        k+=1
        matrix=x_9.reshape(b,a)
        p=np.dot(matrix,np.dot(x_9,w)+b-y_10.reshape(a,1))/b
        #print('p',p)
        print('w',w)
        w=w-learn_rate*p
        print('w*',w)
        loss=np.sum(np.square(np.dot(x_9,w)+b-y_10))/(2*a)
        #print('loss',loss)

        
        
        
        

    

    
