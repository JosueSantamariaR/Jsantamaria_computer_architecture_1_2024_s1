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
