from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load processor and model (only load once for performance)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to("cpu")

def describe_image(image_path, num_words=10):
    """
    Generate a caption for an image.

    Args:
        image_path (str): Path to the input image.
        num_words (int): Desired number of words in the caption.

    Returns:
        str: Generated caption.
    """
    try:
        # Load and preprocess the image
        image = Image.open(image_path).convert("RGB")

        # Prepare inputs for the model
        inputs = processor(image, return_tensors="pt").to("cpu")

        # Generate the caption
        output = model.generate(
            **inputs,
            max_length=50,  # Allow room for the model to complete sentences
            min_length=5,   # Encourage meaningful captions
            num_beams=3,    # Beam search for quality
            repetition_penalty=1.2  # Penalize repetition
        )
        caption = processor.decode(output[0], skip_special_tokens=True)

        # Post-process: Limit to the desired number of words
        caption_words = caption.split()
        if len(caption_words) > num_words:
            # Truncate at the nearest punctuation for completeness
            truncated_caption = " ".join(caption_words[:num_words])
            if not truncated_caption.endswith(('.', '!', '?')):
                truncated_caption += "..."
            return truncated_caption
        return caption
    except Exception as e:
        print(f"Error describing {image_path}: {e}")
        return None
