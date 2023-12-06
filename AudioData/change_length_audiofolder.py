# Change the length of all audio files in a folder to 5 seconds

import os
from pydub import AudioSegment

def convert_audio_to_5_seconds(input_audio_path, output_audio_path):
    # Load the input audio file
    audio = AudioSegment.from_file(input_audio_path)

    # Calculate the target duration in milliseconds (5000 milliseconds = 5 seconds)
    target_duration_ms = 5000

    # Check the current duration of the audio
    current_duration_ms = len(audio)

    if current_duration_ms < target_duration_ms:
        # If the input audio is shorter than 5 seconds, pad it with silence
        silence = AudioSegment.silent(duration=target_duration_ms - current_duration_ms)
        audio = audio + silence
    elif current_duration_ms > target_duration_ms:
        # If the input audio is longer than 5 seconds, truncate it
        audio = audio[:target_duration_ms]

    # Export the resulting audio to the output file
    audio.export(output_audio_path, format="wav")

# Specify the input directory containing audio files
input_directory = "/home/ananya/BTP/test/nohorn_unevenlength"  # Replace with your input directory path

# Specify the output directory for the 5-second audio files
output_directory = "/home/ananya/BTP/test/nohorn_5sec"  # Replace with your desired output directory

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List all files in the input directory
audio_files = [f for f in os.listdir(input_directory) if f.endswith(".wav")]

# Process each audio file
for audio_file in audio_files:
    input_audio_path = os.path.join(input_directory, audio_file)
    output_audio_path = os.path.join(output_directory, audio_file)
    convert_audio_to_5_seconds(input_audio_path, output_audio_path)
