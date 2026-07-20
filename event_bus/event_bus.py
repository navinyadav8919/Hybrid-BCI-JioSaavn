"""
=========================================================
Hybrid BCI JioSaavn Automation
Event Bus
=========================================================

Responsibilities
----------------
1. Publish events.
2. Subscribe to events.
3. Unsubscribe events.
4. Broadcast events.
5. Keep modules loosely coupled.

=========================================================
"""

import logging
import threading
from collections import defaultdict


class EventBus:

    def __init__(self):

        self.subscribers = defaultdict(list)

        self.lock = threading.Lock()

        logging.info("Event Bus Initialized")

    # --------------------------------------------------

    def subscribe(self, event_name, callback):
        """
        Register a callback for an event.

        Example:
            event_bus.subscribe(
                "prediction",
                decision_manager.handle_prediction
            )
        """

        with self.lock:

            if callback not in self.subscribers[event_name]:

                self.subscribers[event_name].append(callback)

                logging.info(
                    f"Subscribed -> {callback.__name__} "
                    f"to [{event_name}]"
                )

    # --------------------------------------------------

    def unsubscribe(self, event_name, callback):
        """
        Remove a callback.
        """

        with self.lock:

            if callback in self.subscribers[event_name]:

                self.subscribers[event_name].remove(callback)

                logging.info(
                    f"Unsubscribed -> {callback.__name__}"
                )

    # --------------------------------------------------

    def publish(self, event_name, data=None):
        """
        Publish an event.

        Example:

        event_bus.publish(
            "prediction",
            prediction
        )
        """

        callbacks = self.subscribers.get(event_name, [])

        logging.info(

            f"Publishing Event : {event_name}"

        )

        for callback in callbacks:

            try:

                callback(data)

            except Exception as e:

                logging.exception(e)

    # --------------------------------------------------

    def publish_async(self, event_name, data=None):
        """
        Publish asynchronously.
        """

        thread = threading.Thread(

            target=self.publish,

            args=(event_name, data),

            daemon=True

        )

        thread.start()

    # --------------------------------------------------

    def clear(self):
        """
        Remove all subscribers.
        """

        with self.lock:

            self.subscribers.clear()

            logging.info("Event Bus Cleared")

    # --------------------------------------------------

    def get_events(self):
        """
        Return registered events.
        """

        return list(self.subscribers.keys())

    # --------------------------------------------------

    def get_subscribers(self, event_name):
        """
        Return subscribers for an event.
        """

        return [

            callback.__name__

            for callback in

            self.subscribers.get(event_name, [])

        ]

    # --------------------------------------------------

    def has_subscribers(self, event_name):

        return len(

            self.subscribers.get(event_name, [])

        ) > 0