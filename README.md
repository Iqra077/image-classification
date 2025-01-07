# image-classification
---
title: Image Classification App
emoji: 🖼️
colorFrom: purple
colorTo: orange
sdk: gradio
sdk_version: 5.9.1
app_file: app.py
pinned: false
---

# Image Classification with Vision Transformers

This app classifies images into predefined categories using a pre-trained Vision Transformer (ViT) model from Hugging Face's Transformers library. The app is built with Gradio, providing an interactive interface for image classification.

## Features
- Accepts image uploads and classifies them into categories.
- Utilizes the powerful Vision Transformer (`google/vit-base-patch16-224`) for accurate image classification.
- Simple and intuitive web interface built with Gradio.

## How to Use
1. **Upload an image** or drag and drop an image into the input box.
2. Click **"Submit"** to classify the image and view the predicted category.

## Example Inputs:
- **A picture of a cat** → Predicted Class: Cat
- **A picture of a dog** → Predicted Class: Dog
- **A picture of a car** → Predicted Class: Car

## Deployment
This app is designed for deployment on Hugging Face Spaces. The app is continuously deployed with updates via GitHub or Hugging Face Spaces CLI.

## How It Works
1. The app uses the **Vision Transformer (ViT)** from Hugging Face's Transformers library.
2. Uploaded images are preprocessed using the `ViTFeatureExtractor` to ensure compatibility with the model.
3. The model predicts the category of the image, returning the result along with the class label.

## Tech Stack
- **Transformers**: For the pre-trained Vision Transformer model.
- **Gradio**: For creating the interactive interface.
- **Pillow**: For image preprocessing.
- **Hugging Face Spaces**: For deployment and hosting.

## Development and Testing
- Use the included `Makefile` to automate tasks such as dependency installation, linting, and testing.
- Run `make install` to set up the environment.
- Run `make test` to perform unit tests (if implemented).
- Run `make lint` to ensure code quality and formatting.

## Requirements
- Python 3.8+
- Libraries listed in `requirements.txt`:
  - `gradio`
  - `transformers`
  - `torch`
  - `Pillow`
  - `huggingface_hub`

## Continuous Integration and Deployment (CI/CD)
The app supports CI/CD through a well-structured `Makefile` and deployment to Hugging Face Spaces. Use the `deploy` target in the `Makefile` to upload the app.

---

Feel free to upload an image and explore its classification result.
