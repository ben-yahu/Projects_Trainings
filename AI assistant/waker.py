import os
from pocketsphinx import LiveSpeech
import subprocess

# Define the wake word(s) you want to listen for
WAKE_WORDS = ["yumi"]

# Loop indefinitely to keep listening
while True:
    # Create a new instance of LiveSpeech with the appropriate configuration
    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=True,
        lm=False,
        keyphrase=" | ".join(WAKE_WORDS),
        kws_threshold=1,
    )
    
    # Start listening
    print("Listening for wake word...")
    for phrase in speech:
        # When the wake word is detected, print a message and break out of the loop
        print(f"Wake word '{phrase}' detected!")
        break

    # Run your python script here
    subprocess.run(["python", "E:\My Practises\Yume\Yume AI.py"])

    # Once the script has finished running, start listening again
    print("Script finished. Listening for wake word...")
