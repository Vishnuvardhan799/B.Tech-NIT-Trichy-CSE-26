import math
import random
import numpy as np
import tensorflow as tf


class Network(object):
    def __init__(self, layer_sizes):
        self.num_layers = len(layer_sizes)
        self.n_classes = layer_sizes[-1]
        self.x = tf.placeholder(tf.float32, [None, layer_sizes[0]])
        self.pkeep = tf.placeholder(tf.float32)
        self.learning_rate = tf.placeholder(tf.float32)
        self.decay_speed = 2000

        self.weights = []
        self.biases = []
        for j, k in zip(layer_sizes[:-1], layer_sizes[1:]):
            self.weights.append(tf.Variable(tf.truncated_normal([j, k], stddev=0.1)))
            self.biases.append(tf.Variable(tf.ones([k]) / 10))

        layer_input = tf.reshape(self.x, [-1, layer_sizes[0]])
        for i in range(0, self.num_layers - 2):
            layer_output = tf.nn.sigmoid(tf.matmul(layer_input, self.weights[i]) + self.biases[i])
            layer_output_dropped = tf.nn.dropout(layer_output, self.pkeep)
            layer_input = layer_output_dropped
        ylogits = tf.matmul(layer_input, self.weights[-1]) + self.biases[-1]
        self.y = tf.nn.sigmoid(ylogits)

        # placeholder for correct labels
        self.y_ = tf.placeholder(tf.float32, [None, self.n_classes])

        # loss function
        cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(logits=ylogits, labels=self.y_)
        cross_entropy = tf.reduce_mean(cross_entropy) * 100

        # Here TensorFlow computes the partial derivatives of the loss function relatively to all the weights and biases
        optimizer = tf.train.AdamOptimizer(learning_rate=self.learning_rate)
        self.train_step = optimizer.minimize(cross_entropy)

        self.sess = tf.Session()
        init = tf.global_variables_initializer()
        self.sess.run(init)

    def gradient_descent(self, training_data, n_epochs=10, min_learning_rate=0.0001, max_learning_rate=0.003):
        training_x, training_y = training_data
        training_y = np.array(training_y).reshape(len(training_y), 1)
        for epoch in range(0, n_epochs):
            random.shuffle(training_data)

            # load batch of data and q-value targets
            learning_rate = min_learning_rate + (max_learning_rate - min_learning_rate) * math.exp(
                -epoch / self.decay_speed)
            train_data_dict = {self.x: np.asarray(training_x),
                               self.y_: np.asarray(training_y),
                               self.learning_rate: learning_rate, self.pkeep: 0.75}

            # train
            self.sess.run(self.train_step, feed_dict=train_data_dict)

    def get_q_value(self, network_input):
        test_data_dict = {self.x: network_input.reshape(1, len(network_input)), self.pkeep: 1}
        return self.sess.run(self.y, feed_dict=test_data_dict)

