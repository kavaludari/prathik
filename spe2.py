import speech_recognition as sr

#Record audio
r=sr.Recognizer()
with sr.Microphone()as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_threshold = True
	print("Say something")
	audio = r.listen(source)

try:
	print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
	print("Could not request results from Google speech Recognition service; {0}".format(e))