import wave

def frametoSound(framesFile, soundFile):
    # Sample rate
    framerate = 44100  # 44.1 KHz

    # Open the frames file in read mode
    with open(framesFile, 'rb') as framesFile:
        # Read the frames from the frames file
        frames = framesFile.read()

    # Open the output audio file in write mode
    with wave.open(soundFile, 'wb') as audio_output:
        audio_output.setnchannels(1)  # Mono
        audio_output.setsampwidth(1)   # 8-bit
        audio_output.setframerate(framerate)
        audio_output.writeframes(frames)

# Input frames file name
framesFile = "frameFile.txt"

# Output audio file name
soundFile = "audio_reconstructed.wav"

# Convert the frames file to audio
frames_to_sound(framesFile, soundFile)

print(f"The frames file '{framesFile}' has been converted to audio format in '{soundFile}'")


"""
import soundfile as sf
import numpy as np

# Define sampling rate
sampling_rate = 44100

# Open audio file
audio_file = sf.read("audio.wav")

# Get audio signal
audio_data = audio_file[0]

# Validate audio duration (at least 10 seconds)
audio_duration = len(audio_data) / sampling_rate
if audio_duration < 10:
    print("Audio must be at least 10 seconds long.")
    exit()

# Convert data to raw byte format
raw_data = np.array(audio_data * 128, dtype=np.uint8)

# Save data to raw text file
with open("audio_raw.txt", "wb") as text_file:
    text_file.write(raw_data)

print("Audio file successfully converted to raw format (.txt)!")

"""