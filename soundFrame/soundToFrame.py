import wave

def soundtoFrame(soundFile, framesFile):
    # Sample rate
    framerate = 44100  # 44.1 KHz

    # Open the audio file
    soundFile = wave.open(soundFile, 'r')
    soundFile.setframerate(framerate)  # Set the sample rate

    # Get audio parameters
    nframes = soundFile.getnframes()

    # Read audio data as bytes
    frames = soundFile.readframes(nframes)

    # Close the audio file
    soundFile.close()

    # Open the output file in write mode
    with open(framesFile, 'wb') as outputFile:
        # Write each byte of the audio data to the output file
        outputFile.write(frames)

# Input audio file name
soundFile = "audio.wav"

# Output raw format file name
framesFile = "frameFile.txt"

# Convert the audio file to raw format
audio_a_crudo(soundFile, framesFile)

print(f"El archivo de audio '{soundFile}' ha sido convertido a formato crudo en '{framesFile}'")