"""
=========================================================
Hybrid BCI JioSaavn Automation
Live EEG Provider
=========================================================

Responsibilities
----------------
1. Connect to EEG Device
2. Receive raw EEG samples
3. Send samples for processing
4. Return standardized commands

NOTE
----
This module DOES NOT perform:

• Preprocessing
• Feature Extraction
• Classification

Those are handled inside processing/.

=========================================================
"""

import time
import logging

from config.eeg_config import eeg_config

from processing.preprocessing import Preprocessor
from processing.feature_extraction import FeatureExtractor
from processing.classifier import Classifier
from processing.confidence_filter import ConfidenceFilter


class EEGProvider:

    def __init__(self):

        self.preprocessor = Preprocessor()

        self.feature_extractor = FeatureExtractor()

        self.classifier = Classifier()

        self.confidence_filter = ConfidenceFilter()

        self.connected = False

        self.connect()

    # --------------------------------------------------

    def connect(self):
        """
        Connect to EEG Device.
        """

        try:

            # =================================================
            # Replace this section with your EEG SDK
            #
            # Example:
            # self.device = Emotiv(...)
            # self.device.connect()
            #
            # or
            #
            # self.serial = serial.Serial(...)
            #
            # =================================================

            logging.info("Connecting to EEG Device...")

            self.connected = True

            logging.info("EEG Device Connected.")

        except Exception as e:

            logging.exception(e)

            self.connected = False

    # --------------------------------------------------

    def disconnect(self):

        logging.info("Disconnecting EEG Device...")

        self.connected = False

    # --------------------------------------------------

    def is_connected(self):

        return self.connected

    # --------------------------------------------------

    def read_signal(self):
        """
        Read one EEG window.

        Replace this method with the
        actual EEG SDK.

        Returns
        -------
        Raw EEG samples
        """

        if not self.connected:

            return None

        # -----------------------------------------------
        # Example placeholder
        # -----------------------------------------------

        raw_signal = []

        return raw_signal

    # --------------------------------------------------

    def get_next_command(self):
        """
        Complete EEG Pipeline
        """

        raw_signal = self.read_signal()

        if raw_signal is None:

            return None

        # -----------------------------------------------

        clean_signal = self.preprocessor.process(
            raw_signal
        )

        # -----------------------------------------------

        features = self.feature_extractor.extract(
            clean_signal
        )

        # -----------------------------------------------

        prediction = self.classifier.predict(
            features
        )

        # prediction example:
        #
        # {
        #     "command":"Right_Play_Pause",
        #     "confidence":0.93,
        #     "domain":"AI_ML"
        # }

        # -----------------------------------------------

        prediction = self.confidence_filter.validate(
            prediction
        )

        if prediction is None:

            return None

        # -----------------------------------------------

        command = {

            "command":
                prediction["command"],

            "confidence":
                prediction["confidence"],

            "domain":
                prediction.get(
                    "domain",
                    eeg_config.TARGET_DOMAIN
                ),

            "timestamp":
                time.time(),

            "source":
                "EEG"

        }

        return command