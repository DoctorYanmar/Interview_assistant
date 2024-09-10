**Interview Assistant**

Interview Assistant is a program that helps during online interviews by providing suggestions based on the interviewer's questions using ChatGPT.

### Installation

#### Windows

1. Download and extract the program archive.
2. Run `setup.bat` by double-clicking it.
3. Follow the on-screen instructions. The script will install Python 3.10 (if not already installed), create a virtual environment, and install the necessary dependencies.
4. After installation, a browser window will open with the VB-Audio Virtual Cable website. Download and install the program.

#### macOS / Linux

1. Download and extract the program archive.
2. Open a terminal in the program folder.
3. Run the command (macOS): `chmod +x setup_macos.sh && ./setup_macos.sh`
4. Run the command (Linux): `chmod +x setup_linux.sh && ./setup_linux.sh`
5. Follow the on-screen instructions. The script will install Python 3.10 (if not already installed), create a virtual environment, and install the necessary dependencies.
6. After installation, a browser window will open with the VB-Audio Virtual Cable website. Download and install the program.

### Configuration

#### API Key Setup

1. Open the `.env` file in a text editor.
2. Replace `your_api_key_here` with your OpenAI API key.

#### Virtual Audio Output Setup

##### Windows

###### Step 1: Install Virtual Audio Device

1. Download and install VB-Audio Virtual Cable from the official website: [https://vb-audio.com/Cable/](https://vb-audio.com/Cable/)
2. Restart your computer to ensure all drivers are properly installed.
3. After restarting, you should see a new audio device named "CABLE Input" and "CABLE Output." These are two ends of the virtual cable.

###### Step 2: Zoom Setup

1. Open Zoom and log into your account.
2. Click the gear icon in the top-right corner to open the settings.
3. From the left menu, select "Audio."
4. In the "Speaker" section, select "CABLE Input (VB-Audio Virtual Cable)."
5. In the "Microphone" section, keep your regular microphone selected.

###### Step 3: Windows Audio Settings

1. Open Windows sound settings (right-click the speaker icon -> Sound Settings).
2. Scroll down to "Advanced Sound Options" and click "Sound Control Panel."
3. Go to the "Recording" tab.
4. Find "CABLE Output" in the list and double-click it.
5. Switch to the "Listen" tab.
6. Check the box for "Listen to this device."
7. In the dropdown "Playback through this device," select your headphones or speakers.
8. Click "Apply" and then "OK."

###### Step 4: Zoom Audio Test

1. Go back to Zoom settings.
2. In the "Speaker" section, click "Test Speaker."
3. You should hear the test sound through your headphones or speakers.

##### macOS

###### Step 1: Install Virtual Audio Device

1. Download and install VB-Audio Virtual Cable for macOS from the official website: [https://vb-audio.com/Cable/](https://vb-audio.com/Cable/)
2. Restart your computer.

###### Step 2: Zoom Setup

1. Open Zoom and go to settings (zoom.us -> Settings).
2. Select the "Audio" tab.
3. In the "Speaker" section, select "CABLE Input (VB-Audio Virtual Cable)."
4. In the "Microphone" section, keep your regular microphone selected.

###### Step 3: macOS Audio Settings

1. Open "System Preferences" -> "Sound."
2. In the "Output" tab, select your regular output device (headphones or speakers).
3. In the "Input" tab, make sure your regular microphone is selected.

###### Step 4: Audio Listening Setup

1. Open the "Audio MIDI Setup" app (located in Applications -> Utilities).
2. In the menu, select "Show Audio Devices."
3. Find "CABLE Output" in the list of devices and select it.
4. Click the gear icon at the bottom left of the window.
5. Choose "Use This Device for Sound Output."
6. In the popup, select your regular sound output device.

###### Step 5: Zoom Audio Test

1. Go back to Zoom settings.
2. Click "Test Speaker and Microphone."
3. You should hear the test sound through your headphones or speakers.

**If you don’t hear the sound or the program isn’t capturing audio, double-check your system and Zoom audio settings. Ensure that all devices are correctly selected and volume levels are set appropriately.**

### Using the Program

To start the program:

- Windows: double click on interview_helper.bat
- macOS: Run interview_helper_macos.sh (in terminal: ./interview_helper_macos.sh)
- Linux: Run interview_helper_linux.sh (in terminal: ./interview_helper_linux.sh)

In the program window:

1. Select the appropriate audio device (usually "CABLE Output").
2. Choose the ChatGPT model (e.g., "gpt-4o-mini").
3. Write a detailed prompt in the prompt window (the default settings include a sample prompt you can use as a template).
4. Select the language (Russian or English).
6. Push Save Settings button for correct work of program further.

When the interviewer starts asking a question, press "Start Recording."  
Once the interviewer finishes, press "Stop Recording" (same button as "Start Recording").  
The program will process the audio, convert it to text, and send a query to ChatGPT.  
In the "ChatGPT Suggestions" window, you will see a prompt to help answer the question.

### Important Notes

- Ensure you can run "virtual network" if [ChatGPT](https://openai.com/) page is not opening in your country
- Ensure you have properly configured virtual audio outputs before using the program.
- Verify that the correct OpenAI API key is specified in the `.env` file.
- If you don’t hear the audio or the program isn’t capturing sound, check your system and Zoom audio settings.
- Remember that using such a program may be unethical in certain situations. Make sure you are not violating interview rules.

### Troubleshooting

- **Program doesn’t start**: Make sure all installation steps were followed.
- **Audio capture not working**: Check virtual audio output settings.
- **Speech recognition issues**: Try speaking more clearly and slowly.
- **ChatGPT suggestions are irrelevant**: Try changing the model or modifying the prompt in the program settings.

### Support

If you encounter any problems or have questions, please create an issue in the project repository on GitHub.


### Obtaining OpenAI API Key
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