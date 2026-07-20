"""
=========================================================
Hybrid BCI JioSaavn Automation
Application Constants
=========================================================

This module contains project-wide constants.

Only immutable values should be stored here.

Used By
-------
Entire Application
=========================================================
"""

# =========================================================
# PROJECT
# =========================================================

PROJECT_NAME = "Hybrid BCI JioSaavn"

VERSION = "1.0.0"

AUTHOR = "Ragam Naveen"

# =========================================================
# INPUT SOURCES
# =========================================================

INPUT_JSON = "JSON"

INPUT_EEG = "EEG"

INPUT_CHAT = "CHAT"

INPUT_VOICE = "VOICE"

# =========================================================
# DOMAINS
# =========================================================

DOMAIN_AI_ML = "AI_ML"

DOMAIN_IOT = "IoT"

DOMAIN_PYTHON = "Python"

DOMAIN_EMBEDDED = "Embedded"

# =========================================================
# PLATFORM
# =========================================================

PLATFORM_AUTO = "AUTO"

PLATFORM_ANDROID = "ANDROID"

PLATFORM_WEBSITE = "WEBSITE"

# =========================================================
# APPLICATIONS
# =========================================================

APP_JIOSAAVN = "JioSaavn"

APP_ANDROID = "Android"

APP_WEBSITE = "Website"

# =========================================================
# EXECUTION STATUS
# =========================================================

STATUS_PENDING = "PENDING"

STATUS_RUNNING = "RUNNING"

STATUS_SUCCESS = "SUCCESS"

STATUS_FAILED = "FAILED"

STATUS_RETRY = "RETRY"

STATUS_COMPLETED = "COMPLETED"

# =========================================================
# MQTT STATUS
# =========================================================

MQTT_CONNECTED = "CONNECTED"

MQTT_DISCONNECTED = "DISCONNECTED"

MQTT_RECONNECTING = "RECONNECTING"

# =========================================================
# BCI COMMANDS
# =========================================================

CMD_PLAY = "Right_Play_Pause"

CMD_NEXT = "Right_Next_Song"

CMD_PREVIOUS = "Right_Previous_Song"

CMD_VOLUME_UP = "Right_Volume_Up"

CMD_VOLUME_DOWN = "Right_Volume_Down"

CMD_SEARCH = "Right_Search_Playlist"

CMD_OPEN_APP = "Right_JioSaavn"

CMD_HOME = "Right_Return_to_Home"

CMD_DROP = "Drop"

# =========================================================
# CHAT INTENTS
# =========================================================

INTENT_PLAY = "PLAY"

INTENT_PAUSE = "PAUSE"

INTENT_RESUME = "RESUME"

INTENT_NEXT = "NEXT"

INTENT_PREVIOUS = "PREVIOUS"

INTENT_SEARCH = "SEARCH"

INTENT_PLAY_SONG = "PLAY_SONG"

INTENT_PLAY_ARTIST = "PLAY_ARTIST"

INTENT_PLAY_PLAYLIST = "PLAY_PLAYLIST"

INTENT_VOLUME_UP = "VOLUME_UP"

INTENT_VOLUME_DOWN = "VOLUME_DOWN"

INTENT_OPEN = "OPEN"

INTENT_CLOSE = "CLOSE"

INTENT_STOP = "STOP"

# =========================================================
# JSON KEYS
# =========================================================

KEY_COMMAND = "command"

KEY_CONFIDENCE = "confidence"

KEY_DOMAIN = "domain"

KEY_TIMESTAMP = "timestamp"

KEY_OPERATION = "operation"

KEY_SAMPLE = "sample"

KEY_STATE = "state"

KEY_PLATFORM = "platform"

KEY_SOURCE = "source"

KEY_INTENT = "intent"

KEY_TASK = "task"

# =========================================================
# EVENT BUS EVENTS
# =========================================================

EVENT_COMMAND_RECEIVED = "COMMAND_RECEIVED"

EVENT_COMMAND_VALIDATED = "COMMAND_VALIDATED"

EVENT_TASK_CREATED = "TASK_CREATED"

EVENT_TASK_COMPLETED = "TASK_COMPLETED"

EVENT_PLATFORM_SELECTED = "PLATFORM_SELECTED"

EVENT_EXECUTION_STARTED = "EXECUTION_STARTED"

EVENT_EXECUTION_FINISHED = "EXECUTION_FINISHED"

EVENT_ACK_RECEIVED = "ACK_RECEIVED"

# =========================================================
# SESSION
# =========================================================

SESSION_ACTIVE = "ACTIVE"

SESSION_IDLE = "IDLE"

SESSION_EXPIRED = "EXPIRED"

# =========================================================
# LOGGING
# =========================================================

LOG_INFO = "INFO"

LOG_WARNING = "WARNING"

LOG_ERROR = "ERROR"

LOG_DEBUG = "DEBUG"

# =========================================================
# SUPPORTED COMMANDS
# =========================================================

SUPPORTED_BCI_COMMANDS = [

    CMD_PLAY,

    CMD_NEXT,

    CMD_PREVIOUS,

    CMD_VOLUME_UP,

    CMD_VOLUME_DOWN,

    CMD_SEARCH,

    CMD_OPEN_APP,

    CMD_HOME,

    CMD_DROP

]

# =========================================================
# SUPPORTED PLATFORMS
# =========================================================

SUPPORTED_PLATFORMS = [

    PLATFORM_ANDROID,

    PLATFORM_WEBSITE

]

# =========================================================
# SUPPORTED INPUT SOURCES
# =========================================================

SUPPORTED_INPUTS = [

    INPUT_JSON,

    INPUT_EEG,

    INPUT_CHAT,

    INPUT_VOICE

]