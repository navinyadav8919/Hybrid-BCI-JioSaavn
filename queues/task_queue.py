"""
=========================================================
Hybrid BCI JioSaavn Automation
Task Queue
=========================================================

Responsibilities
----------------
1. Store high-level tasks.
2. Maintain task priority.
3. Thread-safe queue operations.
4. Support task monitoring.

=========================================================
"""

import logging
import threading
from queue import PriorityQueue, Empty
from itertools import count


class TaskQueue:

    def __init__(self):

        self.queue = PriorityQueue()

        self.counter = count()

        self.lock = threading.Lock()

        logging.info("Task Queue Initialized")

    # -------------------------------------------------

    def enqueue(self, task):

        """
        Add a task to the queue.
        """

        if task is None:
            return

        priority = task.get("priority", 0)

        self.queue.put(
            (
                -priority,
                next(self.counter),
                task
            )
        )

        logging.info(
            f"Task Enqueued : {task.get('task_name')} "
            f"(Priority={priority})"
        )

    # -------------------------------------------------

    def dequeue(self):

        """
        Get next task.
        """

        try:

            _, _, task = self.queue.get_nowait()

            logging.info(
                f"Task Dequeued : {task.get('task_name')}"
            )

            return task

        except Empty:

            return None

    # -------------------------------------------------

    def peek(self):

        """
        View next task without removing.
        """

        with self.lock:

            if self.queue.empty():

                return None

            return self.queue.queue[0][2]

    # -------------------------------------------------

    def size(self):

        return self.queue.qsize()

    # -------------------------------------------------

    def is_empty(self):

        return self.queue.empty()

    # -------------------------------------------------

    def clear(self):

        with self.lock:

            while not self.queue.empty():

                self.queue.get()

        logging.info("Task Queue Cleared")

    # -------------------------------------------------

    def contains(self, task_name):

        with self.lock:

            for _, _, task in self.queue.queue:

                if task.get("task_name") == task_name:

                    return True

        return False

    # -------------------------------------------------

    def remove(self, task_name):

        with self.lock:

            temp = []

            removed = False

            while not self.queue.empty():

                item = self.queue.get()

                if item[2].get("task_name") == task_name:

                    removed = True

                    continue

                temp.append(item)

            for item in temp:

                self.queue.put(item)

        if removed:

            logging.info(
                f"Removed Task : {task_name}"
            )

        return removed

    # -------------------------------------------------

    def get_all_tasks(self):

        with self.lock:

            return [

                item[2]

                for item in list(self.queue.queue)

            ]

    # -------------------------------------------------

    def print_queue(self):

        logging.info("=" * 60)

        logging.info("Current Task Queue")

        for _, _, task in list(self.queue.queue):

            logging.info(
                f"{task.get('task_name')} "
                f"(Priority={task.get('priority',0)})"
            )

        logging.info("=" * 60)