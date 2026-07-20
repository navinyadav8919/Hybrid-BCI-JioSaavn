"""
=========================================================
Hybrid BCI JioSaavn Automation
Prediction Smoother
=========================================================

Responsibilities
----------------
1. Remove noisy predictions.
2. Stabilize classifier outputs.
3. Prevent accidental command execution.
4. Forward only stable predictions.

=========================================================
"""

import logging
from collections import deque
from collections import Counter


class PredictionSmoother:

    def __init__(self,
                 window_size=5,
                 minimum_votes=3):

        self.window_size = window_size

        self.minimum_votes = minimum_votes

        self.predictions = deque(maxlen=window_size)

        logging.info("Prediction Smoother Initialized")

    # -------------------------------------------------

    def reset(self):

        """
        Clear prediction history.
        """

        self.predictions.clear()

    # -------------------------------------------------

    def add_prediction(self, prediction):

        """
        Add new prediction.

        prediction example:

        {
            "command":"Right_Play_Pause",
            "confidence":0.94
        }
        """

        if prediction is None:

            return None

        command = prediction.get("command")

        if command is None:

            return None

        self.predictions.append(command)

        return self.get_smoothed_prediction(prediction)

    # -------------------------------------------------

    def get_smoothed_prediction(self, latest_prediction):

        """
        Majority Voting.
        """

        if len(self.predictions) < self.window_size:

            return None

        counts = Counter(self.predictions)

        command, votes = counts.most_common(1)[0]

        if votes >= self.minimum_votes:

            logging.info(

                f"Stable Prediction : {command}"

            )

            return {

                "command": command,

                "confidence": latest_prediction.get(

                    "confidence",

                    0.0

                ),

                "votes": votes,

                "window_size": self.window_size

            }

        logging.info(

            "Prediction not stable."

        )

        return None

    # -------------------------------------------------

    def get_history(self):

        """
        Return prediction history.
        """

        return list(self.predictions)

    # -------------------------------------------------

    def is_stable(self):

        """
        Check whether prediction window
        contains enough matching predictions.
        """

        if len(self.predictions) < self.window_size:

            return False

        counts = Counter(self.predictions)

        _, votes = counts.most_common(1)[0]

        return votes >= self.minimum_votes

    # -------------------------------------------------

    def most_common_prediction(self):

        """
        Return current majority command.
        """

        if not self.predictions:

            return None

        counts = Counter(self.predictions)

        return counts.most_common(1)[0][0]