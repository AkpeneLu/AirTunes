import numpy as np
import pandas as pd
from config import ALL_PATHS, POSSIBLE_SENSORS
from instrument_patterns import InstrumentPatterns
from instruments import InstrumentCombinations
from scamp import *
#return random.choice(matching_combinations)
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


def play_instruments(piano_instrument, snare_drum_instrument, drum_data, piano_data):
    for drum_value, piano_value in zip(drum_data, piano_data):
        # Map sensor value to a velocity for the snare drum sound
        snare_drum_velocity = min(max(int(drum_value), 30), 127)  # Use the sensor data directly for velocity
        piano_pitch = 60 + int(piano_value / 10)  # Map sensor value to piano pitch
        
        # Adjust drum duration based on sensor data (e.g., higher value -> shorter duration)
        drum_duration = max(0.1, 1.0 - (drum_value / max(drum_data) * 0.9))  # Normalize and invert

        # Play the notes concurrently
        snare_drum_instrument.play_note(38, snare_drum_velocity, drum_duration)  # Acoustic Snare Drum (MIDI note 38)
        piano_instrument.play_note(piano_pitch, 0.8, 0.5)  # Play the piano note

        # Wait for the duration of the drum note
        wait(drum_duration)




def scale_data(data, factor=10):
    # Scale the data by a given factor
    return (data - data.min()) * factor / (data.max() - data.min())


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

        mapping = map_sensors_to_instrument(df_filtered, all_valid_instrument_combination)

        #{'PIANO': 'LIGHT %', 'FLUTE': 'TEMP °C', 'BASS_GUITAR': 'VOC ppb', 'DRUMS': 'PRESSURE hPa', 'VIOLIN': 'HUMIDITY %'}

        
        # Extracting the mapped sensor data
        drum_data = scale_data(df_filtered[mapping.get('DRUMS', 'VOC ppb')], factor=1000)
        piano_data = scale_data(df_filtered[mapping.get('PIANO', 'LIGHT %')], factor=100)

        #print(drum_data.head())
        #print(piano_data.head())

        session = Session()
        
        # Directly add instruments to the session
        snare_drum_instrument = session.new_part("drum")
        piano_instrument = session.new_part("piano")
        
        # Play both instruments together
        play_instruments(piano_instrument, snare_drum_instrument, drum_data, piano_data)
        
        # Run the session
        session.run()

    

