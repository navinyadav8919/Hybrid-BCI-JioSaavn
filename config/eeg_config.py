"""
=========================================================
Hybrid BCI JioSaavn Automation
EEG Configuration
=========================================================

This module contains all EEG-related settings used
throughout the application.

Used By
-------
json_provider.py
eeg_provider.py
preprocessing.py
feature_extraction.py
classifier.py
confidence_filter.py
prediction_smoother.py
=========================================================
"""

from dataclasses import dataclass
from pathlib import Path

from config.settings import settings


@dataclass(frozen=True)
class EEGConfig:
    """
    EEG Processing Configuration
    """

    # =====================================================
    # Input Source
    # =====================================================

    INPUT_SOURCE = settings.INPUT_SOURCE
    # JSON
    # EEG

    # =====================================================
    # Dataset
    # =====================================================

    DATASET_PATH = settings.JSON_DATASET

    # =====================================================
    # EEG Acquisition
    # =====================================================

    SAMPLE_RATE = settings.SAMPLE_RATE

    WINDOW_SECONDS = settings.WINDOW_SECONDS

    CHANNELS = 14

    OVERLAP_SECONDS = 0

    # =====================================================
    # Signal Processing
    # =====================================================

    LOWCUT_FREQUENCY = 0.5

    HIGHCUT_FREQUENCY = 40.0

    NOTCH_FREQUENCY = 50

    FILTER_ORDER = 4

    # =====================================================
    # Feature Extraction
    # =====================================================

    ENABLE_FEATURE_EXTRACTION = True

    FEATURE_METHOD = "PSD"

    FEATURE_VECTOR_SIZE = 128

    NORMALIZE_FEATURES = True

    # =====================================================
    # Classification
    # =====================================================

    MODEL_TYPE = "SVM"

    MODEL_PATH = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "trained_models"
        / "svm_model.pkl"
    )

    LABEL_ENCODER = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "trained_models"
        / "label_encoder.pkl"
    )

    SCALER = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "trained_models"
        / "scaler.pkl"
    )

    # =====================================================
    # Prediction
    # =====================================================

    CONFIDENCE_THRESHOLD = settings.CONFIDENCE_THRESHOLD

    ENABLE_PREDICTION_SMOOTHING = True

    SMOOTHING_WINDOW = settings.SMOOTHING_WINDOW

    # =====================================================
    # Command Validation
    # =====================================================

    IGNORE_LOW_CONFIDENCE = True

    MIN_CONSECUTIVE_PREDICTIONS = 2

    MAX_COMMAND_QUEUE = 20

    # =====================================================
    # JSON Keys
    # =====================================================

    KEY_COMMAND = "command"

    KEY_CONFIDENCE = "confidence"

    KEY_DOMAIN = "domain"

    KEY_TIMESTAMP = "timestamp"

    KEY_OPERATION = "operation"

    KEY_SAMPLE = "sample"

    KEY_STATE = "state"

    # =====================================================
    # Target Domain
    # =====================================================

    TARGET_DOMAIN = "AI_ML"

    # =====================================================
    # Realtime EEG
    # =====================================================

    ENABLE_REALTIME = False

    DEVICE_NAME = "Emotiv"

    SERIAL_PORT = ""

    BAUDRATE = 115200

    # =====================================================
    # Performance
    # =====================================================

    MAX_PROCESSING_TIME_MS = 100

    MAX_BUFFER_SIZE = 500

    # =====================================================
    # Logging
    # =====================================================

    SAVE_RAW_SIGNAL = False

    SAVE_FEATURES = False

    SAVE_PREDICTIONS = True

    LOG_EEG_PROCESSING = True


# Singleton Instance
eeg_config = EEGConfig()