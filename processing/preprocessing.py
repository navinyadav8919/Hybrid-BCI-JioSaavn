"""
=========================================================
Hybrid BCI JioSaavn Automation
EEG Signal Preprocessing
=========================================================

Responsibilities
----------------
1. Remove invalid values
2. Apply Band-pass Filter
3. Apply Notch Filter
4. Normalize Signal
5. Return Clean EEG Signal

This module NEVER performs:

• Feature Extraction
• Classification

=========================================================
"""

import logging
import numpy as np
from scipy.signal import butter
from scipy.signal import filtfilt
from scipy.signal import iirnotch


class Preprocessor:

    def __init__(self,
                 sampling_rate=128):

        self.fs = sampling_rate

        logging.info("Preprocessor Initialized")

    # -------------------------------------------------

    def process(self, signal):

        """
        Complete preprocessing pipeline.
        """

        if signal is None:

            return None

        signal = np.asarray(signal, dtype=np.float32)

        signal = self.remove_invalid(signal)

        signal = self.bandpass_filter(signal)

        signal = self.notch_filter(signal)

        signal = self.normalize(signal)

        return signal

    # -------------------------------------------------

    def remove_invalid(self, signal):

        """
        Replace NaN and Infinite values.
        """

        signal = np.nan_to_num(

            signal,

            nan=0.0,

            posinf=0.0,

            neginf=0.0

        )

        return signal

    # -------------------------------------------------

    def bandpass_filter(self,
                        signal,
                        lowcut=0.5,
                        highcut=40):

        """
        EEG Bandpass Filter

        Default:

        0.5 Hz - 40 Hz
        """

        nyquist = 0.5 * self.fs

        low = lowcut / nyquist

        high = highcut / nyquist

        b, a = butter(

            4,

            [low, high],

            btype="band"

        )

        return filtfilt(b, a, signal)

    # -------------------------------------------------

    def notch_filter(self,
                     signal,
                     frequency=50,
                     quality=30):

        """
        Remove Power Line Noise.

        India = 50 Hz

        US = 60 Hz
        """

        b, a = iirnotch(

            frequency,

            quality,

            self.fs

        )

        return filtfilt(b, a, signal)

    # -------------------------------------------------

    def normalize(self, signal):

        """
        Z-score normalization.
        """

        mean = np.mean(signal)

        std = np.std(signal)

        if std == 0:

            return signal

        return (signal - mean) / std

    # -------------------------------------------------

    def min_max_normalize(self,
                          signal):

        """
        Optional Min-Max Scaling.
        """

        minimum = np.min(signal)

        maximum = np.max(signal)

        if maximum == minimum:

            return signal

        return (signal - minimum) / (

            maximum - minimum

        )

    # -------------------------------------------------

    def remove_dc_offset(self,
                         signal):

        """
        Remove DC Offset.
        """

        return signal - np.mean(signal)