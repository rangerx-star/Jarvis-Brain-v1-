import os
import time

# Jarvis synthesizer or TTS(text-to-speech)

def synthesize(TEXT):
  if TEXT:
    print("\nSynthesizing...")
    os.system(f'termux-tts-speak "{TEXT}"')
    time.sleep(.5)
    print("END synthesizing")
  else:
    print("No text given to synthesize.")