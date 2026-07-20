"""
=========================================================
Hybrid BCI JioSaavn Automation
Voice Interface
=========================================================

Responsibilities
----------------
1. Listen to user voice
2. Convert speech to text
3. Send text to Intent Parser
4. Return standardized task

This module NEVER executes commands.

=========================================================
"""

import logging
import speech_recognition as sr

from config.chat_config import chat_config

from chat.intent_parser import IntentParser
from chat.task_planner import TaskPlanner


class VoiceInterface:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.microphone = sr.Microphone()

        self.intent_parser = IntentParser()

        self.task_planner = TaskPlanner()

        logging.info("Voice Interface Initialized.")

    # -----------------------------------------------------

    def get_next_command(self):

        """
        Listen for one voice command.
        """

        try:

            with self.microphone as source:

                print("\nListening...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio)

            print(f"You said : {text}")

            return self.process_text(text)

        except sr.UnknownValueError:

            print("Could not understand audio.")

            return None

        except sr.RequestError:

            print("Speech Recognition Service unavailable.")

            return None

        except KeyboardInterrupt:

            print("\nVoice Session Closed.")

            return None

        except Exception as e:

            logging.exception(e)

            return None

    # -----------------------------------------------------

    def process_text(self, text):

        """
        Process recognized speech.
        """

        logging.info(f"Voice Input : {text}")

        intent = self.intent_parser.parse(text)

        if intent is None:

            print(chat_config.ERROR_MESSAGE)

            return None

        task = self.task_planner.create_task(intent)

        if task is None:

            print(chat_config.ERROR_MESSAGE)

            return None

        logging.info("Voice Task Created Successfully.")

        return {

            "source": "VOICE",

            "task": task

        }

    # -----------------------------------------------------

    def reset(self):

        logging.info("Voice Session Reset")