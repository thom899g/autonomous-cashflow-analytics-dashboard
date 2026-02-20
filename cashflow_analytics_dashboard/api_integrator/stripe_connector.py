from abc import ABC, abstractmethod
from typing import Dict, Any
import stripe

class StripeConnector:
    def __init__(self, api_key: str):
        self.client = stripe.Stripe(api_key)
    
    @abstractmethod
    def get_payment_history(self) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def create_charge(self, amount: float, currency: str, source_id: str) -> bool:
        pass

class QuickBooksConnector(StripeConnector):
    def __init__(self, api_key: str):
        super().__init__(api_key)
    
    def get_invoice_status(self) -> Dict[str, Any]:
        pass
    
    def create_refund(self, transaction_id: str) -> bool:
        pass