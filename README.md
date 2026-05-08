🚀 Deepfake Image Detection System








📖 Overview



This project presents a Deepfake Image Detection System designed to classify facial images as REAL or FAKE using advanced deep learning techniques.

The solution leverages transfer learning with MobileNetV2 and is deployed through a Flask-based web application, enabling real-time predictions with confidence scores via a simple and intuitive interface.



🎯 Objective




The objective of this project is to develop a reliable system capable of identifying AI-generated (deepfake) images by:

Detecting manipulated facial content

Building an end-to-end machine learning pipeline

Delivering real-time predictions through a web interface



📂 Dataset



Dataset: Real vs Fake Face Dataset

Source: Kaggle Dataset Repository

The dataset contains a large collection of real and synthetically generated facial images used for training, validation, and evaluation.



🧠 Model Architecture




The model is built using Transfer Learning:

Base Model: MobileNetV2 (ImageNet pretrained)

Input Size: 128 × 128 × 3

Custom Layers

Global Average Pooling

Dense Layer (128, ReLU)

Dropout (0.5)

Sigmoid Output Layer

Classification Strategy

Probability > 0.5 → REAL

Probability ≤ 0.5 → FAKE



🧪 Methodology




🔹 Data Preparation


Dataset loading (train, validation, test)

Image resizing and normalization

Data augmentation to improve generalization



🔹 Model Development


Baseline CNN experimentation

Transfer learning using MobileNetV2

Training on ~100K images

Performance monitoring using accuracy and loss


🔹 Evaluation


Confusion Matrix analysis

Classification report generation

Accuracy and F1-score evaluation

Visualization of predictions


🔹 Deployment


Flask web application

Image upload interface

Real-time classification (REAL / FAKE)

Confidence score output


🏗️ Project Structure




Deepfake-Detection/
│
├── app.py
├── model.ipynb
├── deepfake.weights.h5
├── templates/
│   └── index.html
├── train.csv
├── valid.csv
├── test.csv
├── requirements.txt
└── README.md



💻 System Workflow




User uploads an image

Image is resized to 128×128

Pixel values are normalized

Model performs prediction

Output is displayed as:
REAL / FAKE

Confidence score




📊 Sample Results




Input Type	Prediction	Confidence

Real Image	REAL	0.99

Real Image	REAL	0.97

Deepfake	FAKE	0.02

Deepfake	FAKE	0.06



🚀 Key Features




Real-time deepfake detection

Lightweight and efficient architecture

Transfer learning-based approach

Clean and responsive UI

Scalable and easy to extend


⚠️ Challenges & Solution



Challenge:

Model loading issues due to TensorFlow/Keras version mismatch.


Solution:

Resolved by reconstructing the architecture and loading trained weights independently:


model.load_weights("deepfake.weights.h5")



🔮 Future Enhancements




Video-based deepfake detection

Cloud deployment (AWS / Render / Hugging Face)

Face detection preprocessing

Model explainability (Grad-CAM)

Mobile optimization



⚠️ Limitations



Performance depends on dataset quality

Limited generalization to unseen deepfake techniques

Requires further optimization for production use




🙏 Acknowledgements



Kaggle Deepfake Dataset

TensorFlow & Keras Documentation

Flask Documentation
