# Day 20: Model Hyperparameter Tuning for Improved Accuracy

## Task
Perform hyperparameter tuning on a deep learning model to improve accuracy.

## Dataset
MNIST Handwritten Digits Dataset

## Approach
- Loaded MNIST dataset.
- Built a tunable neural network model.
- Used Random Search to tune:
  - Number of neurons
  - Learning rate
- Selected the model with the highest validation accuracy.
- Evaluated and saved the best model.

## Hyperparameters Tuned
- Dense layer units (32–128)
- Learning rate (0.01, 0.001, 0.0001)

## Techniques Used
- Keras Tuner – Random Search
- TensorFlow Sequential API
- Adam optimizer
- Model evaluation and saving

## Insights and Observations
- Hyperparameter tuning significantly improves accuracy.
- Learning rate has a strong impact on convergence.
- Random search is faster than grid search for deep models.

## Code
Implementation is available in `day20.py`.
