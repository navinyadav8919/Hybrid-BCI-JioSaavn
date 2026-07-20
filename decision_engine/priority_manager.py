"""
=========================================================
Hybrid BCI JioSaavn Automation
Priority Manager
=========================================================

Responsibilities
----------------
1. Assign priority to commands.
2. Assign priority to sources.
3. Generate final priority score.
4. Sort commands before execution.

=========================================================
"""

import logging


class PriorityManager:

    def __init__(self):

        self.command_priority = {

            "Drop": 100,

            "Right_Return_to_Home": 95,

            "Right_JioSaavn": 90,

            "Right_Search_Playlist": 85,

            "Right_Play_Pause": 80,

            "Right_Next_Song": 75,

            "Right_Previous_Song": 75,

            "Right_Volume_Up": 70,

            "Right_Volume_Down": 70

        }

        self.source_priority = {

            "EEG": 40,

            "VOICE": 35,

            "CHAT": 30,

            "JSON": 20

        }

        logging.info("Priority Manager Initialized")

    # -------------------------------------------------

    def calculate_priority(self, command):

        """
        Calculate final priority.
        """

        if command is None:
            return 0

        cmd = command.get("command", "")

        source = command.get("source", "JSON")

        confidence = command.get("confidence", 1.0)

        command_score = self.command_priority.get(cmd, 50)

        source_score = self.source_priority.get(source.upper(), 10)

        confidence_score = int(confidence * 10)

        total = command_score + source_score + confidence_score

        logging.info(
            f"{cmd} -> Priority = {total}"
        )

        return total

    # -------------------------------------------------

    def assign_priority(self, command):

        """
        Attach priority to command.
        """

        priority = self.calculate_priority(command)

        command["priority"] = priority

        return command

    # -------------------------------------------------

    def sort_commands(self, commands):

        """
        Highest priority first.
        """

        commands = [

            self.assign_priority(cmd)

            for cmd in commands

        ]

        commands.sort(

            key=lambda x: x["priority"],

            reverse=True

        )

        return commands

    # -------------------------------------------------

    def get_command_priority(self, command):

        return self.command_priority.get(command, 0)

    # -------------------------------------------------

    def get_source_priority(self, source):

        return self.source_priority.get(source.upper(), 0)

    # -------------------------------------------------

    def register_command_priority(self,

                                  command,

                                  priority):

        self.command_priority[command] = priority

    # -------------------------------------------------

    def register_source_priority(self,

                                 source,

                                 priority):

        self.source_priority[source.upper()] = priority