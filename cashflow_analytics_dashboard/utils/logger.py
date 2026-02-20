import logging
from typing import Any

class DashboardLogger:
    def __init__(self, name: str):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(name)
    
    def log_info(self, message: str) -> None:
        self.logger.info(message)