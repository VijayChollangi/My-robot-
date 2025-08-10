import speech_recognition as sr
import time
from datetime import datetime

# File to save command history
log_file = "command_history.txt"

# Clear old log or create new
with open(log_file, "w") as f:
    f.write("🔴 Voice Command History Log\n")
    f.write(f"Session Start: {datetime.now()}\n\n")

def simulate_movement(command):
    if "forward" in command:
        print("🚗 Moving Forward")
    elif "backward" in command:
        print("🔙 Moving Backward")
    elif "left" in command:
        print("↪️ Turning Left")
    elif "right" in command:
        print("↩️ Turning Right")
    elif "stop" in command:
        print("🛑 Robot Stopped")
    else:
        print("❓ Unknown Command")

    # Save command to file
    with open(log_file, "a") as f:
        f.write(f"{datetime.now().strftime('%H:%M:%S')} → {command}\n")

# Recognizer setup
recognizer = sr.Recognizer()

print("🤖 Virtual Robot Ready. Speak a command...")

try:
    while True:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"✅ You said: {command}")
                simulate_movement(command)

            except sr.UnknownValueError:
                print("❌ Could not understand voice.")
            except sr.RequestError:
                print("🌐 Could not connect to speech service.")

            time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Virtual Robot Exiting.")
    print("\n📜 Command History:")
    with open(log_file, "r") as f:
        print(f.read())