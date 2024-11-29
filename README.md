
# 🌟 Image Description Generator

A Python-based tool for generating captions for images using the **BLIP (Bootstrapped Language-Image Pretraining)** model from Salesforce.

## ✨ Features
- 📂 Automatically generates captions for all images in the `images` folder.
- ⚡ Supports processing multiple images in bulk.
- 📄 Saves the generated captions in a CSV file in the `output` folder.
- 🛠️ Modular design with reusable scripts for core functionality.

## 🤖 The Model: BLIP (Bootstrapped Language-Image Pretraining)
This project leverages the **BLIP (Base)** model, a pretrained vision-language model developed by Salesforce. BLIP is designed for tasks like image captioning, visual question answering, and image-text retrieval.

### 🔎 Why BLIP?
BLIP provides:
- **🚀 State-of-the-art performance**: Excellent results in generating natural language descriptions for images.
- **🌍 Pretrained on diverse datasets**: The model understands a wide range of concepts and objects.
- **🔧 Flexibility**: Works well out-of-the-box for image captioning without requiring fine-tuning.

### Model Details
- **Model Name**: `Salesforce/blip-image-captioning-base`
- **Architecture**: Vision Transformer (ViT) combined with a Transformer-based language model.
- **Source**: [Hugging Face Transformers](https://huggingface.co/Salesforce/blip-image-captioning-base)

For more information about BLIP, visit the [official paper](https://arxiv.org/abs/2201.12086).

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/image-description-generator.git
    cd image-description-generator
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

1. 📂 Place images in the `images` folder (e.g., `images/horse.jpg`).
2. ▶️ Run the main script:
    ```bash
    python main.py
    ```
3. ✅ Check the generated captions in the `output/captions.csv`.

### ⚙️ Command-Line Arguments
You can customize the behavior of the program by modifying the parameters in the scripts or adding command-line arguments. Current configuration includes:
- 📁 Input folder: `images/`
- 📄 Output file: `output/captions.csv`
- ✍️ Number of words: Default is 10 words per caption.

## 📂 Folder Structure

The repository is organized as follows:

```
image-description-generator/
├── images/                 # Folder for input images
│   ├── horse.jpg
│   ├── beach.jpg
│   └── ... (other images)
├── output/                 # Folder for generated outputs
│   └── captions.csv        # Captions generated for images
├── scripts/                # Python scripts for core functionality
│   ├── describe.py         # Logic for generating captions
│   └── utils.py            # Helper functions
├── main.py                 # Main script to execute the program
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
└── LICENSE                 # License file
```

## 🛠️ How It Works

1. **🖼️ Image Preprocessing**:
    - Each image in the `images/` folder is processed and converted into a format compatible with the BLIP model using the Hugging Face `transformers` library.
    
2. **✍️ Caption Generation**:
    - The BLIP model generates captions based on the visual features of the image.
    - Captions are generated with a configurable word limit (default: 10 words).

3. **📄 Output**:
    - Captions are saved in `output/captions.csv` with the format:
      ```
      Image,Caption
      horse.jpg,A brown horse galloping through a green field.
      beach.jpg,A beautiful sunset over a sandy beach with waves.
      ```

## 🤝 Contributing

Contributions are welcome! Open an issue or submit a pull request for improvements.

## 📜 License

This project is licensed under the MIT License.
