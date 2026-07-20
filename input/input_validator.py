"""
=========================================================
Hybrid BCI JioSaavn Automation
Input Validator
=========================================================

Responsibilities
----------------
1. Validate incoming commands/tasks.
2. Check mandatory fields.
3. Validate confidence score.
4. Validate supported commands.
5. Return True/False.

Used By
-------
Input Manager
Decision Engine

=========================================================
"""

import logging

from config.settings import settings
from config.constants import (
    SUPPORTED_BCI_COMMANDS,
    INPUT_JSON,
    INPUT_EEG,
    INPUT_CHAT,
    INPUT_VOICE,
)


class InputValidator:

    def __init__(self):

        logging.info("Input Validator Initialized")

    # --------------------------------------------------

    def validate(self, command):

        """
        Validate incoming command/task.

        Parameters
        ----------
        command : dict

        Returns
        -------
        bool
        """

        if command is None:

            logging.warning("Received empty command.")

            return False

        if not isinstance(command, dict):

            logging.error("Command must be a dictionary.")

            return False

        source = command.get("source")

        if source not in [

            INPUT_JSON,

            INPUT_EEG,

            INPUT_CHAT,

            INPUT_VOICE

        ]:

            logging.error(f"Unknown source : {source}")

            return False

        # --------------------------------------------
        # Chat / Voice Validation
        # --------------------------------------------

        if source in [INPUT_CHAT, INPUT_VOICE]:

            return self.validate_task(command)

        # --------------------------------------------
        # JSON / EEG Validation
        # --------------------------------------------

        return self.validate_bci_command(command)

    # --------------------------------------------------

    def validate_bci_command(self, command):

        """
        Validate BCI command.
        """

        required_fields = [

            "command",

            "confidence",

            "source"

        ]

        for field in required_fields:

            if field not in command:

                logging.error(
                    f"Missing field : {field}"
                )

                return False

        confidence = command["confidence"]

        if not isinstance(confidence, (float, int)):

            logging.error("Confidence is invalid.")

            return False

        if confidence < settings.CONFIDENCE_THRESHOLD:

            logging.warning(

                f"Low Confidence : {confidence}"

            )

            return False

        if command["command"] not in SUPPORTED_BCI_COMMANDS:

            logging.warning(

                f"Unsupported Command : {command['command']}"

            )

            return False

        return True

    # --------------------------------------------------

    def validate_task(self, command):

        """
        Validate Chat/Voice task.
        """

        if "task" not in command:

            logging.error("Task missing.")

            return False

        task = command["task"]

        required_fields = [

            "task_id",

            "intent",

            "platform",

            "status"

        ]

        for field in required_fields:

            if field not in task:

                logging.error(

                    f"Task missing : {field}"

                )

                return False

        return True

    # --------------------------------------------------

    def is_supported_command(self, cmd):

        """
        Check supported BCI command.
        """

        return cmd in SUPPORTED_BCI_COMMANDS

    # --------------------------------------------------

    def print_validation(self, command):

        """
        Print validation result.
        """

        valid = self.validate(command)

        if valid:

            logging.info("Input Validation Passed")

        else:

            logging.warning("Input Validation Failed")

        return valid