"""
=========================================================
Hybrid BCI JioSaavn Automation
Confidence Filter
=========================================================

Responsibilities
----------------
1. Filter low-confidence predictions.
2. Decide whether to:
   • ACCEPT
   • CONFIRM
   • REJECT
3. Return standardized decision.

=========================================================
"""

import logging

from config.settings import settings


class ConfidenceFilter:

    def __init__(self):

        self.accept_threshold = settings.CONFIDENCE_THRESHOLD

        self.confirm_threshold = 0.60

        logging.info("Confidence Filter Initialized")

    # -------------------------------------------------

    def evaluate(self, prediction):

        """
        Evaluate prediction confidence.

        Parameters
        ----------
        prediction : dict

        Example
        -------
        {
            "command": "Right_Play_Pause",
            "confidence": 0.91
        }

        Returns
        -------
        dict
        """

        if prediction is None:

            return self.reject("No prediction")

        command = prediction.get("command")

        confidence = prediction.get("confidence", 0.0)

        # ---------------------------------------------

        if confidence >= self.accept_threshold:

            logging.info(

                f"Accepted : {command} ({confidence:.2f})"

            )

            return {

                "status": "ACCEPT",

                "command": command,

                "confidence": confidence

            }

        # ---------------------------------------------

        elif confidence >= self.confirm_threshold:

            logging.warning(

                f"Needs Confirmation : {command}"

            )

            return {

                "status": "CONFIRM",

                "command": command,

                "confidence": confidence,

                "message": f"Did you mean '{command}'?"

            }

        # ---------------------------------------------

        else:

            logging.warning(

                f"Rejected : {command}"

            )

            return self.reject(command, confidence)

    # -------------------------------------------------

    def reject(self, command=None, confidence=0):

        """
        Reject prediction.
        """

        return {

            "status": "REJECT",

            "command": command,

            "confidence": confidence

        }

    # -------------------------------------------------

    def is_accepted(self, prediction):

        """
        True if prediction is accepted.
        """

        result = self.evaluate(prediction)

        return result["status"] == "ACCEPT"

    # -------------------------------------------------

    def update_threshold(self, threshold):

        """
        Update acceptance threshold.
        """

        self.accept_threshold = threshold

        logging.info(

            f"New Threshold : {threshold}"

        )

    # -------------------------------------------------

    def get_threshold(self):

        return self.accept_threshold