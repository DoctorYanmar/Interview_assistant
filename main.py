import time
from dotenv import load_dotenv
from src.audio_capture import AudioCapture
from src.speech_recognizer import SpeechRecognizer
from src.chatgpt_integration import ChatGPTIntegration
import os
import numpy as np
from src.gui import InterviewAssistantGUI
import json
import sys
import platform
from PyQt6.QtWidgets import QApplication


def check_dependencies():
    try:
        import openai
        import sounddevice
        from PyQt6.QtWidgets import QApplication
    except ImportError as e:
        print(f"Ошибка: {e}")
        if platform.system() == "Windows":
            print("Пожалуйста, запустите setup.bat для установки всех зависимостей.")
        else:
            print("Пожалуйста, запустите setup.sh для установки всех зависимостей.")
        sys.exit(1)


def main():
    check_dependencies()
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        print("Ошибка: API ключ OpenAI не найден в файле .env")
        print("Пожалуйста, добавьте ваш API ключ в файл .env")
        sys.exit(1)

    audio_capture = AudioCapture()
    chatgpt = ChatGPTIntegration()
    recognizer = SpeechRecognizer()

    app = QApplication(sys.argv)

    def start_recording():
        settings = window.get_settings()
        audio_capture.device_index = int(settings['audio_device'])
        chatgpt.set_model(settings['model'])
        chatgpt.set_system_prompt(settings['prompt'])
        recognizer.set_language(settings['language'])
        audio_capture.start_recording()
        debug_message = "Запись начата...\n"
        debug_message += f"Используемая модель ChatGPT: {settings['model']}"
        window.update_debug(debug_message)

    def stop_recording():
        audio_capture.stop_recording()
        window.update_debug("Запись остановлена. Обработка аудио...")
        audio_data = audio_capture.get_audio_data()
        if audio_data is not None:
            try:
                audio_bytes = audio_data.tobytes()
                transcript = recognizer.transcribe_audio(audio_bytes)
                window.update_debug(f"Транскрибированный текст: {transcript}")
                window.update_transcription(transcript)

                settings = window.get_settings()
                window.update_debug(
                    f"Отправка запроса к модели ChatGPT: {settings['model']}")
                suggestion = chatgpt.get_response(transcript)
                window.update_debug(f"Подсказка от ChatGPT: {suggestion}")

                window.update_suggestion(suggestion)
            except Exception as e:
                error_message = f"Ошибка во время транскрибации или получения подсказки: {e}"
                print(error_message)
                window.update_debug(error_message)
        else:
            window.update_debug("Аудиоданные не захвачены.")

    window = InterviewAssistantGUI(
        audio_capture, chatgpt, start_recording, stop_recording)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
