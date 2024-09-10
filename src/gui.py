import sys
import json
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QTextEdit, QComboBox, QLabel, QFrame, QScrollArea, QSplitter,
                             QDialog)
from PyQt6.QtCore import Qt, QSize
from src.hotkey_handler import HotkeyHandler


class HotkeyInfoDialog(QDialog):
    def __init__(self, hotkey_info, parent=None):
        super().__init__(parent)
        self.setWindowTitle("HotKey Buttons")
        self.setMinimumSize(300, 200)

        layout = QVBoxLayout(self)

        for shortcut, description in hotkey_info:
            layout.addWidget(QLabel(f"{shortcut}: {description}"))

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)


class InterviewAssistantGUI(QMainWindow):
    def __init__(self, audio_capture, chatgpt, start_recording_callback, stop_recording_callback):
        super().__init__()
        self.audio_capture = audio_capture
        self.chatgpt = chatgpt
        self.start_recording_callback = start_recording_callback
        self.stop_recording_callback = stop_recording_callback

        self.setWindowTitle("Interview Assistant")
        self.setGeometry(100, 100, 800, 900)
        self.setMinimumSize(300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Инициализация обработчика горячих клавиш
        self.hotkey_handler = HotkeyHandler(self)

        self.create_widgets()
        self.load_settings()

    def create_widgets(self):
        # Prompt frame
        prompt_frame = QFrame()
        prompt_frame.setFrameStyle(
            QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        prompt_layout = QVBoxLayout(prompt_frame)
        prompt_layout.addWidget(QLabel("ChatGPT Prompt"))
        self.prompt_entry = QTextEdit()
        self.prompt_entry.setMinimumHeight(150)
        prompt_layout.addWidget(self.prompt_entry)
        self.main_layout.addWidget(prompt_frame)

        # Model selection
        model_frame = QFrame()
        model_frame.setFrameStyle(
            QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        model_layout = QVBoxLayout(model_frame)
        model_layout.addWidget(QLabel("ChatGPT Model"))
        self.model_entry = QComboBox()
        self.model_entry.setEditable(True)
        model_layout.addWidget(self.model_entry)
        self.main_layout.addWidget(model_frame)

        # Language selection
        language_frame = QFrame()
        language_frame.setFrameStyle(
            QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        language_layout = QVBoxLayout(language_frame)
        language_layout.addWidget(QLabel("Language"))
        self.language_combobox = QComboBox()
        self.language_combobox.addItems(["en", "ru"])
        language_layout.addWidget(self.language_combobox)
        self.main_layout.addWidget(language_frame)

        # Audio device selection
        device_frame = QFrame()
        device_frame.setFrameStyle(
            QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        device_layout = QVBoxLayout(device_frame)
        device_layout.addWidget(QLabel("Audio Device"))
        self.device_combobox = QComboBox()
        device_layout.addWidget(self.device_combobox)
        self.main_layout.addWidget(device_frame)
        self.update_audio_devices()

        # Control buttons
        control_frame = QFrame()
        control_layout = QHBoxLayout(control_frame)
        self.record_button = QPushButton("Start Recording")
        self.record_button.clicked.connect(self.toggle_recording)
        control_layout.addWidget(self.record_button)
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_all)
        control_layout.addWidget(self.clear_button)
        self.save_button = QPushButton("Save Settings")
        self.save_button.clicked.connect(self.save_settings)
        control_layout.addWidget(self.save_button)
        self.hotkey_info_button = QPushButton("HotKey Buttons")
        self.hotkey_info_button.clicked.connect(self.show_hotkey_info)
        control_layout.addWidget(self.hotkey_info_button)
        self.main_layout.addWidget(control_frame)

        # Create a splitter for the bottom part
        splitter = QSplitter(Qt.Orientation.Vertical)

        # Transcription display
        transcription_frame = QFrame()
        transcription_frame.setFrameStyle(
            QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        transcription_layout = QVBoxLayout(transcription_frame)
        transcription_layout.addWidget(QLabel("Transcription"))
        self.transcription_text = QTextEdit()
        self.transcription_text.setReadOnly(True)
        transcription_layout.addWidget(self.transcription_text)
        splitter.addWidget(transcription_frame)

        # ChatGPT Suggestions display
        suggestions_frame = QFrame()
        suggestions_frame.setFrameStyle(
            QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        suggestions_layout = QVBoxLayout(suggestions_frame)
        suggestions_layout.addWidget(QLabel("ChatGPT Suggestions"))
        self.suggestions_text = QTextEdit()
        self.suggestions_text.setReadOnly(True)
        suggestions_layout.addWidget(self.suggestions_text)
        splitter.addWidget(suggestions_frame)

        # Debug messages display
        debug_frame = QFrame()
        debug_frame.setFrameStyle(
            QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        debug_layout = QVBoxLayout(debug_frame)
        debug_layout.addWidget(QLabel("Debug Messages"))
        self.debug_text = QTextEdit()
        self.debug_text.setReadOnly(True)
        debug_layout.addWidget(self.debug_text)
        splitter.addWidget(debug_frame)

        # Set initial sizes for splitter
        splitter.setSizes([100, 500, 100])  # Suggestions gets the most space

        self.main_layout.addWidget(splitter)

    def show_hotkey_info(self):
        dialog = HotkeyInfoDialog(
            self.hotkey_handler.get_shortcut_info(), self)
        dialog.exec()

    def update_audio_devices(self):
        devices = self.audio_capture.list_audio_devices()
        device_list = [
            f"{device['id']} - {device['name']} (API: {device['host_api']}, Ch: {device['max_input_channels']}, SR: {device['default_samplerate']})" for device in devices]
        self.device_combobox.clear()
        self.device_combobox.addItems(device_list)

    def toggle_recording(self):
        if self.record_button.text() == "Start Recording":
            self.start_recording_callback()
            self.record_button.setText("Stop Recording")
        else:
            self.stop_recording_callback()
            self.record_button.setText("Start Recording")

    def clear_all(self):
        self.transcription_text.clear()
        self.suggestions_text.clear()
        self.debug_text.clear()

    def update_transcription(self, text):
        self.transcription_text.setPlainText(text)

    def update_suggestion(self, text):
        self.suggestions_text.setPlainText(text)

    def update_debug(self, text):
        self.debug_text.append(text)
        self.debug_text.verticalScrollBar().setValue(
            self.debug_text.verticalScrollBar().maximum())

    def save_settings(self):
        settings = {
            "prompt": self.prompt_entry.toPlainText().strip(),
            "model": self.model_entry.currentText(),
            "audio_device": self.device_combobox.currentText(),
            "language": self.language_combobox.currentText()
        }
        with open("settings.json", "w") as f:
            json.dump(settings, f)

    def load_settings(self):
        if os.path.exists("settings.json"):
            with open("settings.json", "r") as f:
                settings = json.load(f)
            self.prompt_entry.setPlainText(settings.get("prompt", ""))
            self.model_entry.setCurrentText(settings.get("model", ""))
            index = self.device_combobox.findText(settings.get(
                "audio_device", ""), Qt.MatchFlag.MatchContains)
            if index >= 0:
                self.device_combobox.setCurrentIndex(index)
            index = self.language_combobox.findText(
                settings.get("language", "en"))
            if index >= 0:
                self.language_combobox.setCurrentIndex(index)
        else:
            # Set default values if settings.json doesn't exist
            default_prompt = "You are an assistant providing brief hints for interview questions. Offer minimal key words or phrases to guide the person in answering, but not give a full answer. The hint should be short, no more than 2-3 words or a brief phrase. Format the response as a bulleted list."
            default_model = "gpt-4o-mini-2024-07-18"
            self.prompt_entry.setPlainText(default_prompt)
            self.model_entry.setCurrentText(default_model)

    def get_settings(self):
        return {
            "prompt": self.prompt_entry.toPlainText().strip(),
            "model": self.model_entry.currentText(),
            "audio_device": self.device_combobox.currentText().split(" - ")[0],
            "language": self.language_combobox.currentText()
        }

    def sizeHint(self):
        return QSize(800, 900)
