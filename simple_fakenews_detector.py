""""
Dataset is small and hardcoded for demo

Model type: Simple feedforward neural network

Prediction: Takes input from the user and predicts "REAL" or "FAKE"

Limitations: Accuracy not reliable due to tiny sample size

"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Step 1: Sample data
texts = [
    "NASA finds water on Mars",
    "Apple launches new iPhone with AI",
    "Aliens have landed in Delhi",
    "Government bans all smartphones",
    "COVID-19 vaccine approved worldwide",
    "World ends tomorrow",
    "Elon Musk buys the Moon",
    "UN announces global peace treaty",
]
labels = ["REAL", "REAL", "FAKE", "FAKE", "REAL", "FAKE", "FAKE", "REAL"]

# Step 2: Text vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts).toarray()

# Step 3: Encode labels to numeric values
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(labels)  # FAKE -> 0, REAL -> 1
y_categorical = to_categorical(y_encoded)  # One-hot encoding

# Step 4: Build neural network
model = Sequential()
model.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(Dropout(0.2))  # Prevent overfitting
model.add(Dense(2, activation='softmax'))  # 2 output classes: FAKE, REAL

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 5: Train model
model.fit(X, y_categorical, epochs=20, verbose=0)

# Step 6: Take input and predict
headline = input("📰 Enter a news headline: ")
headline_vec = vectorizer.transform([headline]).toarray()
prediction = model.predict(headline_vec)

predicted_label = encoder.inverse_transform([np.argmax(prediction)])
print(" This news is:", "FAKE " if predicted_label[0] == "FAKE" else "REAL ")
