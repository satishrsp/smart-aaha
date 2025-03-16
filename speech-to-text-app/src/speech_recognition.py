class SpeechRecognizer:
    def __init__(self):
        import speech_recognition as sr
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def start_recognition(self):
        with self.microphone as source:
            print("Adjusting for ambient noise... Please wait.")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from the service; {e}"

    def stop_recognition(self):
        print("Stopping recognition.")