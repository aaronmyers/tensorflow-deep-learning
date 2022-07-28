import tensorflow as tf

print(tf.__version__)

scalar = tf.constant(7)

scalar.ndim

vector = tf.constant([10, 10])
vector

vector.ndim

matrix = tf.constant([[10,7],
    [7,10]]))
matrix

matrix.ndim

