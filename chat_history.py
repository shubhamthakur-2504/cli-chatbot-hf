from collections import deque
from dataclasses import dataclass

@dataclass
class ChatHistory:
    max_length: int

    def __post_init__(self):
        self.history = deque(maxlen=self.max_length)

    def add_message(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def get_history(self):
        return list(self.history)