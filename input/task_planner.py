"""
=========================================================
Hybrid BCI JioSaavn Automation
Task Planner
=========================================================

Responsibilities
----------------
1. Convert parsed intents into executable tasks.
2. Add metadata required by the execution engine.
3. Return a standardized task object.

This module NEVER executes commands.

=========================================================
"""

import uuid
import time
import logging


class TaskPlanner:

    def __init__(self):

        logging.info("Task Planner Initialized.")

    # --------------------------------------------------

    def create_task(self, intent):

        """
        Convert an intent into a task.
        """

        if intent is None:

            return None

        task = {

            "task_id": str(uuid.uuid4()),

            "timestamp": time.time(),

            "intent": intent.get("intent"),

            "target": intent.get("target"),

            "platform": intent.get(
                "platform",
                "AUTO"
            ),

            "priority": self.get_priority(
                intent.get("intent")
            ),

            "status": "PENDING",

            "retries": 0,

            "source": "CHAT"

        }

        logging.info(
            f"Task Created : {task['task_id']}"
        )

        return task

    # --------------------------------------------------

    def get_priority(self, intent):

        """
        Assign priority to tasks.
        """

        high_priority = [

            "PAUSE",

            "STOP",

            "NEXT",

            "PREVIOUS",

            "VOLUME_UP",

            "VOLUME_DOWN"

        ]

        medium_priority = [

            "PLAY",

            "SEARCH",

            "OPEN_APP",

            "CLOSE_APP"

        ]

        low_priority = [

            "SWITCH_PLATFORM"

        ]

        if intent in high_priority:

            return 1

        elif intent in medium_priority:

            return 2

        elif intent in low_priority:

            return 3

        return 5

    # --------------------------------------------------

    def update_status(self, task, status):

        """
        Update task status.
        """

        task["status"] = status

        return task

    # --------------------------------------------------

    def increment_retry(self, task):

        """
        Increase retry count.
        """

        task["retries"] += 1

        return task