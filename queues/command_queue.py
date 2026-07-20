"""
=========================================================
Hybrid BCI JioSaavn Automation
Command Queue
=========================================================

Responsibilities
----------------
1. Store validated commands.
2. Maintain priority order.
3. Provide thread-safe operations.
4. Support queue monitoring.

=========================================================
"""

import logging
import threading
from queue import PriorityQueue, Empty
from itertools import count


class CommandQueue:

    def __init__(self):

        self.queue = PriorityQueue()

        self.counter = count()

        self.lock = threading.Lock()

        logging.info("Command Queue Initialized")

    # --------------------------------------------------

    def enqueue(self, command):

        """
        Add a command into the queue.

        Lower priority number in PriorityQueue comes first,
        so we negate the priority.
        """

        if command is None:
            return

        priority = command.get("priority", 0)

        self.queue.put(
            (
                -priority,
                next(self.counter),
                command
            )
        )

        logging.info(
            f"Enqueued : {command['command']} "
            f"(Priority={priority})"
        )

    # --------------------------------------------------

    def dequeue(self):

        """
        Remove highest priority command.
        """

        try:

            _, _, command = self.queue.get_nowait()

            logging.info(
                f"Dequeued : {command['command']}"
            )

            return command

        except Empty:

            return None

    # --------------------------------------------------

    def peek(self):

        """
        Peek next command without removing it.
        """

        with self.lock:

            if self.queue.empty():

                return None

            item = self.queue.queue[0]

            return item[2]

    # --------------------------------------------------

    def clear(self):

        """
        Clear queue.
        """

        with self.lock:

            while not self.queue.empty():

                self.queue.get()

        logging.info("Command Queue Cleared")

    # --------------------------------------------------

    def size(self):

        return self.queue.qsize()

    # --------------------------------------------------

    def is_empty(self):

        return self.queue.empty()

    # --------------------------------------------------

    def get_all(self):

        """
        Return commands currently in queue.
        """

        with self.lock:

            return [

                item[2]

                for item in

                list(self.queue.queue)

            ]

    # --------------------------------------------------

    def contains(self, command_name):

        """
        Check if a command already exists.
        """

        with self.lock:

            for _, _, command in self.queue.queue:

                if command.get("command") == command_name:

                    return True

        return False

    # --------------------------------------------------

    def remove(self, command_name):

        """
        Remove all matching commands.
        """

        with self.lock:

            remaining = []

            removed = False

            while not self.queue.empty():

                item = self.queue.get()

                if item[2].get("command") == command_name:

                    removed = True

                    continue

                remaining.append(item)

            for item in remaining:

                self.queue.put(item)

        if removed:

            logging.info(f"Removed command : {command_name}")

        return removed

    # --------------------------------------------------

    def print_queue(self):

        """
        Print queue contents.
        """

        logging.info("=" * 60)

        logging.info("Current Command Queue")

        for _, _, command in list(self.queue.queue):

            logging.info(
                f"{command['command']} "
                f"(Priority={command.get('priority',0)})"
            )

        logging.info("=" * 60)