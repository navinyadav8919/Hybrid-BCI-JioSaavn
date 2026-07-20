"""
=========================================================
Hybrid BCI JioSaavn Automation
Input Manager
=========================================================

The Input Manager is responsible for selecting the
active input source and returning standardized commands.

Supported Inputs

1. JSON Dataset
2. Live EEG
3. Chat
4. Voice

The remaining system never needs to know the source.

=========================================================
"""

import logging

from config.settings import settings
from config.constants import (
    INPUT_JSON,
    INPUT_EEG,
    INPUT_CHAT,
    INPUT_VOICE,
)

from input.json_provider import JsonProvider
from input.eeg_provider import EEGProvider
from input.chat_interface import ChatInterface
from input.voice_interface import VoiceInterface


class InputManager:

    def __init__(self):

        self.source = settings.INPUT_SOURCE.upper()

        logging.info(
            f"Input Source Selected : {self.source}"
        )

        self.provider = self.__create_provider()

    # --------------------------------------------------

    def __create_provider(self):

        """
        Create the appropriate provider.
        """

        if self.source == INPUT_JSON:

            return JsonProvider()

        elif self.source == INPUT_EEG:

            return EEGProvider()

        elif self.source == INPUT_CHAT:

            return ChatInterface()

        elif self.source == INPUT_VOICE:

            return VoiceInterface()

        raise ValueError(
            f"Unsupported Input Source : {self.source}"
        )

    # --------------------------------------------------

    def get_next_command(self):

        """
        Returns the next standardized command.
        """

        return self.provider.get_next_command()

    # --------------------------------------------------

    def reset(self):

        """
        Reset provider if supported.
        """

        if hasattr(self.provider, "reset"):

            self.provider.reset()

    # --------------------------------------------------

    def get_source(self):

        return self.source