import numpy as np
import pandas as pd
from chords import map_value_to_chord
from config import ALL_PATHS, POSSIBLE_SENSORS
from instrument_patterns import InstrumentPatterns
from instruments import InstrumentCombinations
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

def get_random_instrument_combination(sensor_count):
    matching_combinations = {}
    for combination in InstrumentCombinations:
        if len(combination.value) <= sensor_count:
            matching_combinations[combination] = combination.value[:sensor_count]
    return matching_combinations

def map_sensors_to_instrument(df_filtered, combinations):
    sensor_to_instrument_mapping = {}
    assigned_sensors = set()
    for combination in combinations:
        for instrument in combinations[combination]:        
            best_fit_column = None
            best_fit_score = None
            for column in df_filtered.columns:
                if column in assigned_sensors:
                    continue  # Skip already assigned sensors
                data = df_filtered[column]
                pattern_function = getattr(InstrumentPatterns, f"{instrument.name.lower()}_pattern", None)
                if pattern_function:
                    fit_score = pattern_function(data)
                    if best_fit_score is None or fit_score < best_fit_score:  
                        best_fit_score = fit_score
                        best_fit_column = column
            if best_fit_column:
                if instrument.name not in sensor_to_instrument_mapping:
                    sensor_to_instrument_mapping[instrument.name] = best_fit_column
                    assigned_sensors.add(best_fit_column) 
    return sensor_to_instrument_mapping

def get_sensor_threshold_mapping(df_filtered):
    sensor_to_threshold_mapping = {}
    
    for column in df_filtered.columns:
        data = df_filtered[column]
        max = data.max()
        min = data.min()
        # Calculate the range of the data
        data_range = max - min
        # Set the threshold as one-third of the range
        threshold = min + (data_range / 3)
        # Store the threshold in the dictionary
        sensor_to_threshold_mapping[column] = {"threshold": threshold, "min": min, "max" : max}

    return sensor_to_threshold_mapping
        

def scale_data(data, factor=10):
    return (data - data.min()) * factor / (data.max() - data.min())

def play_instruments(piano_instrument, snare_drum_instrument, drum_data, piano_data):
    value_min = min(piano_data)
    value_max = max(piano_data)

    for drum_value, piano_value in zip(drum_data, piano_data):
        snare_drum_velocity = min(max(int(drum_value), 30), 127)  # Use the sensor data directly for velocity
        piano_chord = map_value_to_chord(piano_value, value_min, value_max)
        drum_duration = max(0.1, 1.0 - (drum_value / max(drum_data) * 0.9))  # Normalize and invert

        note_handles = []
        for note in piano_chord:
            note_handle = piano_instrument.start_note(note, 0.8)  # Start each note in the chord
            note_handles.append(note_handle)
        
        wait(0.5)  # Hold the chord for the duration

        for note_handle in note_handles:
            piano_instrument.end_note(note_handle)

        #snare_drum_instrument.play_note(38, snare_drum_velocity, drum_duration)  # Acoustic Snare Drum (MIDI note 38)
        wait(drum_duration)



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
random_numbers_2 = [(random.choice(notes), random.choice(durada)) for _ in range(80)]

#random_numbers = random.choices(notes, k=80)

# Function to play the trumpet melody
"""def play_trumpet():
    while True:
        for note, duration in random_numbers:
            trumpet.play_note(note, 0.8, duration)
            wait(duration/2)"""

def play_trumpet(random_numbers):
    while True:
        for note in random_numbers:
            trumpet.play_note(note, 0.8, 1.0)
            wait(0.5)


# Function to play the violin melody
def play_violin():
    while True:
        for note, duration in random_numbers_2:
            violin.play_note(note, 0.8, duration)
            wait(duration/2)

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

# Main processing loop
for paths in ALL_PATHS: 
    folder_path = paths
    files = ALL_PATHS[folder_path]

    for set_number in range(1, files + 1):  
        path = f"{folder_path}set{set_number}.csv"
        df = pd.read_csv(path, delimiter=';') 

        available_columns = [col for col in POSSIBLE_SENSORS if col in df.columns]
        all_valid_instrument_combination = get_random_instrument_combination(len(available_columns))
        df_filtered = df[available_columns]
        df_filtered = df_filtered[df_filtered.shift() != df_filtered]
        df_filtered = df_filtered.dropna()

        instrument_mapping = map_sensors_to_instrument(df_filtered, all_valid_instrument_combination)
        threshold_mapping = get_sensor_threshold_mapping(df_filtered)
        drum_data = scale_data(df_filtered[instrument_mapping.get('DRUMS', 'VOC ppb')], factor=1000)
        piano_data = scale_data(df_filtered[instrument_mapping.get('PIANO', 'LIGHT %')], factor=100)
        piano_boolean = [0 if value <= threshold_mapping['LIGHT %']["threshold"] else 1 for value in piano_data]


        session = Session(tempo=120)
        #drums = session.new_midi_part("drums", 2)

        #session.fork(play_drums)
        #session.fork(play_drums_2)
        wait(9)
        #session.fork(play_drums_3)
        wait(3)
        #session.fork(play_piano)
        #<wait(12)
        session.fork(play_trumpet(piano_data))
        wait(12)
        #session.fork(play_violin)
        wait(400)

        session.run()
