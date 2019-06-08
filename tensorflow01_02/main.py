# coding:utf-8
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Embedding, Dropout, Conv1D, Dense, GlobalMaxPooling1D
from keras.preprocessing import sequence
from keras.datasets import imdb
from keras import backend as K

# 代码源于keras example的 imdb_cnn.py
max_features = 5000
maxlen = 20
batch_size = 32
embedding_dims = 50
filters = 250
kernel_size = 3
hidden_dims = 250
epochs = 2

# 读取数据
print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

# 定义模型
# 这里对每个层都添加一个name
model = Sequential()
model.add(Embedding(max_features + 1, 100, name="input_layer"))
model.add(Dropout(0.2, name="dropout_layer1"))
model.add(Conv1D(filters=256, kernel_size=5, padding="valid", activation="relu", strides=1, name="cnn_layer"))
model.add(Dropout(0.2, name="dropout_layer2"))
model.add(GlobalMaxPooling1D(name="maxpooling_layer"))
model.add(Dense(256, activation='relu', name="dense_layer1"))
model.add(Dropout(0.2, name="dropout_layer3"))
model.add(Dense(2, activation='softmax', name="output_layer"))

# 模型训练
sess = tf.Session()
K.set_session(sess)

# 这步找到input_layer和output_layer的完整路径，在golang中使用时需要用来定义输入输出node
for n in sess.graph.as_graph_def().node:
    if 'input_layer' in n.name:
        print(n.name)
    if 'output_layer' in n.name:
        print(n.name)

model.fit(x_train,
          y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test),
          shuffle=1)

# 以下是关键代码
# Use TF to save the graph model instead of Keras save model to load it in Golang
builder = tf.saved_model.builder.SavedModelBuilder("cnnModel")
# Tag the model, required for Go
builder.add_meta_graph_and_variables(sess, ["myTag"])
builder.save()
sess.close()