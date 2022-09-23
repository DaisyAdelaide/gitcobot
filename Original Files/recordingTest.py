###############################################################################
#   Script to record audio for an arbitrary time (until keyboard interrupt).
#   Source:
#   https://roytuts.com/python-voice-recording-through-microphone-for-arbitrary-time-using-pyaudio/#:~:text=To%20use%20PyAudio%2C%20first%20we,PyAudio.
#
#   Modified to call speech recognition script once audio file has been saved
###############################################################################

import pyaudio
import wave
import srTest
import action

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Overwrites file each time script runs
filename = 'output.wav'

def record():

    # Instantiates pyaudio to set up portaudio system
    p = pyaudio.PyAudio()

    # Set up a stream to record audio
    stream = p.open(format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK)

    print("Start recording")

    frames = []

    # Read audio data from stream until interrupted
    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Done recording")
    except Exception as e:
        print(str(e))

    sample_width = p.get_sample_size(FORMAT)

    # Pause recording, terminate stream, and terminate portaudio session
    stream.stop_stream()
    stream.close()
    p.terminate()

    return sample_width, frames

def record_to_file(file_path):
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    sample_width, frames = record()
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


print('#' * 80)
print("Please speak into the microphone")
print('Press Ctrl+C to stop the recording')

record_to_file(filename)
print("Result written to " + filename)
print('#' * 80)

srTest.toText(filename)
action.write_file_2()
