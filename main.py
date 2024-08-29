import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import audio_plot


# List of possible columns
possible_columns = [
    'PM2_5 μg/m3',
    'CO2 ppm',
    'HUMIDITY %',
    'TEMP °C',
    'VOC ppb',
    'PRESSURE hPa',
    'PM1 μg/m3',
    'SOUND_LEVEL_A dBSPL',
    'LIGHT %'
]


all_paths = {
    "bad-air-quality/yearly/": 1,
    "moderate-air-quality/yearly/": 3,
    "moderate-air-quality/monthly/": 1,
    "good-air-quality/yearly/": 3,
}

for paths in all_paths: 
    folder_path = paths
    files = all_paths[folder_path]

    for set_number in range(1, files + 1):  
        path = f"{folder_path}set{set_number}.csv"
        
        df = pd.read_csv(path, delimiter=';') 

        # Find which of the possible columns are present in the DataFrame
        available_columns = [col for col in possible_columns if col in df.columns]

        # Extract only the available columns from the DataFrame
        df_filtered = df[available_columns]

        # Display the first few rows of the filtered DataFrame
        print(df_filtered.head())


    

