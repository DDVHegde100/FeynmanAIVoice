import speech_recognition as sr
import pyttsx3
import tkinter as tk

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to capture voice input
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "Sorry, I could not request results."

# Function to speak a response
def speak_response(response):
    tts_engine.say(response)
    tts_engine.runAndWait()

# Function to process commands
def process_command(command):
    if "turn on the light" in command:
        light_status.set("Light: ON")
        speak_response("Turning on the light")
    elif "turn off the light" in command:
        light_status.set("Light: OFF")
        speak_response("Turning off the light")
    elif "turn on the pump" in command:
        pump_status.set("Pump: ON")
        speak_response("Turning on the pump")
    elif "turn off the pump" in command:
        pump_status.set("Pump: OFF")
        speak_response("Turning off the pump")
    else:
        speak_response("Sorry, I did not understand that command.")

# Function to handle voice commands
def handle_voice_command():
    command = listen_command()
    process_command(command)

# Create a simple GUI
root = tk.Tk()
root.title("Smart Home Control")

# GUI elements for device status
light_status = tk.StringVar(value="Light: OFF")
pump_status = tk.StringVar(value="Pump: OFF")

light_label = tk.Label(root, textvariable=light_status)
light_label.pack(pady=10)
pump_label = tk.Label(root, textvariable=pump_status)
pump_label.pack(pady=10)

# Button to initiate voice command
voice_button = tk.Button(root, text="Give Voice Command", command=handle_voice_command)
voice_button.pack(pady=20)

root.mainloop()
