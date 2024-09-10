# Interview Assistant

Interview Assistant is a program that helps during online interviews by providing suggestions based on the interviewer's questions using ChatGPT.

![Interview Assistant Screenshot](https://ibb.co/C8QLYRC)

## Table of Contents

- [Installation](#installation)
  - [Windows](#windows)
  - [macOS / Linux](#macos--linux)
- [Configuration](#configuration)
  - [API Key Setup](#api-key-setup)
  - [Virtual Audio Output Setup](#virtual-audio-output-setup)
    - [Windows](#windows-1)
    - [macOS](#macos)
- [Using the Program](#using-the-program)
- [Important Notes](#important-notes)
- [Troubleshooting](#troubleshooting)
- [Support](#support)
- [Obtaining OpenAI API Key](#obtaining-openai-api-key)
- [License](#license)

## Installation

### Windows

1. Download and extract the program archive.
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

#### Windows

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
   - Open Sound Control Panel.
   - Set up "Listen to this device" for "CABLE Output".
   - Select your headphones or speakers as the playback device.

4. **Test in Zoom:**
   - In Zoom audio settings, test the speaker.
   - You should hear the test sound through your headphones or speakers.

</details>

#### macOS

<details>
<summary>macOS Setup Instructions</summary>

1. **Install Virtual Audio Device:**
   - Download and install [VB-Audio Virtual Cable for macOS](https://vb-audio.com/Cable/).
   - Restart your computer.

2. **Zoom Setup:**
   - In Zoom settings, select "CABLE Input (VB-Audio Virtual Cable)" as the speaker.
   - Keep your regular microphone selected.

3. **macOS Audio Settings:**
   - Set your regular output device in System Preferences.
   - Configure "CABLE Output" in Audio MIDI Setup.

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

- Ensure you can access https://openai.com/ in your country.
- Verify that virtual audio outputs are correctly configured.
- Check that the correct OpenAI API key is specified in the `.env` file.
- If audio issues occur, check your system and Zoom audio settings.
- Be aware of the ethical considerations when using this program during interviews.

## Troubleshooting

- If the program doesn't start, ensure all installation steps were followed correctly.
- For audio capture issues, check virtual audio output settings.
- To improve speech recognition, speak clearly and slowly.
- If ChatGPT suggestions are irrelevant, try changing the model or modifying the prompt.

## Support

If you encounter any problems or have questions, please [create an issue](link_to_your_repository/issues) in the project repository on GitHub.

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
To use this program, you need an OpenAI API key. Follow these steps to obtain one:

Go to the OpenAI website: https://openai.com/
Click "Sign up" (if you don't have an account) or "Log in" (if you already have an account).
Once logged in, navigate to the API section: https://platform.openai.com/account/api-keys
Click the "Create new secret key" button.
Copy the generated key (it's important to save it as it's only shown once).
Paste this key into the .env file in the program directory, replacing your_api_key_here with your actual key.

Important: To use the API key, you need to add a payment method to your OpenAI account. After any free trial period (if offered) ends, API usage will be billed according to OpenAI's current pricing.
Note: Keep your API key secure and do not share it with others. Using the API may result in financial charges, so monitor your usage and set up spending limits in your OpenAI account 


##License

This project is licensed under the MIT License - see the LICENSE.md file for details.
Interview assistan uses the OpenAI API, which is subject to the OpenAI API Terms of Use.
This software recommends the use of VB-Audio Virtual Cable, which is subject to its own license terms. For more information, visit: https://vb-audio.com/Cable/
For a full list of dependencies and their respective licenses, please refer to the requirements.txt file in this project.