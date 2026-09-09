import torch
import torch.nn as nn
import tensorflow as tf


# =========================
# PyTorch Model
# =========================

class PyTorchModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(10, 16),
            nn.ReLU(),
            nn.Linear(16, 2)
        )

    def forward(self, x):
        return self.network(x)


def run_pytorch():

    model = PyTorchModel()

    sample_input = torch.randn(1, 10)

    output = model(sample_input)

    prediction = torch.argmax(output, dim=1)

    return prediction.item()


# =========================
# TensorFlow Model
# =========================

def run_tensorflow():

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(10,)),
        tf.keras.layers.Dense(16, activation="relu"),
        tf.keras.layers.Dense(2, activation="softmax")
    ])

    sample_input = tf.random.normal((1, 10))

    output = model(sample_input)

    prediction = tf.argmax(output, axis=1)

    return int(prediction.numpy()[0])