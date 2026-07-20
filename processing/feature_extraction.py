"""
=========================================================
Hybrid BCI JioSaavn Automation
Feature Extraction
=========================================================

Responsibilities
----------------
1. Extract statistical features
2. Extract signal energy features
3. Extract frequency features
4. Return a feature vector

Input:
    Preprocessed EEG Signal

Output:
    Feature Vector (NumPy Array)

=========================================================
"""

import logging
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy.signal import welch


class FeatureExtractor:

    def __init__(self, sampling_rate=128):

        self.fs = sampling_rate

        logging.info("Feature Extractor Initialized")

    # --------------------------------------------------

    def extract(self, signal):

        """
        Complete Feature Extraction Pipeline
        """

        if signal is None:

            return None

        signal = np.asarray(signal)

        features = []

        # Statistical Features
        features.extend(
            self.statistical_features(signal)
        )

        # Energy Features
        features.extend(
            self.energy_features(signal)
        )

        # Frequency Features
        features.extend(
            self.frequency_features(signal)
        )

        return np.asarray(features, dtype=np.float32)

    # --------------------------------------------------

    def statistical_features(self, signal):

        """
        Statistical Features
        """

        return [

            np.mean(signal),

            np.std(signal),

            np.var(signal),

            np.min(signal),

            np.max(signal),

            np.median(signal),

            np.ptp(signal),

            skew(signal),

            kurtosis(signal),

            np.sqrt(np.mean(signal ** 2))

        ]

    # --------------------------------------------------

    def energy_features(self, signal):

        """
        Signal Energy Features
        """

        energy = np.sum(signal ** 2)

        power = np.mean(signal ** 2)

        rms = np.sqrt(power)

        return [

            energy,

            power,

            rms

        ]

    # --------------------------------------------------

    def frequency_features(self, signal):

        """
        Power Spectral Density Features
        """

        freq, psd = welch(

            signal,

            fs=self.fs,

            nperseg=min(256, len(signal))

        )

        delta = self.band_power(freq, psd, 0.5, 4)

        theta = self.band_power(freq, psd, 4, 8)

        alpha = self.band_power(freq, psd, 8, 13)

        beta = self.band_power(freq, psd, 13, 30)

        gamma = self.band_power(freq, psd, 30, 45)

        total_power = np.sum(psd)

        return [

            delta,

            theta,

            alpha,

            beta,

            gamma,

            total_power

        ]

    # --------------------------------------------------

    def band_power(

        self,

        frequencies,

        psd,

        low,

        high

    ):

        """
        Calculate EEG Band Power
        """

        mask = (

            (frequencies >= low)

            &

            (frequencies <= high)

        )

        return np.sum(psd[mask])

    # --------------------------------------------------

    def feature_names(self):

        """
        Names of Features
        """

        return [

            "Mean",

            "StandardDeviation",

            "Variance",

            "Minimum",

            "Maximum",

            "Median",

            "PeakToPeak",

            "Skewness",

            "Kurtosis",

            "RMS",

            "Energy",

            "Power",

            "SignalRMS",

            "DeltaPower",

            "ThetaPower",

            "AlphaPower",

            "BetaPower",

            "GammaPower",

            "TotalPower"

        ]