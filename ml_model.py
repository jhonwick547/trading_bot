# ml_model.py
import os
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

class MLModel:
    def __init__(self):
        self.model_path = "xgb_model.json"
        self.model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
        # Load or train model
        if os.path.exists(self.model_path):
            self.model.load_model(self.model_path)
        else:
            # Dummy training on random data (for demonstration)
            X = np.random.randn(500, 3)  # pretend features
            y = np.random.choice([0,1,2], size=500)  # 0=hold,1=buy,2=sell
            self.model.fit(X, y)
            self.model.save_model(self.model_path)
    def predict(self, closes, signals):
        # Create a feature vector from strategies (this is placeholder logic)
        feat = np.array(signals).reshape(1, -1)
        pred = self.model.predict(feat)[0]
        # Map numeric to our convention
        return {0: 0, 1: 1, 2: -1}.get(pred, 0)
