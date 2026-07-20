"""
=========================================================
Hybrid BCI JioSaavn Automation
Chat Interface
=========================================================

Responsibilities
----------------
1. Accept user chat input
2. Validate input
3. Send input to Intent Parser
4. Return standardized task

This module NEVER executes commands.

=========================================================
"""

import logging

from config.chat_config import chat_config
from chat.intent_parser import IntentParser
from chat.task_planner import TaskPlanner


class ChatInterface:

    def __init__(self):

        self.intent_parser = IntentParser()

        self.task_planner = TaskPlanner()

        logging.info("Chat Interface Initialized.")

    # -----------------------------------------------------

    def get_next_command(self):

        """
        Read one chat message
        """

        while True:

            try:

                message = input("\nYou : ").strip()

                if len(message) == 0:

                    continue

                if len(message) > chat_config.MAX_MESSAGE_LENGTH:

                    print("Message too long.")

                    continue

                return self.process_message(message)

            except KeyboardInterrupt:

                print("\nChat Closed.")

                return None

            except Exception as e:

                logging.exception(e)

                return None

    # -----------------------------------------------------

    def process_message(self, message):

        """
        Process user message.
        """

        logging.info(f"User Message : {message}")

        # ---------------------------------------------
        # Intent Recognition
        # ---------------------------------------------

        intent = self.intent_parser.parse(message)

        if intent is None:

            print(chat_config.ERROR_MESSAGE)

            return None

        # ---------------------------------------------
        # Task Planning
        # ---------------------------------------------

        task = self.task_planner.create_task(intent)

        if task is None:

            print(chat_config.ERROR_MESSAGE)

            return None

        logging.info("Task Created Successfully.")

        return {

            "source": "CHAT",

            "task": task

        }

    # -----------------------------------------------------

    def reset(self):

        logging.info("Chat Session Reset")