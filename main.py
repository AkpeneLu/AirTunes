import numpy as np
import pandas as pd
from config import ALL_PATHS, POSSIBLE_SENSORS
from instruments import InstrumentCombinations

#return random.choice(matching_combinations)
def get_random_instrument_combination(sensor_count):
    matching_combinations = []
    
    for combination in InstrumentCombinations:
        if len(combination.value) <= sensor_count:
            matching_combinations.append({combination: combination.value[:sensor_count]}) 
    
    if not matching_combinations:
        return []
    
    return matching_combinations

for paths in ALL_PATHS: 
    folder_path = paths
    files = ALL_PATHS[folder_path]

    for set_number in range(1, files + 1):  
        path = f"{folder_path}set{set_number}.csv"
        
        df = pd.read_csv(path, delimiter=';') 

        available_columns = [col for col in POSSIBLE_SENSORS if col in df.columns]
        all_valid_instrument_combination = get_random_instrument_combination(len(available_columns))
        print(all_valid_instrument_combination)

        df_filtered = df[available_columns]


    

