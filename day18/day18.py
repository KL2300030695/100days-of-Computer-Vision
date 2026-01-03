import matplotlib.pyplot as plt
from keras.datasets import mnist

# -----------------------------
# Load the MNIST dataset
# -----------------------------
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Training data shape:", x_train.shape)
print("Training labels shape:", y_train.shape)

# -----------------------------
# Display first 20 images
# -----------------------------
plt.figure(figsize=(12, 5))

for i in range(20):
    plt.subplot(4, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(f"Label: {y_train[i]}")
    plt.axis("off")

plt.suptitle("First 20 Handwritten Digits from MNIST Dataset", fontsize=14)
plt.tight_layout()
plt.show()
