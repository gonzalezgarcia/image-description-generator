"""
This script generates text-to-speech (TTS) audio files from captions stored in a CSV file using the Bark model.

Procedure:
    1. Import necessary libraries and modules.
    2. Initialize the processor and model with the "suno/bark" model.
    3. Set the voice preset to "v2/en_speaker_6".
    4. Check if the "output/captions.csv" file exists.
    5. If the file exists, read the captions from the CSV file.
    6. For each caption, process the text and generate the corresponding audio using the Bark model.
    7. Save the generated audio as a WAV file in the "output/tts/" directory.
    8. Print a message indicating the successful generation of TTS for each caption.
    9. If the CSV file does not exist, print a message indicating that the file is not found and suggest using "main.py" to generate captions.
"""
import warnings
warnings.filterwarnings("ignore")
import os
import csv
from transformers import AutoProcessor, BarkModel
import scipy

# Initialize the processor and model
processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")
voice_preset = "v2/en_speaker_6"

# Check if captions.csv exists
if os.path.exists("output/captions.csv"):
    with open("output/captions.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for i, row in enumerate(reader):
            caption = row[1]
            inputs = processor(caption, voice_preset=voice_preset)
            audio_array = model.generate(**inputs)
            audio_array = audio_array.cpu().numpy().squeeze()
            sample_rate = model.generation_config.sample_rate
            output_path = f"output/tts/caption_{row[0][:-4]}.wav"
            scipy.io.wavfile.write(output_path, rate=sample_rate, data=audio_array)
            print(f"Generated TTS for caption {row[0][:-4]}: {output_path}")
else:
    print("captions.csv not found. Please use main.py to generate captions.")