# Project Title - Deepfake Image Detection

# Objective

This project aims to detect whether an image is real or fake (deepfake) using deep learning techniques. The model is trained on a dataset of real and AI-generated facial images and deployed using a Flask web application for real-time predictions.

# Source

Dataset: Real vs Fake Face Dataset

Source: Kaggle Dataset Repository

### Phase 1 - Data Preparation and Preprocessing

* Loading dataset (train, validation, test)
* Image resizing and normalization
* Data augmentation

### Phase 2 - Model Building and Training

* Baseline CNN model
* Transfer Learning using MobileNetV2
* Model training on large dataset (~100k images)
* Accuracy and loss tracking

### Phase 3 - Model Evaluation

* Confusion Matrix
* Classification Report
* Accuracy and F1-score analysis
* Visualization of correct and incorrect predictions

### Phase 4 - Deployment

* Flask web application
* Image upload interface
* Real-time prediction (REAL / FAKE)
* Confidence score display

### Challenges and Solution

* Model loading failed due to TensorFlow/Keras version mismatch
* Resolved by rebuilding the model architecture and loading trained weights using:

model.load_weights("deepfake.weights.h5")

### License

This project is for academic and learning purposes.

### Acknowledgements

Deepfake Dataset (Kaggle)

TensorFlow & Keras documentation

Flask documentation

### Ashwin Shammy Mathew

### Entri Elevate