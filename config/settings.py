"""
=========================================================
Hybrid BCI JioSaavn Automation
Global Application Settings
=========================================================

This file is the single source of truth for all
application settings.

Priority:
1. Environment Variables (.env)
2. Default values in this file
=========================================================
"""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global Application Configuration
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # =====================================================
    # PROJECT
    # =====================================================

    PROJECT_NAME: str = "Hybrid BCI JioSaavn"

    VERSION: str = "1.0.0"

    DEBUG: bool = True

    # =====================================================
    # DATA PATHS
    # =====================================================

    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    DATA_DIR: Path = BASE_DIR / "data"

    LOG_DIR: Path = BASE_DIR / "logs"

    MODEL_DIR: Path = DATA_DIR / "trained_models"

    JSON_DATASET: Path = DATA_DIR / "integrated_eeg.json"

    # =====================================================
    # INPUT SOURCE
    # =====================================================

    INPUT_SOURCE: str = "JSON"
    # JSON
    # EEG
    # CHAT
    # VOICE

    # =====================================================
    # PLATFORM
    # =====================================================

    PLATFORM_MODE: str = "AUTO"
    # AUTO
    # ANDROID
    # WEBSITE

    DEFAULT_PLATFORM: str = "ANDROID"

    # =====================================================
    # MQTT
    # =====================================================

    MQTT_BROKER: str = "broker.emqx.io"

    MQTT_PORT: int = 1883

    MQTT_KEEPALIVE: int = 60

    MQTT_QOS: int = 1

    MQTT_CLIENT_PREFIX: str = "BCI"

    # =====================================================
    # MQTT TOPICS
    # =====================================================

    TOPIC_COMMAND: str = "bci/ml/commands"

    TOPIC_CONTROL: str = "bci/ml/control"

    TOPIC_ACK: str = "bci/ml/ack"

    TOPIC_STATUS: str = "bci/ml/status"

    TOPIC_HEARTBEAT: str = "bci/ml/heartbeat"

    # =====================================================
    # EEG
    # =====================================================

    CONFIDENCE_THRESHOLD: float = 0.75

    SAMPLE_RATE: int = 128

    WINDOW_SECONDS: int = 5

    SMOOTHING_WINDOW: int = 3

    # =====================================================
    # COMMAND
    # =====================================================

    COMMAND_DELAY: float = 2.0

    COMMAND_TIMEOUT: int = 10

    COOLDOWN_SECONDS: int = 2

    MAX_RETRY_COUNT: int = 3

    # =====================================================
    # HEARTBEAT
    # =====================================================

    HEARTBEAT_INTERVAL: int = 30

    # =====================================================
    # WEBSITE
    # =====================================================

    WEBSITE_NAME: str = "JioSaavn"

    WEBSITE_URL: str = "https://www.jiosaavn.com"

    BROWSER: str = "chrome"

    HEADLESS: bool = False

    PAGE_LOAD_TIMEOUT: int = 30

    # =====================================================
    # CHAT
    # =====================================================

    CHAT_ENABLED: bool = True

    VOICE_ENABLED: bool = False

    # =====================================================
    # EXECUTION
    # =====================================================

    ENABLE_ACK: bool = True

    ENABLE_LOGGING: bool = True

    ENABLE_ANALYTICS: bool = True

    ENABLE_HISTORY: bool = True

    ENABLE_COOLDOWN: bool = True

    ENABLE_PLATFORM_DETECTION: bool = True

    # =====================================================
    # LOGGING
    # =====================================================

    LOG_LEVEL: str = "INFO"

    LOG_FILE: str = "application.log"

    # =====================================================
    # DETECTION
    # =====================================================

    PLATFORM_CHECK_INTERVAL: int = 5

    NETWORK_TIMEOUT: int = 5

    # =====================================================
    # SESSION
    # =====================================================

    SESSION_TIMEOUT: int = 1800

    SAVE_HISTORY: bool = True


settings = Settings()