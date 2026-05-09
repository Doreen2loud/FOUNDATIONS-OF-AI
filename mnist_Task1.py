import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress all TensorFlow logging (including errors)


#Loading of libraries and mnist dataset


import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print("All the libraries loaded successfully and ready to use.")

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print("Training images:", x_train.shape)
print("Training labels:", y_train.shape)
print("Testing images: ", x_test.shape)
print("Testing labels: ", y_test.shape)

print("Exploring the dataset...")

print("Example of one image")

print(x_train[0])

print("The label of the image is: ")

print(y_train[0])


print("EXPLORING THE DATA")


print("\nDisplaying 10 sample images...")

plt.figure(figsize=(15, 3))# creating the canvas

for i in range(10):

    plt.subplot(1, 10, i+1)#making the slots

    plt.imshow(x_train[i], cmap='gray')#equivalent to pasting the image

    plt.title(f"Label:{y_train[i]}")
    plt.axis('off')

plt.suptitle("Sample MNIST Images")
plt.show()

print("Visualization complete")


print("PREPARING THE DATA")

#Normalization

x_train = x_train / 255.0
x_test = x_test / 255.0

print("Data normalized successfully.")


print("Pixel values are now simplified to be between:", x_train.min(), "and", x_train.max())


# Flattening the images(converting from 3D to 2D)

x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)


print("Data flattened successfully.")



print("Training data new shape:", x_train.shape)


print("Testing data new shape:", x_test.shape)

model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])



print("Model architecture defined successfully.")

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("Model compiled successfully.")

model.summary()

print("Model summary displayed successfully.")

print("TRAINING THE MODEL")

model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

print("Model trained successfully.")

print("EVALUATING THE MODEL")
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

print("Model evaluation complete.")

print("MAKING PREDICTIONS")

predictions = model.predict(x_test)


plt.figure(figsize=(15, 3))
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Pred:{np.argmax(predictions[i])}\nReal:{y_test[i]}")
    plt.axis('off')
plt.suptitle("AI Predictions vs Real Labels")
plt.show()


print("Predictions made and visualized successfully.")