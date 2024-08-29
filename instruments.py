from enum import Enum

class Instrument(Enum):
    DRUMS = "Drums"
    PIANO = "Piano"
    BASS_GUITAR = "Bass Guitar"
    FLUTE = "Flute"
    VIOLIN = "Violin"
    CELLO = "Cello"
    CLARINET = "Clarinet"
    SAXOPHONE = "Saxophone"
    DOUBLE_BASS = "Double Bass"
    TRUMPET = "Trumpet"
    ELECTRIC_GUITAR = "Electric Guitar"
    SYNTHESIZER = "Synthesizer"
    SYNTH_PAD = "Synth Pad"
    WIND_CHIMES = "Wind Chimes"
    OCEAN_WAVES = "Ocean Waves"
    BIRDS_CHIRPING = "Birds Chirping"
    SYNTH_LEAD = "Synth Lead"
    ELECTRONIC_DRUMS = "Electronic Drums"
    BASS_SYNTH = "Bass Synth"
    VIOLA = "Viola"
    TROMBONE = "Trombone"
    TUBA = "Tuba"
    OBOE = "Oboe"
    TIMPANI = "Timpani"
    SNARE_DRUM = "Snare Drum"
    ACOUSTIC_GUITAR = "Acoustic Guitar"
    MANDOLIN = "Mandolin"
    HARMONICA = "Harmonica"
    HAND_DRUMS = "Hand Drums"
    THEREMIN = "Theremin"
    MODULAR_SYNTH = "Modular Synth"
    DRUM_MACHINE = "Drum Machine"


class InstrumentCombinations(Enum):
    BASIC_QUARTET = [
        Instrument.PIANO,        # Lead
        Instrument.FLUTE,        # Melody
        Instrument.BASS_GUITAR,  # Harmony
        Instrument.DRUMS         # Rhythm
    ]
    CLASSICAL_TRIO = [
        Instrument.VIOLIN,       # Lead
        Instrument.CELLO,        # Harmony
        Instrument.CLARINET      # Support Melody
    ]
    JAZZ_ENSEMBLE = [
        Instrument.SAXOPHONE,    # Lead
        Instrument.TRUMPET,      # Melody
        Instrument.DOUBLE_BASS,  # Harmony
        Instrument.DRUMS         # Rhythm
    ]
    ROCK_BAND = [
        Instrument.ELECTRIC_GUITAR,  # Lead
        Instrument.SYNTHESIZER,      # Harmony/Melody
        Instrument.BASS_GUITAR,      # Harmony
        Instrument.DRUMS             # Rhythm
    ]
    AMBIENT_SOUNDSCAPE = [
        Instrument.SYNTH_PAD,     # Lead Ambient
        Instrument.WIND_CHIMES,   # Effects
        Instrument.OCEAN_WAVES,   # Background Ambient
        Instrument.BIRDS_CHIRPING # Background Effects
    ]
    ELECTRONIC_DUO = [
        Instrument.SYNTH_LEAD,    # Lead
        Instrument.BASS_SYNTH,    # Harmony
        Instrument.ELECTRONIC_DRUMS  # Rhythm
    ]
    ORCHESTRAL_SYMPHONY = [
        Instrument.VIOLIN,        # Lead
        Instrument.FLUTE,         # Melody
        Instrument.VIOLA,         # Harmony
        Instrument.CELLO,         # Harmony
        Instrument.DOUBLE_BASS,   # Bass
        Instrument.TRUMPET,       # Melody/Accent
        Instrument.TROMBONE,      # Harmony
        Instrument.TUBA,          # Bass Harmony
        Instrument.OBOE,          # Support Melody
        Instrument.CLARINET,      # Harmony/Support
        Instrument.SNARE_DRUM     # Rhythm
    ]
    FOLK_BAND = [
        Instrument.ACOUSTIC_GUITAR, # Lead
        Instrument.MANDOLIN,        # Melody
        Instrument.HARMONICA,       # Melody/Effects
        Instrument.HAND_DRUMS       # Rhythm
    ]
    MINIMALIST_DUO = [
        Instrument.PIANO,        # Lead
        Instrument.CELLO         # Harmony
    ]
    EXPERIMENTAL_SET = [
        Instrument.THEREMIN,     # Lead/Experimental
        Instrument.MODULAR_SYNTH, # Ambient/Effects
        Instrument.DRUM_MACHINE  # Rhythm
    ]