
notes_happy = [60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69]
notes_sad = [60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69, 60, 62, 64, 67, 69]

duration = [1.0, 0.25, 1.0, 2.0, 0.25, 0.5, 1.0, 2.0, 0.25, 1.0, 2.0, 0.25, 0.5, 1.0, 2.0, 0.5, 0.25, 2.0, 0.25, 2.0, 0.5, 1.0, 1.0, 0.5, 0.25, 2.0, 0.25, 0.5, 0.5, 1.0, 0.5, 1.0, 2.0, 2.0, 2.0, 0.5, 0.25, 0.25, 0.5, 1.0, 2.0, 0.25, 0.5]
#random.shuffle(duration)



def map_value_to_note(values, moods):
    """Map a sensor value to a chord."""

    value_min = min(values)
    value_max = max(values)

    
    notes_to_play = [0] * len(values)
    i=0
    for value in values:
        if moods[i] == 1:
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