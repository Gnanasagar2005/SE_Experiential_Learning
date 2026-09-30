import math
from array import array
import pygame

SAMPLE_RATE = 44100

def _tone(freqs, duration_ms, volume=0.4):
    # Builds a short 16-bit mono tone; the freqs are played one after another.
    samples = array("h")
    per_note = int(SAMPLE_RATE * duration_ms / 1000 / len(freqs))
    for freq in freqs:
        for i in range(per_note):
            fade = min(1.0, (per_note - i) / (SAMPLE_RATE * 0.01))  # avoid a click at the end
            samples.append(int(32767 * volume * fade * math.sin(2 * math.pi * freq * i / SAMPLE_RATE)))
    return pygame.mixer.Sound(buffer=samples.tobytes())

class Sounds:
    def __init__(self):
        self.enabled = False
        try:
            pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1)
            self.go = _tone([880], 120)
            self.false_start = _tone([220, 160], 300)
            self.session_end = _tone([523, 659, 784, 1047], 600)
            self.enabled = True
        except pygame.error:
            # No audio device available, so the game runs silently.
            pass

    def play(self, name):
        if self.enabled:
            getattr(self, name).play()
