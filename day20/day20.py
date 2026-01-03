import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
import keras_tuner as kt
import os

# -----------------------------
# Load MNIST Dataset
# -----------------------------
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# -----------------------------
# Model Builder Function
# -----------------------------
def model_builder(hp):
    model = Sequential()
    model.add(Flatten(input_shape=(28, 28)))

    # Tune number of neurons
    model.add(Dense(
        units=hp.Int("units_1", min_value=32, max_value=128, step=32),
        activation='relu'
    ))

    model.add(Dense(
        units=hp.Int("units_2", min_value=32, max_value=128, step=32),
        activation='relu'
    ))

    model.add(Dense(10, activation='softmax'))

    # Tune learning rate
    learning_rate = hp.Choice(
        "learning_rate", values=[1e-2, 1e-3, 1e-4]
    )

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model

# -----------------------------
# Random Search Tuner
# -----------------------------
tuner = kt.RandomSearch(
    model_builder,
    objective='val_accuracy',
    max_trials=5,
    executions_per_trial=1,
    directory='tuner_results',
    project_name='mnist_tuning'
)

tuner.search(
    x_train,
    y_train,
    epochs=5,
    validation_data=(x_test, y_test)
)

# -----------------------------
# Get Best Model
# -----------------------------
best_model = tuner.get_best_models(num_models=1)[0]

# Evaluate best model
test_loss, test_accuracy = best_model.evaluate(x_test, y_test)
print(f"Best Model Test Accuracy: {test_accuracy:.4f}")

# -----------------------------
# Save Best Model
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "mnist_best_model.h5")

best_model.save(model_path)
print("✅ Best tuned model saved at:", model_path)
