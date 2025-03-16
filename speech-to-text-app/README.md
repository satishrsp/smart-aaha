3/15/2025: This code is generated from VS code and this is not working. Failing with the below error:

(venv) PS E:\repo\smart-aaha\speech-to-text-app> python.exe .\src\main.py
Traceback (most recent call last):
  File "E:\repo\smart-aaha\speech-to-text-app\src\main.py", line 1, in <module>
    from speech_recognition import SpeechRecognizer, Microphone
ImportError: cannot import name 'Microphone' from 'speech_recognition' (E:\repo\smart-aaha\speech-to-text-app\src\speech_recognition.py)

# Speech to Text App

This project is a simple speech-to-text application built in Python. It utilizes speech recognition libraries to convert spoken language into written text.

## Project Structure

```
speech-to-text-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── speech_recognition.py  # Contains the SpeechRecognizer class
│   └── utils
│       └── __init__.py  # Utility functions and constants
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/speech-to-text-app.git
   cd speech-to-text-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

Follow the prompts to start the speech recognition process.

## Dependencies

This project requires the following Python packages:

- SpeechRecognition
- pyaudio (for microphone input)

Make sure to install these packages using the `requirements.txt` file provided.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.