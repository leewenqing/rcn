import numpy as np
from rnn.rnn import RecurrentNeuralNetwork
from rnn.rcn import RecurrentControlNet
from rnn.tdnn import TimeDelayNeuralNetwork
# from rnn.tdcn import TimeDelayControlNet
import utils.activations as a
import utils.initializers as i

# select model from command line arg
map_str_model = {
    'rnn': RecurrentNeuralNetwork,
    'rcn': RecurrentControlNet,
    'tdnn': TimeDelayNeuralNetwork,
    # 'tdcn': TimeDelayControlNet
}

# base recurrent neural network
base_params = {
    'layer_activation': np.tanh,
    'hidden_size': 32,
    'kernel_initializer': np.zeros,
    'bias_initializer': np.zeros,
    'use_bias': True
}

# recurrent control net
rcn_params = {
    # nonlinear module
    'layer_activation': np.tanh,
    'hidden_size': 32,
    'n_kernel_initializer': np.zeros,
    'n_bias_initializer': np.zeros,
    'n_use_bias': True,

    # linear module
    'l_kernel_initializer': np.zeros,
    'l_bias_initializer': np.zeros,
    'l_use_bias': True
}

# time delay neural network
tdnn_params = {
    'layer_activation': np.tanh,
    'stride': 1,
    'window': 15,
    'layers': [16],
    'kernel_initializer': np.zeros,
    'bias_initializer': np.zeros,
    'use_bias': True
}