"""
=========================================================
Hybrid BCI JioSaavn Automation
Decision Manager
=========================================================

Responsibilities
----------------
1. Validate incoming command.
2. Check current application context.
3. Decide execution platform.
4. Prevent duplicate execution.
5. Generate execution request.

=========================================================
"""

import time
import logging


class DecisionManager:

    def __init__(self,
                 context_manager):

        self.context = context_manager

        logging.info("Decision Manager Initialized")

    # --------------------------------------------------

    def decide(self, command):

        """
        Main decision function.
        """

        if command is None:

            return None

        cmd = command.get("command")

        source = command.get("source", "UNKNOWN")

        confidence = command.get("confidence", 1.0)

        # ------------------------------------------
        # Duplicate protection
        # ------------------------------------------

        last = self.context.get_last_command()

        if last["command"] == cmd:

            if last["time"] is not None:

                elapsed = time.time() - last["time"]

                if elapsed < 1.0:

                    logging.info(
                        "Duplicate command ignored."
                    )

                    return None

        # ------------------------------------------
        # Platform Selection
        # ------------------------------------------

        platform = self.select_platform()

        # ------------------------------------------
        # Context Decisions
        # ------------------------------------------

        if cmd == "Right_Next_Song":

            if not self.context.is_music_playing():

                logging.info(
                    "Music not playing."
                )

                cmd = "Right_Play_Pause"

        elif cmd == "Right_Previous_Song":

            if not self.context.is_music_playing():

                cmd = "Right_Play_Pause"

        elif cmd == "Right_Play_Pause":

            pass

        elif cmd == "Right_Search_Playlist":

            if not self.context.is_jiosaavn_open():

                logging.info(
                    "Opening JioSaavn first."
                )

                return {

                    "command": "Right_JioSaavn",

                    "platform": platform,

                    "source": source,

                    "confidence": confidence

                }

        elif cmd == "Right_Volume_Up":

            volume = self.context.get("volume")

            if volume >= 100:

                logging.info(
                    "Maximum volume reached."
                )

                return None

        elif cmd == "Right_Volume_Down":

            volume = self.context.get("volume")

            if volume <= 0:

                logging.info(
                    "Minimum volume reached."
                )

                return None

        # ------------------------------------------

        decision = {

            "command": cmd,

            "platform": platform,

            "source": source,

            "confidence": confidence,

            "timestamp": time.time()

        }

        self.context.record_command(

            cmd,

            source

        )

        return decision

    # --------------------------------------------------

    def select_platform(self):

        """
        Decide Android or Website.
        """

        current = self.context.get_platform()

        if current:

            return current

        return "ANDROID"

    # --------------------------------------------------

    def set_platform(self, platform):

        self.context.update_platform(platform)

    # --------------------------------------------------

    def get_platform(self):

        return self.context.get_platform()