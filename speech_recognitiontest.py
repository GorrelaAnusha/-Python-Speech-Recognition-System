import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)  # Listen to the user's speech

    try:
        # Recognize speech using Google Web Speech API
        output = r.recognize_google(audio)
        print("You said: {}".format(output))
    except Exception as e:
        # Handle any errors
        print("I can't recognize what you said, please speak clearly.")