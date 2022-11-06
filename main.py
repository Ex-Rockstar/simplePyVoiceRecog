import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say Somethin -.-")

    audio = r.listen(source)

    print("Recognizing Now .... ")


    try:
        print("You said \n" + r.recognize_google(audio))
        print("Audio Recorded Successfully \n ")


    except Exception as e:
        print("Error :  " + str(e))



    with open("recorded.wav", "wb") as f:
        f.write(audio.get_wav_data())


