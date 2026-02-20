import tensorflow as tf
from tensorflow.keras import layers

class CashFlowPredictor:
    def __init__(self):
        self.model = None
    
    def build_model(self, input_shape):
        model = tf.Sequential([
            layers.Dense(64, activation='relu', input_shape=input_shape),
            layers.Dropout(0.2),
            layers.Dense(32, activation='relu'),
            layers.Dropout(0.1),
            layers.Dense(1)
        ])
        return model
    
    def train_model(self, X_train: tf.data.Dataset, y_train: tf.data.Dataset) -> None:
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        self.model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)
    
    def predict(self, data: tf.Tensor) -> tf.Tensor:
        return self.model(data)