"""
=========================================================
Hybrid BCI JioSaavn Automation
JSON Provider
=========================================================

Responsibilities
----------------
1. Read integrated_eeg.json
2. Filter AI_ML commands
3. Return one command at a time
4. Present commands in a standard format

This provider is only for testing.

Later it will be replaced by eeg_provider.py
without changing the remaining architecture.

=========================================================
"""

import json
import time
import logging

from config.eeg_config import eeg_config


class JsonProvider:

    def __init__(self):

        self.dataset = []

        self.current_index = 0

        self.load_dataset()

    # --------------------------------------------------

    def load_dataset(self):

        """
        Load JSON dataset.
        """

        try:

            with open(
                eeg_config.DATASET_PATH,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            if "data" not in data:

                raise ValueError(
                    "Dataset does not contain 'data' section."
                )

            self.dataset = [

                entry

                for entry in data["data"]

                if entry.get(
                    eeg_config.KEY_DOMAIN
                ) == eeg_config.TARGET_DOMAIN

            ]

            logging.info(
                f"{len(self.dataset)} AI_ML commands loaded."
            )

        except Exception as e:

            logging.exception(e)

            self.dataset = []

    # --------------------------------------------------

    def get_next_command(self):

        """
        Return next command.

        Returns None when dataset finishes.
        """

        if self.current_index >= len(self.dataset):

            logging.info(
                "Dataset completed."
            )

            return None

        entry = self.dataset[self.current_index]

        self.current_index += 1

        command = {

            "command":
                entry.get(
                    eeg_config.KEY_COMMAND
                ),

            "confidence":
                entry.get(
                    eeg_config.KEY_CONFIDENCE,
                    0.0
                ),

            "domain":
                entry.get(
                    eeg_config.KEY_DOMAIN
                ),

            "timestamp":
                entry.get(
                    eeg_config.KEY_TIMESTAMP,
                    time.time()
                ),

            "operation":
                entry.get(
                    eeg_config.KEY_OPERATION,
                    ""
                ),

            "sample":
                entry.get(
                    eeg_config.KEY_SAMPLE,
                    0
                ),

            "state":
                entry.get(
                    eeg_config.KEY_STATE,
                    0
                ),

            "source":
                "JSON"

        }

        return command

    # --------------------------------------------------

    def has_next(self):

        """
        Check if more commands are available.
        """

        return self.current_index < len(self.dataset)

    # --------------------------------------------------

    def reset(self):

        """
        Restart dataset streaming.
        """

        self.current_index = 0

        logging.info(
            "Dataset reset."
        )

    # --------------------------------------------------

    def total_commands(self):

        return len(self.dataset)

    # --------------------------------------------------

    def current_position(self):

        return self.current_index