"""
=========================================================
Hybrid BCI JioSaavn Automation
Intent Parser
=========================================================

Responsibilities
----------------
1. Convert natural language into structured intents.
2. Extract entities like song, artist, album, playlist.
3. Return a standardized intent dictionary.

=========================================================
"""

import re
import logging


class IntentParser:

    def __init__(self):

        logging.info("Intent Parser Initialized.")

    # --------------------------------------------------

    def parse(self, text):

        """
        Convert text into structured intent.
        """

        if not text:

            return None

        text = text.lower().strip()

        # --------------------------------------------------
        # PLAY SONG
        # --------------------------------------------------

        match = re.search(r"play (.+)", text)

        if match:

            target = match.group(1).strip()

            return {

                "intent": "PLAY",

                "target": target,

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # SEARCH
        # --------------------------------------------------

        match = re.search(r"search (.+)", text)

        if match:

            target = match.group(1).strip()

            return {

                "intent": "SEARCH",

                "target": target,

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # NEXT
        # --------------------------------------------------

        if any(word in text for word in [

            "next",

            "skip",

            "next song"

        ]):

            return {

                "intent": "NEXT",

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # PREVIOUS
        # --------------------------------------------------

        if any(word in text for word in [

            "previous",

            "back",

            "previous song"

        ]):

            return {

                "intent": "PREVIOUS",

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # PAUSE
        # --------------------------------------------------

        if any(word in text for word in [

            "pause",

            "stop music"

        ]):

            return {

                "intent": "PAUSE",

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # RESUME
        # --------------------------------------------------

        if any(word in text for word in [

            "resume",

            "continue",

            "play"

        ]):

            return {

                "intent": "RESUME",

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # VOLUME UP
        # --------------------------------------------------

        if any(word in text for word in [

            "volume up",

            "increase volume",

            "louder"

        ]):

            return {

                "intent": "VOLUME_UP",

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # VOLUME DOWN
        # --------------------------------------------------

        if any(word in text for word in [

            "volume down",

            "decrease volume",

            "lower volume"

        ]):

            return {

                "intent": "VOLUME_DOWN",

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # OPEN APP
        # --------------------------------------------------

        if any(word in text for word in [

            "open jiosaavn",

            "launch jiosaavn"

        ]):

            return {

                "intent": "OPEN_APP",

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # CLOSE APP
        # --------------------------------------------------

        if any(word in text for word in [

            "close jiosaavn",

            "exit jiosaavn"

        ]):

            return {

                "intent": "CLOSE_APP",

                "platform": "AUTO"

            }

        # --------------------------------------------------
        # WEBSITE
        # --------------------------------------------------

        if "website" in text:

            return {

                "intent": "SWITCH_PLATFORM",

                "platform": "WEBSITE"

            }

        # --------------------------------------------------
        # ANDROID
        # --------------------------------------------------

        if "android" in text or "mobile" in text:

            return {

                "intent": "SWITCH_PLATFORM",

                "platform": "ANDROID"

            }

        # --------------------------------------------------
        # Unknown
        # --------------------------------------------------

        return {

            "intent": "UNKNOWN",

            "text": text

        }