# -*- coding: UTF-8 -*-

# 引入TensorFlow库
import tensorflow as tf

# 创建一个常量
hw = tf.constant("Hello World ! I love TensorFlow")

# 启动一个TensorFlow 的 Session(回话)
sess = tf.Session()

# 运行Graph(计算图)
print(sess.run(hw))

sess.close()
