import numpy as np
import pandas as pd
from chords import map_value_to_chord
from config import ALL_PATHS, POSSIBLE_SENSORS
from instrument_patterns import InstrumentPatterns
from instruments import InstrumentCombinations
from scamp import *
import random

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

# Function to play hi-hat rhythm based on sensor data
def play_hi_hat(sensor_value):
    for _ in range(8):  # Eight beats in a measure
        probability = sensor_value / 100.0  # Normalize sensor value to [0, 1]
        if random.uniform(0, 1) < probability:
            drums.play_note(DRUM_MAPPING["closed_hi_hat"], 1, 0.5)
        else:
            drums.play_note(DRUM_MAPPING["closed_hi_hat"], 1, 0.25)
            drums.play_note(DRUM_MAPPING["closed_hi_hat"], 1, 0.25)

# Function to play backbeat rhythm based on sensor data
def play_backbeat(sensor_value):
    for i in range(4):  # Four beats in a measure
        if i % 2 == 0:  # Play bass drum on beats 1 and 3
            probability_bass = sensor_value / 150.0
            if random.uniform(0, 1) < probability_bass:
                drums.play_note(DRUM_MAPPING["bass_drum"], 1, 1)
            else:
                drums.play_note(DRUM_MAPPING["bass_drum"], 1, 0.5)
                drums.play_note(DRUM_MAPPING["bass_drum"], 1, 0.5)
        else:  # Play snare drum on beats 2 and 4
            probability_snare = sensor_value / 100.0
            if random.uniform(0, 1) < probability_snare:
                drums.play_note(DRUM_MAPPING["snare"], 1, 1)
            else:
                drums.play_note(DRUM_MAPPING["snare"], 1, 0.75)
                drums.play_note(DRUM_MAPPING["snare"], 1, 0.25)

# Main loop to generate the rhythm based on sensor data
def generate_drum_pattern(session, sensor_data):
    for sensor_value in sensor_data:
        session.fork(play_hi_hat, args=(sensor_value,))
        session.fork(play_backbeat, args=(sensor_value,))
        wait(4)  # Wait for the measure to finish before repeating

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

        session = Session(tempo=140)
        drums = session.new_midi_part("drums", 2)

        DRUM_MAPPING = {
            "bass_drum": 36,
            "snare": 38,
            "closed_hi_hat": 42,
            "open_hi_hat": 46,
            "ride": 51,
            "crash": 49,
        }

        drum_instrument = session.new_part("snare_drum")  # Correct the instrument part name
        piano_instrument = session.new_part("piano")
        
        play_instruments(piano_instrument, drum_instrument, drum_data, piano_data)
        generate_drum_pattern(session, drum_data)

        session.run()
