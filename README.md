---
title: Image Classification App
emoji: 🖼️
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "3.40.0"
app_file: app.py
pinned: false
---

# Image Classification with Vision Transformers

This app performs image classification using a pre-trained Vision Transformer (ViT) model from Hugging Face's Transformers library. Built with Gradio, it provides an intuitive interface for users to upload images and classify them into categories.

## Features
- Classifies images into pre-defined categories using the Vision Transformer model.
- User-friendly interface built with Gradio.
- Can be deployed easily on Hugging Face Spaces or other platforms.

## How to Use
1. **Upload an image** using the provided interface.
2. Click **"Submit"** to classify the image.
3. View the predicted category.

## Example Inputs:
- **Upload an image of a cat** → Predicted Class: Cat
- **Upload an image of a dog** → Predicted Class: Dog

## Deployment
This app can be deployed on Hugging Face Spaces or other cloud platforms. The deployment process ensures continuous integration and easy updates.

## How It Works
The app uses a pre-trained Vision Transformer (ViT) model from Hugging Face's `transformers` library. The `ViTFeatureExtractor` preprocesses the image, and the model predicts the class based on the input.

## Tech Stack
- **Hugging Face Transformers**: For the Vision Transformer model and feature extractor.
- **Gradio**: For building the interactive web interface.
- **Hugging Face Spaces**: For hosting and deploying the application.

---

Feel free to upload images and explore the classification capabilities of this app!

