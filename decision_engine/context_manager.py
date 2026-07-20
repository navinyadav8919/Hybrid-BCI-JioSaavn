"""
=========================================================
Hybrid BCI JioSaavn Automation
Context Manager
=========================================================

Responsibilities
----------------
1. Maintain application state.
2. Share state across all modules.
3. Avoid duplicate executions.
4. Store current session information.

=========================================================
"""

import logging
import time


class ContextManager:

    def __init__(self):

        self.reset()

        logging.info("Context Manager Initialized")

    # -------------------------------------------------

    def reset(self):

        """
        Reset complete application context.
        """

        self.context = {

            "session_active": False,

            "platform": None,

            "jiosaavn_open": False,

            "music_playing": False,

            "current_song": None,

            "current_playlist": None,

            "volume": 50,

            "search_active": False,

            "last_command": None,

            "last_command_time": None,

            "last_source": None

        }

    # -------------------------------------------------

    def update(self, key, value):

        """
        Update context value.
        """

        self.context[key] = value

    # -------------------------------------------------

    def get(self, key, default=None):

        """
        Get context value.
        """

        return self.context.get(key, default)

    # -------------------------------------------------

    def start_session(self):

        self.context["session_active"] = True

        logging.info("Session Started")

    # -------------------------------------------------

    def stop_session(self):

        self.context["session_active"] = False

        logging.info("Session Stopped")

    # -------------------------------------------------

    def update_platform(self, platform):

        self.context["platform"] = platform

    # -------------------------------------------------

    def open_jiosaavn(self):

        self.context["jiosaavn_open"] = True

    # -------------------------------------------------

    def close_jiosaavn(self):

        self.context["jiosaavn_open"] = False

    # -------------------------------------------------

    def play_music(self):

        self.context["music_playing"] = True

    # -------------------------------------------------

    def pause_music(self):

        self.context["music_playing"] = False

    # -------------------------------------------------

    def update_song(self, song):

        self.context["current_song"] = song

    # -------------------------------------------------

    def update_playlist(self, playlist):

        self.context["current_playlist"] = playlist

    # -------------------------------------------------

    def update_volume(self, volume):

        volume = max(0, min(100, volume))

        self.context["volume"] = volume

    # -------------------------------------------------

    def start_search(self):

        self.context["search_active"] = True

    # -------------------------------------------------

    def stop_search(self):

        self.context["search_active"] = False

    # -------------------------------------------------

    def record_command(self, command, source):

        self.context["last_command"] = command

        self.context["last_source"] = source

        self.context["last_command_time"] = time.time()

    # -------------------------------------------------

    def get_last_command(self):

        return {

            "command": self.context["last_command"],

            "source": self.context["last_source"],

            "time": self.context["last_command_time"]

        }

    # -------------------------------------------------

    def is_session_active(self):

        return self.context["session_active"]

    # -------------------------------------------------

    def is_music_playing(self):

        return self.context["music_playing"]

    # -------------------------------------------------

    def is_jiosaavn_open(self):

        return self.context["jiosaavn_open"]

    # -------------------------------------------------

    def get_platform(self):

        return self.context["platform"]

    # -------------------------------------------------

    def get_context(self):

        """
        Return complete context.
        """

        return self.context.copy()

    # -------------------------------------------------

    def print_context(self):

        """
        Print current context.
        """

        logging.info("=" * 50)

        logging.info("CURRENT CONTEXT")

        for key, value in self.context.items():

            logging.info(f"{key} : {value}")

        logging.info("=" * 50)