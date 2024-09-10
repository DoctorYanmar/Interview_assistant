import os
import tempfile
import wave
import openai


class SpeechRecognizer:
    def __init__(self, language="en"):
        self.language = language
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")

    def set_language(self, language):
        self.language = language

    def save_audio(self, audio_data, sample_rate=16000, sample_width=2, channels=1):
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            with wave.open(temp_file.name, 'wb') as wf:
                wf.setnchannels(channels)
                wf.setsampwidth(sample_width)
                wf.setframerate(sample_rate)
                wf.writeframes(audio_data)
            return temp_file.name

    def transcribe_audio(self, audio_data):
        temp_file_name = self.save_audio(audio_data)
        try:
            return self.transcribe_with_api(temp_file_name)
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return ""
        finally:
            os.remove(temp_file_name)

    def transcribe_with_api(self, file_name):
        with open(file_name, "rb") as audio_file:
            transcript = openai.Audio.transcribe(
                "whisper-1", audio_file, language=self.language)
        return transcript["text"]

    def transcribe_stream(self, audio_generator):
        buffer = b""
        for audio_data in audio_generator:
            buffer += audio_data
            if len(buffer) >= 32000:  # Approximately 2 seconds of audio at 16kHz
                yield self.transcribe_audio(buffer)
                buffer = b""
        if buffer:
            yield self.transcribe_audio(buffer)


if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    # Example usage:
    # audio_data = b"..." # Your audio data here
    # text = recognizer.transcribe_audio(audio_data)
    # print(f"Transcribed: {text}")
