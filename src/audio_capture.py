import sounddevice as sd
import numpy as np
import wave
import os
import threading
import time


class AudioCapture:
    def __init__(self, device_index=None, rate=16000, channels=1):
        self.device_index = device_index
        self.rate = rate
        self.channels = channels
        self.stream = None
        self.audio_buffer = []
        self.is_recording = False
        self.recording_thread = None
        self.max_seconds = 300  # Увеличено до 5 минут (300 секунд)
        self.start_time = None
        self.max_buffer_size = self.rate * self.max_seconds  # Максимальный размер буфера

    def start_recording(self):
        try:
            self.audio_buffer = []
            self.is_recording = True
            self.start_time = time.time()
            self.recording_thread = threading.Thread(target=self._record)
            self.recording_thread.start()
            print("Debug: Recording started successfully")
        except Exception as e:
            print(f"Debug: Error starting recording: {str(e)}")

    def stop_recording(self):
        self.is_recording = False
        if self.recording_thread:
            self.recording_thread.join()
        print(
            f"Debug: Recording stopped. Captured {len(self.audio_buffer)} audio chunks")

    def _record(self):
        chunk_size = 1024
        with sd.InputStream(device=self.device_index, channels=self.channels, samplerate=self.rate, dtype='int16') as stream:
            while self.is_recording and (time.time() - self.start_time) < self.max_seconds:
                audio_chunk, overflowed = stream.read(chunk_size)
                if overflowed:
                    print("Debug: Input overflow")
                self.audio_buffer.append(audio_chunk)

                # Проверка на превышение максимального размера буфера
                total_samples = sum(len(chunk) for chunk in self.audio_buffer)
                if total_samples >= self.max_buffer_size:
                    print(
                        f"Debug: Maximum buffer size reached ({self.max_seconds} seconds)")
                    self.is_recording = False
                    break

            if (time.time() - self.start_time) >= self.max_seconds:
                print(
                    f"Debug: Maximum recording time of {self.max_seconds} seconds reached")

    def get_audio_data(self):
        if self.audio_buffer:
            total_samples = sum(len(chunk) for chunk in self.audio_buffer)
            print(f"Debug: Total samples: {total_samples}")
            return np.concatenate(self.audio_buffer)
        else:
            print("Debug: No audio data captured")
            return None

    def save_audio_to_file(self, filename="debug_audio.wav"):
        if not self.audio_buffer:
            print("Debug: No audio data to save")
            return

        try:
            audio_data = np.concatenate(self.audio_buffer)
            with wave.open(filename, 'wb') as wf:
                wf.setnchannels(self.channels)
                wf.setsampwidth(2)  # 16-bit audio
                wf.setframerate(self.rate)
                wf.writeframes(audio_data.tobytes())

            print(f"Debug: Audio saved to {filename}")
            file_size = os.path.getsize(filename)
            print(f"Debug: File size: {file_size} bytes")

            # Print audio data information
            total_samples = len(audio_data)
            duration = total_samples / self.rate
            print(f"Debug: Total samples: {total_samples}")
            print(f"Debug: Audio duration: {duration:.2f} seconds")
        except Exception as e:
            print(f"Debug: Error saving audio to file: {str(e)}")

    def list_audio_devices(self):
        devices = sd.query_devices()
        input_devices = []
        seen_devices = set()
        for i, device in enumerate(devices):
            if device['max_input_channels'] > 0:
                device_info = {
                    "id": i,
                    "name": device['name'],
                    "host_api": device['hostapi'],
                    "max_input_channels": device['max_input_channels'],
                    "default_samplerate": device['default_samplerate']
                }
                device_key = f"{device['name']}_{device['hostapi']}_{device['max_input_channels']}_{device['default_samplerate']}"
                if device_key not in seen_devices:
                    input_devices.append(device_info)
                    seen_devices.add(device_key)
                    print(
                        f"Input Device id {i} - {device['name']} (Host API: {device['hostapi']}, Channels: {device['max_input_channels']}, Sample Rate: {device['default_samplerate']})")
        return input_devices

    def __del__(self):
        self.is_recording = False
        if self.recording_thread:
            self.recording_thread.join()


if __name__ == "__main__":
    capture = AudioCapture()
    capture.list_audio_devices()
