# remove warnings
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