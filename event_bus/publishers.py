"""
=========================================================
Hybrid BCI JioSaavn Automation
Publishers
=========================================================

Responsibilities
----------------
1. Publish all application events.
2. Hide EventBus implementation details.
3. Provide easy-to-use publishing methods.
4. Standardize event publishing.

=========================================================
"""

import logging

from event_bus.event_dispatcher import EventDispatcher
from event_bus.event_types import EventTypes


class Publishers:

    def __init__(self, dispatcher: EventDispatcher):

        self.dispatcher = dispatcher

        logging.info("Publishers Initialized")

    # =====================================================
    # SESSION EVENTS
    # =====================================================

    def session_started(self, session):

        self.dispatcher.dispatch(
            EventTypes.SESSION_STARTED,
            session
        )

    def session_stopped(self, session):

        self.dispatcher.dispatch(
            EventTypes.SESSION_STOPPED,
            session
        )

    # =====================================================
    # INPUT EVENTS
    # =====================================================

    def eeg_received(self, eeg):

        self.dispatcher.dispatch(
            EventTypes.EEG_RECEIVED,
            eeg
        )

    def json_received(self, data):

        self.dispatcher.dispatch(
            EventTypes.JSON_RECEIVED,
            data
        )

    def chat_received(self, chat):

        self.dispatcher.dispatch(
            EventTypes.CHAT_RECEIVED,
            chat
        )

    def voice_received(self, voice):

        self.dispatcher.dispatch(
            EventTypes.VOICE_RECEIVED,
            voice
        )

    # =====================================================
    # PROCESSING EVENTS
    # =====================================================

    def features_extracted(self, features):

        self.dispatcher.dispatch(
            EventTypes.FEATURES_EXTRACTED,
            features
        )

    def prediction_generated(self, prediction):

        self.dispatcher.dispatch(
            EventTypes.PREDICTION_GENERATED,
            prediction
        )

    def prediction_filtered(self, prediction):

        self.dispatcher.dispatch(
            EventTypes.PREDICTION_FILTERED,
            prediction
        )

    def prediction_smoothed(self, prediction):

        self.dispatcher.dispatch(
            EventTypes.PREDICTION_SMOOTHED,
            prediction
        )

    # =====================================================
    # COMMAND EVENTS
    # =====================================================

    def command_generated(self, command):

        self.dispatcher.dispatch(
            EventTypes.COMMAND_GENERATED,
            command
        )

    def command_validated(self, command):

        self.dispatcher.dispatch(
            EventTypes.COMMAND_VALIDATED,
            command
        )

    def command_rejected(self, command):

        self.dispatcher.dispatch(
            EventTypes.COMMAND_REJECTED,
            command
        )

    # =====================================================
    # DECISION EVENTS
    # =====================================================

    def decision_ready(self, decision):

        self.dispatcher.dispatch(
            EventTypes.DECISION_READY,
            decision
        )

    # =====================================================
    # EXECUTION EVENTS
    # =====================================================

    def execution_started(self, command):

        self.dispatcher.dispatch(
            EventTypes.EXECUTION_STARTED,
            command
        )

    def execution_completed(self, result):

        self.dispatcher.dispatch(
            EventTypes.EXECUTION_COMPLETED,
            result
        )

    def execution_failed(self, error):

        self.dispatcher.dispatch(
            EventTypes.EXECUTION_FAILED,
            error
        )

    # =====================================================
    # PLATFORM EVENTS
    # =====================================================

    def platform_changed(self, platform):

        self.dispatcher.dispatch(
            EventTypes.PLATFORM_CHANGED,
            platform
        )

    # =====================================================
    # MQTT EVENTS
    # =====================================================

    def mqtt_connected(self):

        self.dispatcher.dispatch(
            EventTypes.MQTT_CONNECTED
        )

    def mqtt_disconnected(self):

        self.dispatcher.dispatch(
            EventTypes.MQTT_DISCONNECTED
        )

    def mqtt_message_sent(self, message):

        self.dispatcher.dispatch(
            EventTypes.MQTT_MESSAGE_SENT,
            message
        )

    def mqtt_message_received(self, message):

        self.dispatcher.dispatch(
            EventTypes.MQTT_MESSAGE_RECEIVED,
            message
        )

    # =====================================================
    # PLAYER EVENTS
    # =====================================================

    def song_started(self, song):

        self.dispatcher.dispatch(
            EventTypes.SONG_STARTED,
            song
        )

    def song_paused(self, song):

        self.dispatcher.dispatch(
            EventTypes.SONG_PAUSED,
            song
        )

    def song_changed(self, song):

        self.dispatcher.dispatch(
            EventTypes.SONG_CHANGED,
            song
        )

    def volume_changed(self, volume):

        self.dispatcher.dispatch(
            EventTypes.VOLUME_CHANGED,
            volume
        )

    def playlist_search_started(self, playlist):

        self.dispatcher.dispatch(
            EventTypes.PLAYLIST_SEARCH_STARTED,
            playlist
        )

    def playlist_search_completed(self, playlist):

        self.dispatcher.dispatch(
            EventTypes.PLAYLIST_SEARCH_COMPLETED,
            playlist
        )

    # =====================================================
    # ERROR EVENTS
    # =====================================================

    def error(self, error):

        self.dispatcher.dispatch(
            EventTypes.ERROR_OCCURRED,
            error
        )

    def warning(self, warning):

        self.dispatcher.dispatch(
            EventTypes.WARNING_OCCURRED,
            warning
        )