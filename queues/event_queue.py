"""
=========================================================
Hybrid BCI JioSaavn Automation
Event Queue
=========================================================

Responsibilities
----------------
1. Store system events.
2. Preserve event order.
3. Support event priorities.
4. Thread-safe queue operations.
5. Prevent event loss.

=========================================================
"""

import logging
import threading
import time
import uuid
from queue import PriorityQueue, Empty
from itertools import count


class EventQueue:

    def __init__(self):

        self.queue = PriorityQueue()

        self.counter = count()

        self.lock = threading.Lock()

        logging.info("Event Queue Initialized")

    # -------------------------------------------------

    def enqueue(self,
                event_type,
                payload=None,
                priority=50):

        """
        Add an event to the queue.
        """

        event = {

            "event_id": str(uuid.uuid4()),

            "event_type": event_type,

            "payload": payload,

            "priority": priority,

            "timestamp": time.time()

        }

        self.queue.put(

            (

                -priority,

                next(self.counter),

                event

            )

        )

        logging.info(

            f"Event Enqueued : "

            f"{event_type}"

        )

        return event

    # -------------------------------------------------

    def dequeue(self):

        """
        Get highest priority event.
        """

        try:

            _, _, event = self.queue.get_nowait()

            logging.info(

                f"Event Dequeued : "

                f"{event['event_type']}"

            )

            return event

        except Empty:

            return None

    # -------------------------------------------------

    def peek(self):

        """
        View next event without removing.
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

        logging.info("Event Queue Cleared")

    # -------------------------------------------------

    def get_all_events(self):

        with self.lock:

            return [

                item[2]

                for item

                in list(self.queue.queue)

            ]

    # -------------------------------------------------

    def contains(self,
                 event_type):

        with self.lock:

            for _, _, event in self.queue.queue:

                if event["event_type"] == event_type:

                    return True

        return False

    # -------------------------------------------------

    def remove(self,
               event_type):

        with self.lock:

            temp = []

            removed = False

            while not self.queue.empty():

                item = self.queue.get()

                if item[2]["event_type"] == event_type:

                    removed = True

                    continue

                temp.append(item)

            for item in temp:

                self.queue.put(item)

        if removed:

            logging.info(

                f"Removed Event : {event_type}"

            )

        return removed

    # -------------------------------------------------

    def print_queue(self):

        logging.info("=" * 60)

        logging.info("Current Event Queue")

        for _, _, event in list(self.queue.queue):

            logging.info(

                f"{event['event_type']} "

                f"(Priority={event['priority']})"

            )

        logging.info("=" * 60)