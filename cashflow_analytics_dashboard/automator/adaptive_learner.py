from typing import Dict
import random

class AdaptiveLearner:
    def __init__(self):
        self.strategies = {}
    
    def train_strategy(self, name: str, strategy_func) -> None:
        self.strategies[name] = strategy_func
    
    def execute_strategy(self, trigger: Dict) -> Dict:
        if not self.strategies:
            raise ValueError("No strategies trained")
        
        selected_strategy = random.choice(list(self.strategies.keys()))
        return self.strategies[selected_strategy](trigger)