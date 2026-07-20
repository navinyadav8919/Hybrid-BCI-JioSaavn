"""
=========================================================
Hybrid BCI JioSaavn Automation
Command Validator
=========================================================

Responsibilities
----------------
1. Validate command structure.
2. Validate confidence value.
3. Validate platform.
4. Validate source.
5. Prevent invalid commands entering the system.

=========================================================
"""

import logging


class CommandValidator:

    def __init__(self):

        self.supported_commands = {

            "Right_JioSaavn",

            "Right_Play_Pause",

            "Right_Next_Song",

            "Right_Previous_Song",

            "Right_Volume_Up",

            "Right_Volume_Down",

            "Right_Search_Playlist",

            "Right_Return_to_Home",

            "Drop"

        }

        self.supported_sources = {

            "EEG",

            "JSON",

            "CHAT",

            "VOICE"

        }

        self.supported_platforms = {

            "AUTO",

            "ANDROID",

            "WEBSITE"

        }

        logging.info("Command Validator Initialized")

    # -----------------------------------------------------

    def validate(self, command):

        """
        Validate a standard command object.
        """

        if command is None:

            return False, "Command is None"

        # -------------------------------------------------
        # Required fields
        # -------------------------------------------------

        required_fields = [

            "command",

            "source",

            "confidence",

            "platform"

        ]

        for field in required_fields:

            if field not in command:

                return False, f"Missing field : {field}"

        # -------------------------------------------------
        # Command validation
        # -------------------------------------------------

        cmd = command["command"]

        if cmd not in self.supported_commands:

            return False, f"Unsupported command : {cmd}"

        # -------------------------------------------------
        # Confidence validation
        # -------------------------------------------------

        confidence = command["confidence"]

        if not isinstance(confidence, (int, float)):

            return False, "Confidence must be numeric"

        if confidence < 0 or confidence > 1:

            return False, "Confidence must be between 0 and 1"

        # -------------------------------------------------
        # Source validation
        # -------------------------------------------------

        source = command["source"]

        if source not in self.supported_sources:

            return False, f"Unsupported source : {source}"

        # -------------------------------------------------
        # Platform validation
        # -------------------------------------------------

        platform = command["platform"]

        if platform not in self.supported_platforms:

            return False, f"Unsupported platform : {platform}"

        logging.info("Command validation successful.")

        return True, "Valid Command"

    # -----------------------------------------------------

    def is_supported_command(self, command):

        return command in self.supported_commands

    # -----------------------------------------------------

    def register_command(self, command):

        """
        Dynamically add a new command.
        """

        self.supported_commands.add(command)

        logging.info(f"Registered command : {command}")

    # -----------------------------------------------------

    def get_supported_commands(self):

        return sorted(self.supported_commands)

    # -----------------------------------------------------

    def get_supported_sources(self):

        return sorted(self.supported_sources)

    # -----------------------------------------------------

    def get_supported_platforms(self):

        return sorted(self.supported_platforms)