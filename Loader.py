import numpy as np


def load_dataset():
    with open('data/train-images.idx3-ubyte', 'rb') as fx:
        train_x = np.frombuffer(fx.read()[16:], dtype=np.uint8).reshape(60000, 784).T
    with open('data/train-labels.idx1-ubyte', 'rb') as fy:
        train_y = np.frombuffer(fy.read()[8:], dtype=np.uint8).reshape(1, 60000)

    with open('data/t10k-images.idx3-ubyte', 'rb') as fx:
        test_x = np.frombuffer(fx.read()[16:], dtype=np.uint8).reshape(10000, 784).T
    with open('data/t10k-labels.idx1-ubyte', 'rb') as fy:
        test_y = np.frombuffer(fy.read()[8:], dtype=np.uint8).reshape(1, 10000)

    return train_x, train_y, test_x, test_y, 10
