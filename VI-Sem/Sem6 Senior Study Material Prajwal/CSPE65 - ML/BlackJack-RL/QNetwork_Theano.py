import numpy as np
import theano
from theano import tensor as T


def convert_to_shared(data):
    """Place the data into shared variables.  This allows Theano to copy
    the data to the GPU, if one is available.
    """
    shared_x = theano.shared(
        np.asarray(data[0], dtype=theano.config.floatX), borrow=True)
    shared_y = theano.shared(
        np.asarray(data[1], dtype=theano.config.floatX), borrow=True)
    return shared_x, shared_y


class Layer(object):
    def __init__(self, layer_input, n_in, n_out, activation_fn=T.nnet.relu):
        self.w = theano.shared(np.asarray(np.random.normal(loc=0.0, scale=np.sqrt(1.0 / n_out), size=(n_in, n_out)), dtype=theano.config.floatX))
        self.b = theano.shared(np.asarray(np.zeros((n_out,), dtype=theano.config.floatX)))

        self.input = layer_input
        self.output = activation_fn(T.dot(self.input, self.w) + self.b)
        self.params = [self.w, self.b]

    def cost(self, net):
        return T.mean(T.square(self.output - net.y[0]))

    def output_value(self):
        return T.dot(self.input, self.w) + self.b


class Network(object):
    def __init__(self, layer_sizes):
        self.x = T.matrix("x")
        self.y = T.vector("y")

        self.layers = []
        next_input = self.x
        for x, y in zip(layer_sizes[:-1], layer_sizes[1:]):
            layer = Layer(next_input, x, y)
            self.layers.append(layer)
            next_input = layer.output

        self.params = [param for layer in self.layers for param in layer.params]

    def gradient_descent(self, training_data, epochs, eta=0.05):
        training_x, training_y = convert_to_shared(training_data)

        cost = self.layers[-1].cost(self)
        gradients = T.grad(cost, self.params)
        updates = [(param, param - eta * grad) for param, grad in zip(self.params, gradients)]

        train = theano.function(
            [], cost, updates=updates,
            givens={
                self.x: training_x,
                self.y: training_y
            }
        )

        for epoch in xrange(epochs):
            train()

    def get_q_value(self, network_input):
        shared_network_input = theano.shared(
            np.asarray([network_input], dtype=theano.config.floatX), borrow=True)

        q_value = self.layers[-1].output_value()

        predict = theano.function(
            [], q_value,
            givens={
                self.x: shared_network_input,
            }
        )

        return predict()[0][0]
