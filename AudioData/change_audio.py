import os
import numpy as np
import wave
import struct

# Set the parameters for the extended audio files
target_duration = 3  # Target duration in seconds
sample_rate = 44100  # Samples per second
amplitude = 16000  # Amplitude of the audio signal

# Input and output directories
input_dir = '/home/mehul/Desktop/BTP/audio'
output_dir = '/home/mehul/Desktop/BTP/audio2'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to extend an audio file
def extend_audio(input_file, output_file):
    with wave.open(input_file, 'rb') as wf:
        num_channels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        original_sample_rate = wf.getframerate()
        original_duration = wf.getnframes() / original_sample_rate
        num_samples_needed = int(target_duration * sample_rate)

        # Read the audio data from the input file
        audio_data = wf.readframes(-1)
        audio_data = np.frombuffer(audio_data, dtype=np.int16)

        # Extend or truncate the audio data to the target duration
        if len(audio_data) < num_samples_needed:
            # If the audio is shorter, fill the remaining with zeros
            extended_audio = np.concatenate((audio_data,
np.zeros(num_samples_needed - len(audio_data))))
        else:
            # If the audio is longer, truncate it to the target duration
            extended_audio = audio_data[:num_samples_needed]

        # Create a new WAV file with the extended audio
        with wave.open(output_file, 'wb') as output_wf:
            output_wf.setnchannels(num_channels)
            output_wf.setsampwidth(sample_width)
            output_wf.setframerate(sample_rate)
            for value in extended_audio:
                packed_value = struct.pack('h', int(value))
                output_wf.writeframes(packed_value)

# Process all audio files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.wav'):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename)
        extend_audio(input_file, output_file)

print(f"Audio files extended and saved in '{output_dir}'.")
