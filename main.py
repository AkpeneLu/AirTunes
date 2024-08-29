import numpy as np
import pandas as pd
from config import ALL_PATHS, POSSIBLE_SENSORS
from instrument_patterns import InstrumentPatterns
from instruments import InstrumentCombinations

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


for paths in ALL_PATHS: 
    folder_path = paths
    files = ALL_PATHS[folder_path]

    for set_number in range(1, files + 1):  
        path = f"{folder_path}set{set_number}.csv"
        
        df = pd.read_csv(path, delimiter=';') 

        available_columns = [col for col in POSSIBLE_SENSORS if col in df.columns]
        all_valid_instrument_combination = get_random_instrument_combination(len(available_columns))
        df_filtered = df[available_columns]

        mapping = map_sensors_to_instrument(df_filtered, all_valid_instrument_combination)

    

