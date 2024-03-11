# Speech Recognition Program

This Python program uses the SpeechRecognition library to transcribe speech from a microphone using Google's Web Speech API.

## Requirements

- Python 3.x
- SpeechRecognition library
- PyAudio library (dependency of SpeechRecognition for microphone input)
- Google Cloud Speech-to-Text API credentials (if using the `recognize_google_cloud` method)

## Installation

1. Clone the repository or download the Python script.
2. Install the required libraries using pip:
3. Set up Google Cloud Speech-to-Text API credentials if using the `recognize_google_cloud` method. Follow the instructions [here](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries#client-libraries-usage-python).

## Usage

1. Run the Python script `speech_recognition.py`.
2. Make sure your microphone is connected and accessible by your computer.
3. Speak into the microphone, and the program will transcribe the speech in real-time.
4. The transcribed text will be displayed in the console.

## Troubleshooting

- If the program doesn't work, make sure your microphone is properly connected and accessible by your computer.
- If you encounter issues with the Google Cloud Speech-to-Text API, double-check your API credentials and configuration.



