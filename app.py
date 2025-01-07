import gradio as gr
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import requests

# Load pre-trained Vision Transformer model and feature extractor
model_name = "google/vit-base-patch16-224"
model = ViTForImageClassification.from_pretrained(model_name)
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)

# Define prediction function
def classify_image(image):
    # Preprocess the image
    inputs = feature_extractor(images=image, return_tensors="pt")
    
    # Perform inference
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    
    # Get label
    predicted_label = model.config.id2label[predicted_class_idx]
    return f"Predicted Class: {predicted_label}"

# Gradio Interface
interface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Classification with Vision Transformers",
    description="Upload an image to classify it into one of the categories."
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
