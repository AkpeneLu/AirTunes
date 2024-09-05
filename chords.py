
notes_happy = [60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69]


notes_sad = random_midi_list = [
    66, 68, 60, 62, 63, 66, 69, 62, 69, 62, 62, 71, 71, 63, 68, 66, 66, 60, 
    68, 68, 63, 69, 68, 65, 66, 66, 63, 60, 60, 63, 65, 65, 68, 69, 60, 66, 
    69, 65, 62, 68, 68, 71, 66, 71, 60, 71, 60, 62, 71, 63, 60, 62, 62, 69, 
    63, 62, 62, 60, 60, 62, 68, 63, 60, 62, 71, 69, 69, 68, 68, 68, 69, 60, 
    66, 71, 66, 66, 62, 63, 60, 69
]

duration = [1.0, 0.25, 1.0, 2.0, 0.25, 0.5, 1.0, 2.0, 0.25, 1.0, 2.0, 0.25, 0.5, 1.0, 2.0, 0.5, 0.25, 2.0, 0.25, 2.0, 0.5, 1.0, 1.0, 0.5, 0.25, 2.0, 0.25, 0.5, 0.5, 1.0, 0.5, 1.0, 2.0, 2.0, 2.0, 0.5, 0.25, 0.25, 0.5, 1.0, 2.0, 0.25, 0.5]
#random.shuffle(duration)


# Happy Chord Progression B
happy_chords_progession_B = [
    (62, 65, 69),  # D Major (D, F#, A)
    (59, 62, 66),  # B Minor (B, D, F#)
    (55, 59, 62),  # G Major (G, B, D)
    (57, 61, 64)   # A Major (A, C#, E)
]

# Happy Chord Progression C
happy_chords_progession_C = [
    (65, 69, 72),  # F Major (F, A, C)
    (62, 65, 69),  # D Major (D, F#, A)
    (59, 63, 66),  # Bb Major (Bb, D, F)
    (57, 61, 64)   # A Major (A, C#, E)
]

# Happy Chord Progression D
happy_chords_progession_D = [
    (64, 67, 71),  # E Major (E, G#, B)
    (57, 61, 64),  # A Major (A, C#, E)
    (55, 59, 62),  # G Major (G, B, D)
    (59, 62, 66)   # B Minor (B, D, F#)
]

# Happy Chord Progression E
happy_chords_progession_E = [
    (65, 69, 72),  # F Major (F, A, C)
    (62, 66, 69),  # D Minor (D, F, A)
    (57, 61, 64),  # A Major (A, C#, E)
    (60, 64, 67)   # C Major (C, E, G)
]

# Happy Chord Progression F
happy_chords_progession_F = [
    (67, 71, 74),  # G Major (G, B, D)
    (64, 68, 71),  # E Minor (E, G, B)
    (62, 65, 69),  # D Major (D, F#, A)
    (60, 64, 67)   # C Major (C, E, G)
]

# Happy Chord Progression G
happy_chords_progession_G = [
    (59, 62, 66),  # B Minor (B, D, F#)
    (62, 66, 69),  # D Minor (D, F, A)
    (65, 69, 72),  # F Major (F, A, C)
    (55, 59, 62)   # G Major (G, B, D)
]

# Happy Chord Progression H
happy_chords_progession_H = [
    (64, 67, 71),  # E Major (E, G#, B)
    (60, 64, 67),  # C Major (C, E, G)
    (65, 69, 72),  # F Major (F, A, C)
    (55, 59, 62)   # G Major (G, B, D)
]

# Happy Chord Progression I
happy_chords_progession_I = [
    (57, 61, 64),  # A Major (A, C#, E)
    (55, 59, 62),  # G Major (G, B, D)
    (59, 63, 66),  # Bb Major (Bb, D, F)
    (64, 68, 71)   # E Minor (E, G, B)
]

# Happy Chord Progression J
happy_chords_progession_J = [
    (60, 63, 67),  # C Minor (C, Eb, G)
    (57, 61, 64),  # A Major (A, C#, E)
    (55, 58, 62),  # G Minor (G, Bb, D)
    (62, 66, 69)   # D Minor (D, F, A)
]

# Happy Chord Progression K
happy_chords_progession_K = [
    (65, 69, 72),  # F Major (F, A, C)
    (59, 63, 66),  # Bb Major (Bb, D, F)
    (64, 68, 71),  # E Minor (E, G, B)
    (55, 59, 62)   # G Major (G, B, D)
]


def map_value_to_note(values, mood = 1):
    """Map a sensor value to a chord."""

    value_min = min(values)
    value_max = max(values)

    
    notes_to_play = [0] * len(values)
    i=0
    for value in values:
        if mood == 1:
            num_notes = len(notes_happy)    
            scaled_value = int((value - value_min) / (value_max - value_min) * (num_notes - 1))
            notes_to_play[i] = notes_happy[scaled_value]
        else: 
            num_notes = len(notes_sad)
            scaled_value = int((value - value_min) / (value_max - value_min) * (num_notes - 1))
            notes_to_play[i] = notes_sad[scaled_value]
        i += 1

    return notes_to_play

def map_value_to_duration(values):
    """Map a sensor value to a duration."""

    value_min = min(values)
    value_max = max(values)

    num_duration = len(duration)
    duration_to_play = [0] * len(values)
    i=0
    for value in values:
        scaled_value = int((value - value_min) / (value_max - value_min) * (num_duration - 1))
        #print(num_duration, scaled_value)
        duration_to_play[i] = duration[scaled_value]
        i += 1
    
    return duration_to_play