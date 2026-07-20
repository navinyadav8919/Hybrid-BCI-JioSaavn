"""
=========================================================
Hybrid BCI JioSaavn Automation
Standard Command Generator
=========================================================

Responsibilities
----------------
1. Convert all input formats into a standard command.
2. Normalize command names.
3. Add metadata.
4. Produce a unified command object.

=========================================================
"""

import time
import logging


class StandardCommandGenerator:

    def __init__(self):

        self.command_map = {

            # -------------------------
            # Playback
            # -------------------------

            "PLAY": "Right_Play_Pause",
            "PAUSE": "Right_Play_Pause",
            "PLAY_PAUSE": "Right_Play_Pause",
            "RIGHT_PLAY_PAUSE": "Right_Play_Pause",

            # -------------------------
            # Next
            # -------------------------

            "NEXT": "Right_Next_Song",
            "NEXT SONG": "Right_Next_Song",
            "NEXT_TRACK": "Right_Next_Song",
            "RIGHT_NEXT_SONG": "Right_Next_Song",

            # -------------------------
            # Previous
            # -------------------------

            "PREVIOUS": "Right_Previous_Song",
            "PREVIOUS SONG": "Right_Previous_Song",
            "PREV": "Right_Previous_Song",
            "RIGHT_PREVIOUS_SONG": "Right_Previous_Song",

            # -------------------------
            # Volume
            # -------------------------

            "VOLUME UP": "Right_Volume_Up",
            "VOLUME_UP": "Right_Volume_Up",
            "RIGHT_VOLUME_UP": "Right_Volume_Up",

            "VOLUME DOWN": "Right_Volume_Down",
            "VOLUME_DOWN": "Right_Volume_Down",
            "RIGHT_VOLUME_DOWN": "Right_Volume_Down",

            # -------------------------
            # Search
            # -------------------------

            "SEARCH": "Right_Search_Playlist",
            "SEARCH PLAYLIST": "Right_Search_Playlist",
            "RIGHT_SEARCH_PLAYLIST": "Right_Search_Playlist",

            # -------------------------
            # Launch
            # -------------------------

            "JIOSAAVN": "Right_JioSaavn",
            "OPEN JIOSAAVN": "Right_JioSaavn",
            "RIGHT_JIOSAAVN": "Right_JioSaavn",

            # -------------------------
            # Home
            # -------------------------

            "HOME": "Right_Return_to_Home",
            "RETURN HOME": "Right_Return_to_Home",
            "RIGHT_RETURN_TO_HOME": "Right_Return_to_Home",

            # -------------------------
            # Drop
            # -------------------------

            "DROP": "Drop"
        }

        logging.info("Standard Command Generator Initialized")

    # -------------------------------------------------

    def generate(self,
                 command,
                 source="UNKNOWN",
                 confidence=1.0,
                 platform="AUTO",
                 metadata=None):
        """
        Generate standard command object.
        """

        if not command:

            return None

        normalized = self.normalize(command)

        standard_command = {

            "command": normalized,

            "source": source,

            "confidence": confidence,

            "platform": platform,

            "timestamp": time.time(),

            "metadata": metadata or {}

        }

        logging.info(
            f"Generated Standard Command : {normalized}"
        )

        return standard_command

    # -------------------------------------------------

    def normalize(self, command):

        """
        Normalize command names.
        """

        cmd = command.upper().strip()

        cmd = cmd.replace("-", "_")

        cmd = cmd.replace("__", "_")

        return self.command_map.get(cmd, command)

    # -------------------------------------------------

    def is_supported(self, command):

        cmd = command.upper().strip()

        return cmd in self.command_map

    # -------------------------------------------------

    def get_supported_commands(self):

        return sorted(set(self.command_map.values()))

    # -------------------------------------------------

    def register_command(self,
                         alias,
                         standard_command):
        """
        Register new command dynamically.
        """

        self.command_map[alias.upper()] = standard_command

        logging.info(
            f"Registered Alias : {alias} -> {standard_command}"
        )