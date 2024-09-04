CHORDS = {
    "C_major": [60, 64, 67],   # C4, E4, G4
    "G_major": [67, 71, 74],   # G4, B4, D5
    "A_minor": [69, 72, 76],   # A4, C5, E5
    "F_major": [65, 69, 72],   # F4, A4, C5
    "D_minor": [62, 65, 69],   # D4, F4, A4
    "E_minor": [64, 67, 71],   # E4, G4, B4
    "B_flat_major": [70, 74, 77], # Bb4, D5, F5

    "E_major": [64, 68, 71],   # E4, G#4, B4
    "D_major": [62, 66, 69],   # D4, F#4, A4
    "A_major": [69, 73, 76],   # A4, C#5, E5
    "B_minor": [71, 74, 77],   # B4, D5, F#5
    "C_minor": [60, 63, 67],   # C4, Eb4, G4
    "F_minor": [65, 68, 72],   # F4, Ab4, C5
    "G_minor": [67, 70, 74],   # G4, Bb4, D5

    "C_augmented": [60, 64, 68],   # C4, E4, G#4
    "G_augmented": [67, 71, 75],   # G4, B4, D#5
    "A_augmented": [69, 73, 77],   # A4, C#5, F5

    "C_diminished": [60, 63, 66],   # C4, Eb4, Gb4
    "D_diminished": [62, 65, 68],   # D4, F4, Ab4
    "E_diminished": [64, 67, 70],   # E4, G4, Bb4
    "G_diminished": [67, 70, 73],   # G4, Bb4, Db5

    "B_major": [71, 75, 78],   # B4, D#5, F#5
    "F_sharp_major": [66, 70, 73],   # F#4, A#4, C#5
    "C_sharp_major": [61, 65, 68],   # C#4, F4, G#4
    "F_sharp_minor": [66, 69, 73],   # F#4, A4, C#5
    "C_sharp_minor": [61, 64, 68],   # C#4, E4, G#4
    "G_sharp_minor": [68, 71, 75],   # G#4, B4, D#5
}


def map_value_to_chord(value, value_min, value_max):
    """Map a sensor value to a chord."""
    chord_names = list(CHORDS.keys())
    num_chords = len(chord_names)
    scaled_value = int((value - value_min) / (value_max - value_min) * (num_chords - 1))
    return CHORDS[chord_names[scaled_value]]