"""
=========================================================
Hybrid BCI JioSaavn Automation
Event Dispatcher
=========================================================

Responsibilities
----------------
1. Dispatch events to EventBus.
2. Validate events.
3. Log event dispatching.
4. Support synchronous dispatch.
5. Support asynchronous dispatch.

=========================================================
"""

import logging
import threading

from event_bus.event_bus import EventBus
from event_bus.event_types import EventTypes


class EventDispatcher:

    def __init__(self, event_bus: EventBus):

        self.event_bus = event_bus

        logging.info("Event Dispatcher Initialized")

    # -------------------------------------------------

    def dispatch(self,
                 event_name,
                 payload=None):

        """
        Dispatch an event synchronously.
        """

        if not self.validate_event(event_name):

            logging.warning(
                f"Unknown Event : {event_name}"
            )

            return False

        logging.info(
            f"Dispatching Event : {event_name}"
        )

        self.event_bus.publish(
            event_name,
            payload
        )

        return True

    # -------------------------------------------------

    def dispatch_async(self,
                       event_name,
                       payload=None):

        """
        Dispatch event asynchronously.
        """

        thread = threading.Thread(

            target=self.dispatch,

            args=(event_name, payload),

            daemon=True

        )

        thread.start()

    # -------------------------------------------------

    def validate_event(self,
                       event_name):

        """
        Verify event exists in EventTypes.
        """

        valid_events = [

            value

            for key, value

            in vars(EventTypes).items()

            if not key.startswith("_")

        ]

        return event_name in valid_events

    # -------------------------------------------------

    def dispatch_prediction(self,
                            prediction):

        self.dispatch(

            EventTypes.PREDICTION_GENERATED,

            prediction

        )

    # -------------------------------------------------

    def dispatch_command(self,
                         command):

        self.dispatch(

            EventTypes.COMMAND_GENERATED,

            command

        )

    # -------------------------------------------------

    def dispatch_decision(self,
                          decision):

        self.dispatch(

            EventTypes.DECISION_READY,

            decision

        )

    # -------------------------------------------------

    def dispatch_execution(self,
                           execution):

        self.dispatch(

            EventTypes.EXECUTION_STARTED,

            execution

        )

    # -------------------------------------------------

    def dispatch_completed(self,
                           result):

        self.dispatch(

            EventTypes.EXECUTION_COMPLETED,

            result

        )

    # -------------------------------------------------

    def dispatch_error(self,
                       error):

        self.dispatch(

            EventTypes.ERROR_OCCURRED,

            error

        )