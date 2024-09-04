from scamp import *
import random

# Create a SCAMP session
session = Session()

session.tempo = 120

# Set up the instruments
piano = session.new_part("piano")
trumpet = session.new_part("trumpet")
violin = session.new_part("violin")
bass = session.new_part("acoustic bass")
drums = session.new_part("drum set", preset="Standard Drum Kit")

# Define a chord progression
chords = [
    (60, 64, 67),  # C Major (C, E, G)
    (57, 60, 64),  # A Minor (A, C, E)
    (55, 59, 62),  # G Major (G, B, D)
    (53, 57, 60)   # F Major (F, A, C)
]

# Define the melody for trumpet and violin
melody_trumpet = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
melody_violin = [72, 71, 69, 67, 65, 64, 62, 60]   # Descending C major scale

# Define a bassline
bassline = [36, 40, 43, 41]  # C, E, G, F in lower octaves

# Define a simple drum pattern (kick, snare, hi-hat)
drum_pattern = [
    (0, 0.75),  # Kick drum on beat 1
    (42, 0.25), # Closed hi-hat on the "and" of beat 1
    (0, 0.75),  # Kick drum on beat 1
    (42, 0.25), # Closed hi-hat on the "and" of beat 1
    (0, 0.75),  # Kick drum on beat 1
    (42, 0.25), # Closed hi-hat on the "and" of beat 1
    (0, 0.75),  # Kick drum on beat 1
    (42, 0.25), # Closed hi-hat on the "and" of beat 1
]

drum_pattern_2 = [
    (36, 1),  # Kick drum on beat 1
    (36, 1),  # Kick drum on beat 1
    (36, 1),  # Kick drum on beat 1
    (36, 1),  # Kick drum on beat 1
]

drum_pattern_3 = [
    (36, 0.5),  # Kick drum on beat 1
    (36, 0.5),  # Kick drum on beat 1
    (36, 0.5),  # Kick drum on beat 1
    (36, 0.5),  # Kick drum on beat 1
]

# Function to play the piano chords
def play_piano():
    while True:
        for chord in chords:
            piano.play_chord(chord, 1, 2)  # Play each chord for 1.5 seconds
            #piano.play_chord(chord, 1, 0.1)  # Play each chord for 1.5 seconds
            wait(1)

notes = [60, 62, 64, 67, 69]
durada = [1.0, 2.0, 0.25, 0.5]
random_numbers = [(random.choice(notes), random.choice(durada)) for _ in range(80)]

#random_numbers = random.choices(notes, k=80)

# Function to play the trumpet melody
def play_trumpet():
    while True:
        for note, duration in random_numbers:
            trumpet.play_note(note, 0.8, duration)
            wait(duration/2)

# Function to play the violin melody
def play_violin():
    for note in chords:
        violin.play_note(note, 0.6, 1.0)
        wait(0.5)

def play_piano():
    while True:
        for chord in chords:
            piano.play_chord(chord, 1, 2)  # Play each chord for 1.5 seconds
            #piano.play_chord(chord, 1, 0.1)  # Play each chord for 1.5 seconds
            wait(1)

# Function to play the bassline
def play_bass():
    for note in bassline:
        bass.play_note(note, 1.2, 1.5)
        wait(1.5)

# Function to play the drum pattern
def play_drums():
    while True:
        for drum, duration in drum_pattern:
            drums.play_note(drum, 1.0, duration)
            wait(duration / 2)

def play_drums_2():
    while True:
        for drum, duration in drum_pattern_2:
            drums.play_note(drum, 1.0, duration)
            wait(duration / 2)

def play_drums_3():
    while True:
        for drum, duration in drum_pattern_3:
            drums.play_note(drum, 1.0, duration)
            wait(duration / 2)





# Start all parts simultaneously
#session.start_transcribing()

# Start each part in its own thread
#session.fork(play_piano)
#session.fork(play_trumpet)
#session.fork(play_violin)
#session.fork(play_bass)
session.fork(play_drums)
session.fork(play_drums_2)
wait(9)
session.fork(play_drums_3)
wait(3)
session.fork(play_piano)
wait(12)
session.fork(play_trumpet)
wait(400)