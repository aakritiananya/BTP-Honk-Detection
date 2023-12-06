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

# Example usage:
input_audio_path = "/home/ananya/BTP/test/1.wav"  # Replace with your input audio file
output_audio_path = "/home/ananya/BTP/test/1_output.wav"  # Output audio file with a fixed 5-second duration
convert_audio_to_5_seconds(input_audio_path, output_audio_path)
