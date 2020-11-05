from typing import List
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
from com_sba_api.ext.db import db, openSession, engine
from pathlib import Path
from sqlalchemy import func
from dataclasses import dataclass
import json
import pandas as pd
import json
import os
import pandas as pd
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


class CabbageAi(object):
    
    def __init__(self):
        self.path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'models','cabbage')

    def create(self):
        
        tf.global_variables_initializer()
        df = pd.read_sql_table('cabbages', engine.connect())
        xy = np.array(df, dtype=np.float32)
        x_data = xy[:,1:-1] #feature
        y_data = xy[:,[-1]] # 가격
        X = tf.placeholder(tf.float32, shape=[None, 4])
        Y = tf.placeholder(tf.float32, shape=[None, 1])
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        hypothesis = tf.matmul(X, W) + b
        cost = tf.reduce_mean(tf.square(hypothesis - Y))
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)
        train = optimizer.minimize(cost)
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        # 러닝
        for step in range(100000):
            cost_, hypo_, _ = sess.run([cost, hypothesis, train],
                                       feed_dict={X: x_data, Y: y_data})
            if step % 500 == 0:
                print('# %d 손실비용 : %d'%(step, cost_))
                print("- 배추가격 : %d" % (hypo_[0]))
                
        # 저장
        saver = tf.train.Saver()
        
        saver.save(sess, self.path+'/cabbage.ckpt')
        print('저장완료')