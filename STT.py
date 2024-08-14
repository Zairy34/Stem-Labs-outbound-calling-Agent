import pyaudio
import numpy as np
from faster_whisper import WhisperModel
import threading
import queue
import time
import wave
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from soundplayer import *




def is_speech(data, threshold=5000):   # Voice Activity Detection (VAD) function
    audio_data = np.frombuffer(data, dtype= np.int16)   # Convert byte data to numpy array
    energy = np.sum(np.abs(audio_data))  # Calculate energy
    return energy > threshold

# Audio capture and processing class
class LiveSTT:
    def __init__(self, model_name="base", record_seconds=10, device_index=1):
        self.model = WhisperModel(model_name)
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2 # steror
        self.RATE = 44100  # Sample rate
        self.CHUNK = 1024  # Buffer size
        self.RECORD_SECONDS = record_seconds
        self.device_index = device_index
        
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.FORMAT,
                                      channels=self.CHANNELS,
                                      rate=self.RATE,
                                      input=True,
                                      input_device_index=self.device_index,
                                      frames_per_buffer=self.CHUNK)
        self.queue = queue.Queue()

    def capture_audio(self):
        while True:
            data = self.stream.read(self.CHUNK)
            if is_speech(data):
                self.queue.put(data)
            else:
                if not self.queue.empty():
                    audio_chunks = []
                    while not self.queue.empty():
                        audio_chunks.append(self.queue.get())
                    if audio_chunks:
                        self.transcribe_audio(b''.join(audio_chunks))

    def transcribe_audio(self, audio_data):
        #print("Transcribing...")
        # Save audio data to temporary file
        temp_filename = "temp.wav"
        with wave.open(temp_filename, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(audio_data)
        segments = None  
        try:
            segments, _ = self.model.transcribe(temp_filename,
                                                vad_filter=True,
                                                vad_parameters=dict(min_silence_duration_ms=500))
            if not segments:
                print("No speech detected.")
            else:
                for segment in segments:
                    print(segment.text)
                    
                    
        except Exception as e:
            #print(f"Error during transcription: {e}")
            pass
        finally:
            os.remove(temp_filename)
        
        if not segments:  # Check if segments are empty
            #print("No speech detected.")
            pass
            return
        
        

    def run(self):
        
            capture_thread = threading.Thread(target=self.capture_audio)
            capture_thread.start()
            print("Live STT system is running...")  

if __name__ == "__main__":
    live_stt = LiveSTT()
    live_stt.run()
    path_mp3file = r'D:\Artificial-intelligance\Challanges\UI\Voiceovers'
    obj = SoundInit(path_mp3file)
    obj.run()