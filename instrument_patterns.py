import numpy as np

class InstrumentPatterns:
    @staticmethod
    def check_data_validity(data, calculation_func):
        # Remove NaN values before any calculations
        data = data.dropna()
        
        if data.empty:
            return np.inf  # Return a large value to indicate poor fit
        
        try:
            return calculation_func(data)
        except Exception:
            return np.inf  # Handle any other exceptions that might occur

    @staticmethod
    def drums_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.std())

    @staticmethod
    def piano_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean())

    @staticmethod
    def bass_guitar_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean() / x.std() if x.std() != 0 else np.inf)

    @staticmethod
    def flute_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.median())

    @staticmethod
    def violin_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.max() - x.min())

    @staticmethod
    def cello_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean() * x.std())

    @staticmethod
    def clarinet_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean() / x.std())

    @staticmethod
    def saxophone_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.std() * x.max())

    @staticmethod
    def double_bass_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.min())

    @staticmethod
    def trumpet_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.max())

    @staticmethod
    def electric_guitar_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.max() - x.mean())

    @staticmethod
    def synthesizer_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.std() / x.mean())

    @staticmethod
    def synth_pad_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean() / x.std())

    @staticmethod
    def wind_chimes_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.kurtosis())

    @staticmethod
    def ocean_waves_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.autocorr())

    @staticmethod
    def birds_chirping_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.skew())

    @staticmethod
    def synth_lead_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean() + x.std())

    @staticmethod
    def electronic_drums_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.std() + x.kurtosis())

    @staticmethod
    def bass_synth_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean() / x.std())

    @staticmethod
    def viola_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.median() * x.std())

    @staticmethod
    def trombone_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.min() * x.std())

    @staticmethod
    def tuba_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.min() / x.std())

    @staticmethod
    def oboe_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean() / x.std())

    @staticmethod
    def timpani_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.max() * x.std())

    @staticmethod
    def snare_drum_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.std() + x.skew())

    @staticmethod
    def acoustic_guitar_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.median())

    @staticmethod
    def mandolin_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean() + x.median())

    @staticmethod
    def harmonica_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.std() * x.median())

    @staticmethod
    def hand_drums_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.std() + x.median())

    @staticmethod
    def theremin_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.mean() / x.std())

    @staticmethod
    def modular_synth_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.std() * x.max())

    @staticmethod
    def drum_machine_pattern(data):
        return InstrumentPatterns.check_data_validity(data, lambda x: x.kurtosis() + x.std())
