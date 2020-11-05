class CabbageService(object):
    def __init__(self):
        self.path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'models','cabbage2')
       
    avg_temp: float = 0.0
    min_temp: float = 0.0
    max_temp: float = 0.0
    rain_fall: float = 0.0

    def assign(self, param):
        self.avg_temp = param.avg_temp
        self.min_temp = param.min_temp
        self.max_temp = param.max_temp
        self.rain_fall = param.rain_fall

    def predict(self):
        X = tf.placeholder(tf.float32, shape=[None, 4])
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        saver = tf.train.Saver()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())

            saver.restore(sess, self.path+'/cabbage.ckpt')
            data = [[self.avg_temp, self.min_temp, self.max_temp, self.rain_fall],]
            arr = np.array(data, dtype = np.float32)
            dict = sess.run(tf.matmul(X, W) + b, {X: arr[0:4]})
            print(dict[0])
        return int(dict[0])



if __name__ == "__main__":
    c = CabbageAi()
    c.new()

    '''
    service = CabbageService()
    cabbage = CabbageVo()
    cabbage.avg_temp = 10
    cabbage.max_temp = -5
    cabbage.min_temp = 30
    cabbage.rain_fall = 20
    service.assign(cabbage)
    price = service.predict()
    print(f'Predicted Cabbage Price is {price} won')
    '''
