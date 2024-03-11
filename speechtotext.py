import speech_recognition

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0)
            audio = recognizer.listen(mic)
            print("Processing...")
            text = recognizer.recognize_google(audio)

            text = text.lower()

            print(f"Recognized: {text}")
    except speech_recognition.WaitTimeoutError:
        print("Listening timed out.")
        continue
    except speech_recognition.UnknownValueError as e:
        print("Could not understand audio: ", str(e))
        continue
    except Exception as e:
        print("Error:", str(e))
        continue
