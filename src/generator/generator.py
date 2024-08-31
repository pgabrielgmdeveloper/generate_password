from src.strategy.generate_password import PasswordStrategy 

class PasswordGenerator:
    def __init__(self, strategy: PasswordStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PasswordStrategy):
        self._strategy = strategy

    def generate_password(self, length: int) -> str:
        if length < 6:
            raise ValueError("O número mínimo de caracteres é 6.")
        return self._strategy.generate(length)
