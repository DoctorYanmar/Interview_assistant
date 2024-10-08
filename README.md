# Interview Assistant | Помощник для Интервью

<details>
<summary>English</summary>

Interview Assistant is a program that helps during online interviews by providing suggestions based on the interviewer's questions using ChatGPT (OpenAI API).

![Interview Assistant Screenshot](https://i.ibb.co/9pyML37/screenshot.jpg)

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Using the Program](#using-the-program)
- [Important Notes](#important-notes)
- [Troubleshooting](#troubleshooting)
- [Support](#support)
- [Obtaining OpenAI API Key](#obtaining-openai-api-key)
- [License](#license)

## Installation

### Windows

1. Download and extract the program archive. [Release 1.0.0 ver](https://github.com/DoctorYanmar/Interview_assistant/releases/tag/Release)
2. Run `setup.bat` by double-clicking it.
3. Follow the on-screen instructions. The script will install Python 3.10 (if not already installed), create a virtual environment, and install the necessary dependencies.
4. After installation, a browser window will open with the VB-Audio Virtual Cable website. Download and install the program.

### macOS / Linux

1. Download and extract the program archive.
2. Open a terminal in the program folder.
3. Run the command (macOS):
   ```
   chmod +x setup_macos.sh && ./setup_macos.sh
   ```
   Run the command (Linux):
   ```
   chmod +x setup_linux.sh && ./setup_linux.sh
   ```
4. Follow the on-screen instructions. The script will install Python 3.10 (if not already installed), create a virtual environment, and install the necessary dependencies.
5. After installation, a browser window will open with the VB-Audio Virtual Cable website. Download and install the program.

## Configuration

### API Key Setup

1. Open the `.env` file in a text editor.
2. Replace `your_api_key_here` with your OpenAI API key.

### Virtual Audio Output Setup

<details>
<summary>Windows Setup Instructions</summary>

1. **Install Virtual Audio Device:**
   - Download and install [VB-Audio Virtual Cable](https://vb-audio.com/Cable/).
   - Restart your computer.
   - Check for new audio devices: "CABLE Input" and "CABLE Output".

2. **Zoom Setup:**
   - Open Zoom settings.
   - In the "Audio" section, select "CABLE Input (VB-Audio Virtual Cable)" as the speaker.
   - Keep your regular microphone selected.

3. **Windows Audio Settings:**

*Check proper installation of VB-Audio Virtual Cable:* 
   - Open Windows Sound settings (right click on speaker icon -> Sound settings)
   - Under "Output" you should see "CABLE Input" (It means program is installed successfully). Now select your regular Output device.
   - Under "Input" you should see "CABLE Output" (It means program is installed successfully). Now select your regular Input device.

*Sharing the Output signal:*
   - Open Windows Sound settings (right-click on the speaker icon -> Sound settings).
   - Scroll down to the "Advanced sound settings" section and click on "Sound control panel".
   - Go to the "Recording" tab.
   - Find "CABLE Output" in the list and double-click on it.
   - Go to the "Listen" tab.
   - Check the "Listen to this device" box.
   - In the "Play through this device" drop-down list, select your headphones or speakers through which you want to hear the sound (Your usual way of listening to sound).
   - Click "Apply", then "OK".

4. **Test in Zoom:**
   - In Zoom audio settings, test the speaker.
   - You should hear the test sound through your headphones or speakers.

</details>

<details>
<summary>macOS Setup Instructions</summary>

1. **Install Virtual Audio Device:**
   - Download and install [VB-Audio Virtual Cable for macOS](https://vb-audio.com/Cable/).
   - Restart your computer.

2. **Zoom Setup:**
   - In Zoom settings, select "CABLE Input (VB-Audio Virtual Cable)" as the speaker.
   - Keep your regular microphone selected.

3. **macOS Audio Settings:**

*Check proper installation of vb-audio cable:*
   - Open "System Preferences" -> "Sound."
   - In the "Output" tab, select your regular output device (headphones or speakers).
   - In the "Input" tab, make sure your regular microphone is selected.

*Sharing the Output signal:*
   - Open the "Audio MIDI Setup" app (located in Applications -> Utilities).
   - In the menu, select "Show Audio Devices."
   - Find "CABLE Output" in the list of devices and select it.
   - Click the gear icon at the bottom left of the window.
   - Choose "Use This Device for Sound Output."
   - In the popup, select your regular sound output device.

4. **Test in Zoom:**
   - In Zoom settings, test the speaker and microphone.
   - You should hear the test sound through your headphones or speakers.

</details>

## Using the Program

1. Start the program:
   - Windows: Double-click `interview_helper.bat`
   - macOS: Run `interview_helper_macos.sh` (`./interview_helper_macos.sh`)
   - Linux: Run `interview_helper_linux.sh` (`./interview_helper_linux.sh`)

2. In the program window:
   - Select the appropriate audio device (usually "CABLE Output").
   - Choose the ChatGPT model.
   - Write a detailed prompt in the prompt window.
   - Select the language (Russian or English).
   - Click "Save Settings".

3. During the interview:
   - Press "Start Recording" when the interviewer starts asking a question.
   - Press "Stop Recording" when the interviewer finishes.
   - Wait for the suggestion in the "ChatGPT Suggestions" window.

## Important Notes

- Ensure you can access https://openai.com/ in your country, if not, then you cannot send/receive requests from OpenAI API. You need to find solution
- Verify that virtual audio outputs are correctly configured.
- Check that the correct OpenAI API key is specified in the `.env` file.
- If audio issues occur, check your system and Zoom audio settings.
- Be aware of the ethical considerations when using this program during interviews.

## Troubleshooting

- If the program doesn't start, ensure all installation steps were followed correctly.
- For audio capture issues, check virtual audio output settings.
- If ChatGPT suggestions are irrelevant, try changing the model or modifying the prompt.

## Support

If you encounter any problems or have questions, please [create an issue](https://github.com/DoctorYanmar/Interview_assistant/issues) in the project repository on GitHub.

## Obtaining OpenAI API Key

<details>
<summary>Instructions for obtaining an OpenAI API key</summary>

1. Go to the [OpenAI website](https://openai.com/).
2. Sign up or log in to your account.
3. Navigate to the [API keys section](https://platform.openai.com/account/api-keys).
4. Create a new key and save it securely.
5. Paste the key into the `.env` file in the program directory.

**Important:** To use the API, you need to add a payment method to your OpenAI account.

</details>

## License

This project is licensed under the [MIT License](LICENSE.md).

- Interview Assistant uses the OpenAI API, which is subject to the [OpenAI API Terms of Use](https://openai.com/policies/api-terms).
- The program recommends the use of VB-Audio Virtual Cable, which is subject to its [own license terms](https://vb-audio.com/Services/licensing.htm).
- For a full list of dependencies and their respective licenses, please refer to the `requirements.txt` file in this project.

</details>

<details>
<summary>Русский</summary>

Interview Assistant - это программа, которая помогает во время онлайн-интервью, предоставляя подсказки на основе вопросов интервьюера с использованием ChatGPT.

![Скриншот Interview Assistant](https://i.ibb.co/9pyML37/screenshot.jpg)

## Содержание

- [Установка](#установка)
- [Настройка](#настройка)
- [Использование программы](#использование-программы)
- [Важные замечания](#важные-замечания)
- [Устранение неполадок](#устранение-неполадок)
- [Поддержка](#поддержка)
- [Получение API ключа OpenAI](#получение-api-ключа-openai)
- [Лицензия](#лицензия)

## Установка

### Windows

1. Скачайте и распакуйте архив с программой. [Release 1.0.0 ver](https://github.com/DoctorYanmar/Interview_assistant/releases/tag/Release)
2. Запустите `setup.bat`, дважды кликнув на него.
3. Следуйте инструкциям на экране. Скрипт установит Python 3.10 (если его нет), создаст виртуальное окружение и установит необходимые зависимости.
4. После завершения установки откроется браузер с сайтом VB-Audio Virtual Cable. Скачайте и установите эту программу.

### macOS / Linux

1. Скачайте и распакуйте архив с программой.
2. Откройте терминал в папке с программой.
3. Выполните команду (macOS):
   ```
   chmod +x setup_macos.sh && ./setup_macos.sh
   ```
   Выполните команду (Linux):
   ```
   chmod +x setup_linux.sh && ./setup_linux.sh
   ```
4. Следуйте инструкциям на экране. Скрипт установит Python 3.10 (если его нет), создаст виртуальное окружение и установит необходимые зависимости.
5. После завершения установки откроется браузер с сайтом VB-Audio Virtual Cable. Скачайте и установите эту программу.

## Настройка

### Настройка API ключа

1. Откройте файл `.env` в текстовом редакторе.
2. Замените `your_api_key_here` на ваш API ключ OpenAI.

### Настройка виртуальных аудио выходов

<details>
<summary>Инструкции для Windows</summary>

1. **Установка виртуального аудиоустройства:**
   - Скачайте и установите [VB-Audio Virtual Cable](https://vb-audio.com/Cable/).
   - Перезагрузите компьютер.
   - Проверьте установку в настройках звука Windows.

2. **Настройка Zoom:**
   - Откройте настройки Zoom.
   - В разделе "Звук" выберите "CABLE Input (VB-Audio Virtual Cable)" как динамик.
   - Оставьте ваш обычный микрофон в настройках микрофона.

3. **Настройка Windows для прослушивания:**

*Проверьте правильность установки VB-Audio Virtual Cable:*
   - Откройте настройки звука Windows (щелкните правой кнопкой мыши по значку динамика -> Настройки звука)
   - В разделе «Вывод» вы должны увидеть «CABLE Input» (это означает, что программа успешно установлена). Теперь выберите свое обычное устройство вывода.
   - В разделе «Ввод» вы должны увидеть «CABLE Output» (это означает, что программа успешно установлена). Теперь выберите свое обычное устройство ввода.

*Обмен сигналом Вывода:*
   - Откройте настройки звука Windows (щелкните правой кнопкой мыши по значку динамика -> Настройки звука).
   - Прокрутите вниз до раздела «Дополнительные параметры звука» и нажмите «Дополнительные параметры звука».
   - Перейдите на вкладку «Запись».
   - Найдите в списке «CABLE Output» и дважды щелкните по нему.
   - Перейдите на вкладку «Прослушивать».
   - Установите флажок «Прослушивать с данного устройства».
   - В раскрывающемся списке «Воспроизводить с данного устройства» выберите наушники или динамики, через которые вы хотите слышать звук(Ваш обычный способ прослушивания звука). 
   - Нажмите «Применить», затем «ОК».

4. **Проверка в Zoom:**
   - В настройках звука Zoom проверьте динамик.
   - Вы должны услышать тестовый звук через ваши наушники или динамики.

</details>

<details>
<summary>Инструкции для macOS</summary>

1. **Установка виртуального аудиоустройства:**
   - Скачайте и установите [VB-Audio Virtual Cable для macOS](https://vb-audio.com/Cable/).
   - Перезагрузите компьютер.

2. **Настройка Zoom:**
   - В настройках Zoom выберите "CABLE Input (VB-Audio Virtual Cable)" как динамик.
   - Оставьте ваш обычный микрофон в настройках микрофона.

3. **Настройка macOS для прослушивания:**

*Проверьте правильность установки кабеля vb-audio:*
   - Откройте "Системные настройки" -> "Звук".
   - Перейдите на вкладку "Выход" и выберите ваше обычное устройство вывода звука (наушники или динамики).
   - Перейдите на вкладку "Вход".
   - Убедитесь, что выбран ваш обычный микрофон.
   
*Обмен сигналом Вывода:*
   - Откройте приложение "Аудио MIDI Setup" (находится в папке "Программы" -> "Утилиты").
   - В меню "Окно" выберите "Показать окно аудиоустройств".
   - Найдите в списке устройств "CABLE Output" и выберите его.
   - Нажмите на кнопку с изображением шестеренки в нижнем левом углу окна.
   - Выберите "Использовать это устройство для вывода звука".
   - В появившемся диалоговом окне выберите ваше обычное устройство вывода звука.


4. **Проверка в Zoom:**
   - В настройках Zoom проверьте динамик и микрофон.
   - Вы должны услышать тестовый звук через ваши наушники или динамики.

</details>

## Использование программы

1. Запустите программу:
   - Windows: Дважды кликните на `interview_helper.bat`
   - macOS: Запустите `interview_helper_macos.sh` (`./interview_helper_macos.sh`)
   - Linux: Запустите `interview_helper_linux.sh` (`./interview_helper_linux.sh`)

2. В открывшемся окне программы:
   - Выберите нужное аудиоустройство (обычно "CABLE Output").
   - Выберите модель ChatGPT.
   - Напишите промпт в окне промпта.
   - Выберите язык (русский или английский).
   - Нажмите "Save Settings".

3. Во время интервью:
   - Нажмите "Start Recording", когда интервьюер начнет задавать вопрос.
   - Нажмите "Stop Recording", когда интервьюер закончит вопрос.
   - Ожидайте подсказку в окне "ChatGPT Suggestions".

## Важные замечания

- Убедитесь, что вы можете открыть https://openai.com/ в вашей стране, если нет, то вы не cможете отправлять/получать запросы от OpenAI API. Вам нужно найти решение
- Проверьте правильность настройки виртуальных аудио выходов.
- Убедитесь, что в файле `.env` указан правильный API ключ OpenAI.
- Проверьте настройки звука в системе и в Zoom при проблемах с аудио.
- Помните об этических аспектах использования такой программы во время интервью.

## Устранение неполадок

- Если программа не запускается, проверьте правильность установки.
- При проблемах с захватом звука, проверьте настройки виртуальных аудио выходов.
- Если ChatGPT дает нерелевантные подсказки, попробуйте изменить модель или промпт.

## Поддержка

Если у вас возникли проблемы или вопросы, пожалуйста, [создайте issue](https://github.com/DoctorYanmar/Interview_assistant/issues) в репозитории проекта на GitHub.

## Получение API ключа OpenAI

<details>
<summary>Инструкции по получению API ключа OpenAI</summary>

1. Перейдите на [сайт OpenAI](https://openai.com/).
2. Зарегистрируйтесь или войдите в аккаунт.
3. Перейдите в раздел [API keys](https://platform.openai.com/account/api-keys).
4. Создайте новый ключ и сохраните его.
5. Вставьте ключ в файл `.env` в директории программы.

**Важно:** Для использования API необходимо привязать способ оплаты к вашему аккаунту OpenAI.

</details>

## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE.md).

- Interview Assistant использует API OpenAI, который подчиняется [Условиям использования API OpenAI](https://openai.com/policies/api-terms).
- Программа рекомендует использовать VB-Audio Virtual Cable, который подчиняется [собственным условиям лицензии](https://vb-audio.com/Services/licensing.htm).
- Полный список зависимостей и соответствующих им лицензий см. в файле `requirements.txt` в этом проекте.

</details>