from PyQt6.QtGui import QShortcut, QKeySequence


class HotkeyHandler:
    def __init__(self, main_window):
        self.main_window = main_window
        self.setup_shortcuts()

    def setup_shortcuts(self):
        # Горячая клавиша для начала/остановки записи (Ctrl+R)
        self.toggle_recording_shortcut = QShortcut(
            QKeySequence("Ctrl+R"), self.main_window)
        self.toggle_recording_shortcut.activated.connect(
            self.main_window.toggle_recording)

        # Горячая клавиша для очистки всех полей (Ctrl+L)
        self.clear_all_shortcut = QShortcut(
            QKeySequence("Ctrl+L"), self.main_window)
        self.clear_all_shortcut.activated.connect(self.main_window.clear_all)

        # Горячая клавиша для сохранения настроек (Ctrl+S)
        self.save_settings_shortcut = QShortcut(
            QKeySequence("Ctrl+S"), self.main_window)
        self.save_settings_shortcut.activated.connect(
            self.main_window.save_settings)

    def get_shortcut_info(self):
        return [
            ("Ctrl+R", "Toggle Recording"),
            ("Ctrl+L", "Clear All Fields"),
            ("Ctrl+S", "Save Settings")
        ]
