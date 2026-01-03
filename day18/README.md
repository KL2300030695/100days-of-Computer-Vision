# Day 18: Handwritten Digit Recognition with Keras (MNIST)

## Task
Load and display the first 20 handwritten digits from the Keras MNIST dataset.

## Dataset
MNIST Handwritten Digits Dataset
- 60,000 training images
- 10,000 testing images
- Image size: 28 × 28 pixels
- Grayscale images
- Digit classes: 0 to 9

## Approach
- Loaded the MNIST dataset using Keras.
- Inspected the shape of training data and labels.
- Displayed the first 20 digit images using Matplotlib.
- Annotated each image with its corresponding label.

## Code Snippet

```python
from keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()

plt.figure(figsize=(12, 5))
for i in range(20):
    plt.subplot(4, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(f"Label: {y_train[i]}")
    plt.axis("off")

plt.show()
