from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras

y = np.load('labels/00e5671e594a6fe621c3605fcc5a0e4466ba6478.npy')
x = np.rot90(np.load('spectro/00e5671e594a6fe621c3605fcc5a0e4466ba6478.npy'))
x = x[0:y.shape[0]]
x = np.expand_dims(x, axis=2)

print('x.shape', x.shape)
print('y.shape', y.shape)

model = keras.Sequential()
model.add(keras.layers.LSTM(128))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

history = model.fit(x, y, epochs=250, shuffle=False)
print(model.summary())
# score = model.evaluate(x_test, y_test)
# print(score)


plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('onset by neural network')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['accuracy', 'loss'], loc='upper left')
plt.show()
