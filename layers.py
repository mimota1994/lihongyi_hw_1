import tensorflow as tf
import numpy as np
def layer(input_9,y_10):
    learning_rate=0.0001
    training_epochs=2000
    display_step=50
    
    input_9=np.array(input_9)
    y_10=np.array(y_10)

    a=input_9.shape[0]#n
    b=input_9.shape[1]#9

    y_10=y_10.reshape(a,1)
       
    w=tf.Variable(np.random.normal(-1,1,9).reshape(9,1),name='weight')
    b=tf.Variable(np.random.normal(),name='bias')
    
    X=tf.placeholder(tf.float64)
    #print(type(X))
    Y=tf.placeholder(tf.float64)

    activation=tf.add(tf.multiply(X,w),b)

    cost=tf.reduce_sum(tf.pow(activation-Y,2))/(2*n_samples)
    optimizer=tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    init=tf.initialize_all_variables()

    with tf.Session() as sess:
        sess.run(init)

        for epoch in range(training_epochs):
            sess.run(optimizer,feed_dict={X:input_9,Y:y_10})

            if epoch%diplay_step==0:
                print('Epoch:','%04d'%(epoch+1),'cost',sess.run(cost,feed_dict={X:input_9,Y:y_10}))
                
    


        
        

    

    
