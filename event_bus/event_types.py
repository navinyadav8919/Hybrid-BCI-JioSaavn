"""
=========================================================
Hybrid BCI JioSaavn Automation
Event Types
=========================================================

This module contains all event names used throughout
the application.

Using constants avoids spelling mistakes and makes
the Event Bus easier to maintain.

=========================================================
"""


class EventTypes:
    """
    Event constants.
    """

    # =====================================================
    # SESSION EVENTS
    # =====================================================

    SESSION_STARTED = "session_started"
    SESSION_STOPPED = "session_stopped"
    SESSION_PAUSED = "session_paused"
    SESSION_RESUMED = "session_resumed"

    # =====================================================
    # INPUT EVENTS
    # =====================================================

    JSON_RECEIVED = "json_received"
    EEG_RECEIVED = "eeg_received"
    CHAT_RECEIVED = "chat_received"
    VOICE_RECEIVED = "voice_received"

    # =====================================================
    # PROCESSING EVENTS
    # =====================================================

    PREPROCESSING_STARTED = "preprocessing_started"
    PREPROCESSING_COMPLETED = "preprocessing_completed"

    FEATURES_EXTRACTED = "features_extracted"

    CLASSIFICATION_STARTED = "classification_started"
    CLASSIFICATION_COMPLETED = "classification_completed"

    PREDICTION_GENERATED = "prediction_generated"
    PREDICTION_FILTERED = "prediction_filtered"
    PREDICTION_SMOOTHED = "prediction_smoothed"

    # =====================================================
    # COMMAND EVENTS
    # =====================================================

    COMMAND_GENERATED = "command_generated"
    COMMAND_VALIDATED = "command_validated"
    COMMAND_REJECTED = "command_rejected"
    COMMAND_STANDARDIZED = "command_standardized"
    COMMAND_ARBITRATED = "command_arbitrated"
    COMMAND_PRIORITY_ASSIGNED = "command_priority_assigned"

    # =====================================================
    # DECISION EVENTS
    # =====================================================

    DECISION_READY = "decision_ready"
    DECISION_REJECTED = "decision_rejected"

    # =====================================================
    # EXECUTION EVENTS
    # =====================================================

    EXECUTION_STARTED = "execution_started"
    EXECUTION_COMPLETED = "execution_completed"
    EXECUTION_FAILED = "execution_failed"

    # =====================================================
    # PLATFORM EVENTS
    # =====================================================

    PLATFORM_SELECTED = "platform_selected"
    PLATFORM_CHANGED = "platform_changed"

    # =====================================================
    # ANDROID EVENTS
    # =====================================================

    ANDROID_CONNECTED = "android_connected"
    ANDROID_DISCONNECTED = "android_disconnected"

    APK_LAUNCHED = "apk_launched"
    APK_CLOSED = "apk_closed"

    # =====================================================
    # WEBSITE EVENTS
    # =====================================================

    WEBSITE_CONNECTED = "website_connected"
    WEBSITE_DISCONNECTED = "website_disconnected"

    WEBSITE_OPENED = "website_opened"
    WEBSITE_CLOSED = "website_closed"

    # =====================================================
    # MQTT EVENTS
    # =====================================================

    MQTT_CONNECTED = "mqtt_connected"
    MQTT_DISCONNECTED = "mqtt_disconnected"

    MQTT_MESSAGE_SENT = "mqtt_message_sent"
    MQTT_MESSAGE_RECEIVED = "mqtt_message_received"

    HEARTBEAT_RECEIVED = "heartbeat_received"
    HEARTBEAT_TIMEOUT = "heartbeat_timeout"

    # =====================================================
    # PLAYER EVENTS
    # =====================================================

    PLAYER_OPENED = "player_opened"
    PLAYER_CLOSED = "player_closed"

    SONG_STARTED = "song_started"
    SONG_PAUSED = "song_paused"
    SONG_RESUMED = "song_resumed"
    SONG_STOPPED = "song_stopped"

    SONG_CHANGED = "song_changed"

    PLAYLIST_SEARCH_STARTED = "playlist_search_started"
    PLAYLIST_SEARCH_COMPLETED = "playlist_search_completed"

    PLAYLIST_SELECTED = "playlist_selected"

    VOLUME_CHANGED = "volume_changed"

    # =====================================================
    # ANALYTICS EVENTS
    # =====================================================

    LOG_CREATED = "log_created"
    HISTORY_UPDATED = "history_updated"

    # =====================================================
    # ERROR EVENTS
    # =====================================================

    ERROR_OCCURRED = "error_occurred"
    WARNING_OCCURRED = "warning_occurred"

    # =====================================================
    # SYSTEM EVENTS
    # =====================================================

    SYSTEM_READY = "system_ready"
    SYSTEM_SHUTDOWN = "system_shutdown"