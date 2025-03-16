from speech_recognition import SpeechRecognizer, Microphone

def main():
    recognizer = SpeechRecognizer()
    
    with Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except Exception as e:
            print("Could not understand audio, please try again.")
            print("Error: " + str(e))

if __name__ == "__main__":
    main()