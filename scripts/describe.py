import os
import csv
from scripts.utils import describe_image

def analyze_images(input_folder, output_csv, num_words=10):
    """Analyze all images in a folder and save captions to a CSV file."""
    # List all images in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Prepare to write results to a CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Image", "Caption"])  # Write header

        for image_file in image_files:
            image_path = os.path.join(input_folder, image_file)
            print(f"Processing: {image_path}")
            
            # Generate a caption for the image
            caption = describe_image(image_path, num_words)
            if caption:
                writer.writerow([image_file, caption])
                print(f"Caption: {caption}")
            else:
                print(f"Failed to generate caption for {image_file}")
