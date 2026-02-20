from typing import List, Dict
import pandas as pd

class DataTransformer:
    def __init__(self):
        self.models = {}
    
    def transform(self, data: List[Dict]) -> pd.DataFrame:
        df = pd.DataFrame(data)
        # Apply transformations here
        return df
    
    def register_model(self, name: str, model_func):
        self.models[name] = model_func

    def apply_model(self, df: pd.DataFrame, model_name: str) -> pd.Series:
        if model_name in self.models:
            return self.models[model_name](df)
        else:
            raise ValueError("Model not registered")