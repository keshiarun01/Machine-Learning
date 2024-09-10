# Lung X-Ray Images to Predict Asthma Using Convolutional Neural Networks

This project involves developing a deep learning model using Convolutional Neural Networks (CNN) to predict asthma and classify its severity from lung X-ray images. The project utilizes Python libraries such as TensorFlow, Keras, and Django for building and deploying the model.

## Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [System Design](#system-design)
- [Methodologies](#methodologies)
- [Modules](#modules)
- [System Testing](#system-testing)
- [Conclusion and Future Work](#conclusion-and-future-work)
- [Directory Structure](#directory-structure)
- [Contributors](#contributors)

## Project Overview

Asthma is a critical respiratory disease requiring early detection and management to prevent progression. This project aims to develop a deep learning model based on CNN that classifies lung X-ray images into three stages of asthma severity: unaffected, intermittent asthma, and severe persistent asthma.

## Objectives

1. **Develop a CNN Model**: Create a deep learning model capable of classifying asthma severity from X-ray images.
2. **Evaluate Model Performance**: Use metrics like accuracy, sensitivity, and specificity to measure model effectiveness.
3. **User Interface Development**: Build a user-friendly interface using Django for real-time predictions.

## System Design

The system design consists of several diagrams to illustrate the workflow and architecture:

- **Architecture Diagram**: Shows the overall structure, data flow, and components of the system.
- **Use Case Diagram**: Describes the interactions between users and the system.
- **Data Flow Diagram**: Visualizes the flow of data within the system.
- **Activity and Sequence Diagrams**: Depict the flow of operations and the sequence of interactions.

## Methodologies

A Convolutional Neural Network (CNN) is used to classify X-ray images by learning features through various layers like Convolutional, MaxPooling, and Fully Connected layers. The architecture is inspired by the human visual cortex and is fine-tuned using different layers and activation functions to enhance prediction accuracy.

## Modules

### 1. Preprocessing and Training Module

- **Preprocessing**: Involves scaling, reshaping, and converting images into arrays.
- **Training**: The CNN model is trained with labeled data of normal, intermittent, and severe persistent asthma cases.

### 2. Classification Module

- **Feature Extraction**: Extracts features using various CNN layers.
- **Classification**: Uses softmax/logistic layers to classify images into severity levels.

### 3. Deployment Module

- **Model Deployment**: The trained model is converted into a `.h5` file and deployed using the Django framework to provide a user-friendly interface for real-time predictions.

## System Testing

The system undergoes rigorous testing to ensure functionality and accuracy:

- **Unit Testing**: Tests individual components of the system for correct behavior.
- **Integration Testing**: Verifies that different modules work together as expected.
- **Performance Testing**: Evaluates the system's handling of large datasets and ensures timely predictions.
- **Security Testing**: Ensures data protection and access control for patient data.

## Conclusion and Future Work

The project successfully demonstrates the use of deep learning to classify asthma severity from lung X-rays, achieving an accuracy of 93%. Future work includes optimizing the network for better accuracy, using larger datasets, and refining the user interface for clinical application.

## Directory Structure

```plaintext
├── dataset/
│   ├── train/
│   │   ├── INTERMITTENT_ASTHMA/
│   │   ├── NORMAL/
│   │   └── SEVERE_PERSISTENT_ASTHMA/
│   └── test/
├── models/
│   └── trained_model.h5
├── app/
│   ├── templates/
│   └── static/
├── requirements.txt
├── app.py
└── README.md
```

## Contributors

- **Keshika A** - [GitHub](https://github.com/keshikaa)
- **Kevin Austin**
