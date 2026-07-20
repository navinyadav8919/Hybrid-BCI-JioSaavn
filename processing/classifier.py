"""
=========================================================
Hybrid BCI JioSaavn Automation
Classifier
=========================================================

Responsibilities
----------------
1. Load trained ML model
2. Predict EEG command
3. Return predicted command
4. Return confidence score

Input
-----
Feature Vector

Output
------
{
    "command": "...",
    "confidence": 0.94
}

=========================================================
"""

import logging
import joblib
import numpy as np
from pathlib import Path


class EEGClassifier:

    def __init__(self, model_path):

        self.model_path = Path(model_path)

        self.model = None

        self.load_model()

    # -------------------------------------------------

    def load_model(self):

        """
        Load trained model.
        """

        if not self.model_path.exists():

            raise FileNotFoundError(

                f"Model not found : {self.model_path}"

            )

        self.model = joblib.load(self.model_path)

        logging.info(

            f"Loaded Model : {self.model_path.name}"

        )

    # -------------------------------------------------

    def predict(self, features):

        """
        Predict EEG command.
        """

        if self.model is None:

            raise RuntimeError(

                "Classifier not loaded."

            )

        features = np.asarray(

            features,

            dtype=np.float32

        ).reshape(1, -1)

        prediction = self.model.predict(

            features

        )[0]

        # -----------------------------
        # Confidence
        # -----------------------------

        confidence = 1.0

        if hasattr(self.model, "predict_proba"):

            probabilities = self.model.predict_proba(

                features

            )[0]

            confidence = float(

                np.max(probabilities)

            )

        return {

            "command": prediction,

            "confidence": confidence

        }

    # -------------------------------------------------

    def predict_command(self, features):

        """
        Return only command.
        """

        return self.predict(features)["command"]

    # -------------------------------------------------

    def predict_confidence(self, features):

        """
        Return only confidence.
        """

        return self.predict(features)["confidence"]

    # -------------------------------------------------

    def is_loaded(self):

        return self.model is not None