import os
from scripts.describe import analyze_images

def main():
    """Main entry point for the image caption generator."""
    # Define input/output paths
    input_folder = "images"
    output_csv = "output/captions.csv"

    # Define parameters
    num_words = 10  # Desired number of words in captions

    # Ensure input/output folders exist
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return
    if os.path.exists(output_csv):
        print(f"Error: Output file '{output_csv}' exists. Please delete it first, or rename the output file in here.")
        return
    else:
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    # Run the analysis
    print("Starting image caption generation...")
    analyze_images(input_folder, output_csv, num_words)
    print(f"Captions saved to '{output_csv}'.")

if __name__ == "__main__":
    main()
