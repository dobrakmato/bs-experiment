import numpy as np
import random
import keras
from keras.layers import Dense, LSTM
from keras.models import Sequential
import matplotlib.pyplot as plt
from keras.utils import plot_model

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

data = np.array([[random.random() * 10] for _ in range(20)])
labels = np.array([x ** 1/2 for x in data])

model = Sequential([
    Dense(1, input_dim=1),
    Dense(256),
    Dense(1),
])

#plot_model(model, to_file='model.png')

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
history = model.fit(data, labels, epochs=5000)

plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('input ' + str(16))
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['accuracy', 'loss'], loc='upper left')
plt.show()
