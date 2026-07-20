"""
=========================================================
Hybrid BCI JioSaavn Automation
Retry Queue
=========================================================

Responsibilities
----------------
1. Store failed commands/tasks.
2. Retry execution after a delay.
3. Limit retry attempts.
4. Remove successful retries.
5. Move permanently failed items to Dead Letter Queue.

=========================================================
"""

import time
import uuid
import logging
import threading
from queue import PriorityQueue, Empty
from itertools import count


class RetryQueue:

    def __init__(self,
                 retry_delay=5,
                 max_retries=3):

        self.queue = PriorityQueue()

        self.counter = count()

        self.lock = threading.Lock()

        self.retry_delay = retry_delay

        self.max_retries = max_retries

        logging.info("Retry Queue Initialized")

    # -------------------------------------------------

    def enqueue(self,
                item,
                priority=50):

        """
        Add failed command/task to retry queue.
        """

        retry_item = {

            "retry_id": str(uuid.uuid4()),

            "item": item,

            "priority": priority,

            "retry_count": 0,

            "next_retry": time.time() + self.retry_delay

        }

        self.queue.put(

            (

                -priority,

                next(self.counter),

                retry_item

            )

        )

        logging.info(

            f"Added to Retry Queue : "

            f"{item.get('command', item.get('task_name','UNKNOWN'))}"

        )

    # -------------------------------------------------

    def dequeue(self):

        """
        Return next retry item if retry time reached.
        """

        if self.queue.empty():

            return None

        priority, index, retry_item = self.queue.queue[0]

        if retry_item["next_retry"] > time.time():

            return None

        self.queue.get()

        return retry_item

    # -------------------------------------------------

    def retry_failed(self):

        """
        Retrieve next retryable item.
        """

        retry_item = self.dequeue()

        if retry_item is None:

            return None

        retry_item["retry_count"] += 1

        logging.info(

            f"Retry Attempt "

            f"{retry_item['retry_count']}"

        )

        return retry_item

    # -------------------------------------------------

    def retry_completed(self,
                        retry_id):

        """
        Successful retry.
        """

        logging.info(

            f"Retry Success : {retry_id}"

        )

    # -------------------------------------------------

    def retry_failed_again(self,
                           retry_item):

        """
        Retry failed again.
        """

        if retry_item["retry_count"] >= self.max_retries:

            logging.error(

                "Maximum Retry Limit Reached"

            )

            return False

        retry_item["next_retry"] = (

            time.time()

            + self.retry_delay

        )

        self.queue.put(

            (

                -retry_item["priority"],

                next(self.counter),

                retry_item

            )

        )

        return True

    # -------------------------------------------------

    def clear(self):

        with self.lock:

            while not self.queue.empty():

                self.queue.get()

    # -------------------------------------------------

    def size(self):

        return self.queue.qsize()

    # -------------------------------------------------

    def is_empty(self):

        return self.queue.empty()

    # -------------------------------------------------

    def print_queue(self):

        logging.info("=" * 60)

        logging.info("Retry Queue")

        for _, _, item in list(self.queue.queue):

            logging.info(

                f"{item['item'].get('command', item['item'].get('task_name','UNKNOWN'))}"

                f" Retry={item['retry_count']}"

            )

        logging.info("=" * 60)