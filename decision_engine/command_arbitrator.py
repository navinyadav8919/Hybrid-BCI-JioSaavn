"""
=========================================================
Hybrid BCI JioSaavn Automation
Command Arbitrator
=========================================================

Responsibilities
----------------
1. Resolve command conflicts.
2. Prioritize command sources.
3. Remove duplicate commands.
4. Return one final command.

Priority

VOICE > CHAT > EEG > JSON

=========================================================
"""

import logging
import time


class CommandArbitrator:

    def __init__(self):

        self.priority = {

            "VOICE": 4,

            "CHAT": 3,

            "EEG": 2,

            "JSON": 1

        }

        self.last_command = None

        self.last_timestamp = 0

        logging.info("Command Arbitrator Initialized")

    # -------------------------------------------------

    def arbitrate(self, commands):

        """
        commands : list

        Example

        [
            {
                "command":"Right_Play_Pause",
                "source":"EEG",
                "confidence":0.91
            },

            {
                "command":"Right_Play_Pause",
                "source":"CHAT"
            }

        ]
        """

        if not commands:

            return None

        # Remove duplicates

        commands = self.remove_duplicates(commands)

        # Highest priority first

        commands.sort(

            key=lambda x: self.priority.get(

                x.get("source", "JSON"),

                0

            ),

            reverse=True

        )

        selected = commands[0]

        self.last_command = selected

        self.last_timestamp = time.time()

        logging.info(

            f"Selected Command : "

            f"{selected['command']} "

            f"({selected['source']})"

        )

        return selected

    # -------------------------------------------------

    def remove_duplicates(self, commands):

        """
        Remove duplicate commands.
        """

        unique = {}

        for command in commands:

            key = command.get("command")

            if key not in unique:

                unique[key] = command

            else:

                current = unique[key]

                current_priority = self.priority.get(

                    current.get("source"),

                    0

                )

                new_priority = self.priority.get(

                    command.get("source"),

                    0

                )

                if new_priority > current_priority:

                    unique[key] = command

        return list(unique.values())

    # -------------------------------------------------

    def last_executed(self):

        return self.last_command

    # -------------------------------------------------

    def clear(self):

        self.last_command = None

        self.last_timestamp = 0