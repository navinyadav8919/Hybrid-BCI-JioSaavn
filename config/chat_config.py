"""
=========================================================
Hybrid BCI JioSaavn Automation
Chat Configuration
=========================================================

This module contains all Chat Interface settings.

Used By
-------
chat_interface.py
intent_parser.py
task_planner.py
context_manager.py
execution_manager.py
=========================================================
"""

from dataclasses import dataclass
from config.settings import settings


@dataclass(frozen=True)
class ChatConfig:
    """
    Chat Interface Configuration
    """

    # =====================================================
    # Chat Enable
    # =====================================================

    ENABLE_CHAT = settings.CHAT_ENABLED

    ENABLE_VOICE = settings.VOICE_ENABLED

    # =====================================================
    # Input
    # =====================================================

    MAX_MESSAGE_LENGTH = 500

    MIN_MESSAGE_LENGTH = 1

    DEFAULT_LANGUAGE = "en"

    SUPPORTED_LANGUAGES = [
        "en",
        "hi",
        "te"
    ]

    # =====================================================
    # Intent Recognition
    # =====================================================

    ENABLE_INTENT_PARSER = True

    ENABLE_ENTITY_EXTRACTION = True

    ENABLE_CONTEXT_MEMORY = True

    # =====================================================
    # Task Planner
    # =====================================================

    ENABLE_TASK_PLANNER = True

    ENABLE_MULTI_STEP_TASKS = True

    MAX_TASKS = 20

    # =====================================================
    # Platform Preference
    # =====================================================

    DEFAULT_PLATFORM = settings.DEFAULT_PLATFORM

    PLATFORM_MODE = settings.PLATFORM_MODE

    # =====================================================
    # Confirmation
    # =====================================================

    ASK_CONFIRMATION_FOR_LOW_CONFIDENCE = True

    CONFIDENCE_THRESHOLD = settings.CONFIDENCE_THRESHOLD

    # =====================================================
    # Conversation
    # =====================================================

    MAX_HISTORY = 50

    SESSION_TIMEOUT = settings.SESSION_TIMEOUT

    SAVE_HISTORY = settings.SAVE_HISTORY

    # =====================================================
    # Supported Intents
    # =====================================================

    SUPPORTED_INTENTS = [

        "PLAY",

        "PAUSE",

        "RESUME",

        "NEXT",

        "PREVIOUS",

        "SEARCH",

        "PLAY_ARTIST",

        "PLAY_ALBUM",

        "PLAY_PLAYLIST",

        "PLAY_SONG",

        "VOLUME_UP",

        "VOLUME_DOWN",

        "MUTE",

        "UNMUTE",

        "STOP",

        "OPEN_JIOSAAVN",

        "CLOSE_JIOSAAVN",

        "SWITCH_PLATFORM"

    ]

    # =====================================================
    # Supported Applications
    # =====================================================

    SUPPORTED_APPLICATIONS = [

        "JioSaavn"

    ]

    # =====================================================
    # Logging
    # =====================================================

    LOG_CHAT_MESSAGES = True

    LOG_TASKS = True

    LOG_INTENTS = True

    LOG_CONTEXT = True

    # =====================================================
    # Response Messages
    # =====================================================

    SUCCESS_MESSAGE = "Task created successfully."

    ERROR_MESSAGE = "Unable to understand your request."

    UNKNOWN_INTENT = "Unknown command."

    CONFIRMATION_MESSAGE = "Please confirm your request."

    # =====================================================
    # Future AI Assistant
    # =====================================================

    ENABLE_LLM = False

    MODEL_NAME = ""

    API_KEY = ""


# Singleton instance

chat_config = ChatConfig()