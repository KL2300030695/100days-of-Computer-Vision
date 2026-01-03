# Day 19: Deep Learning Model Building on TensorFlow

## Task
Build, train, and save a deep learning model using TensorFlow on the MNIST dataset.

## Dataset
MNIST Handwritten Digits Dataset
- Image size: 28 × 28
- Classes: 0–9
- Grayscale images

## Model Architecture
32 → 64 → 128 → 32 → 10

## Approach
- Loaded the MNIST dataset using TensorFlow.
- Normalized pixel values for faster convergence.
- One-hot encoded the labels.
- Built a deep neural network using Dense layers.
- Trained the model using Adam optimizer.
- Evaluated the model on test data.
- Saved the trained model for reuse.

## Techniques Used
- `Sequential()` – Model creation
- `Dense()` – Fully connected layers
- `Flatten()` – Input reshaping
- `model.fit()` – Training
- `model.save()` – Save trained model

## Insights and Observations
- Deeper networks learn better feature representations.
- Normalization improves training stability.
- This model can be extended into a CNN for higher accuracy.

## Code
Implementation is available in `day19.py`.
