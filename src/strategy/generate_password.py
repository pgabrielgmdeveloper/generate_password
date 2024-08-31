import random
import string

from abc import ABC, abstractmethod

class PasswordStrategy(ABC):
    @abstractmethod
    def generate(self, length: int) -> str:
        pass

class UpperCaseStrategy(PasswordStrategy):
    def generate(self, length: int) -> str:
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

class LowerCaseStrategy(PasswordStrategy):
    def generate(self, length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

class MixedCaseAndSpecialStrategy(PasswordStrategy):
    def generate(self, length: int) -> str:
        characters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))
