import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

# Generate dummy data
x = np.random.randint(0, 2, size=(1000, 16))
y = [n[0] for n in x]
y = np.array(y)
x_train = x[:900]
y_train = y[:900]
x_test = x[900:]
y_test = y[900:]

model = Sequential()
model.add(Dense(1, input_dim=16))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=75)
score = model.evaluate(x_test, y_test)
print(score)
