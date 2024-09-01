import pytest
from src.generator.generator import PasswordGenerator
from src.strategy.generate_password import UpperCaseStrategy
from src.strategy.generate_password import LowerCaseStrategy
from src.strategy.generate_password import MixedCaseAndSpecialStrategy

def test_uppercase_strategy():
    length = 8
    generator = PasswordGenerator(UpperCaseStrategy())
    password = generator.generate_password(length)
    assert len(password) == length, "O comprimento da senha deve ser igual ao solicitado"
    assert password.isupper(), "A senha deve conter apenas caracteres maiúsculos"

def test_lowercase_strategy():
    length = 8
    generator = PasswordGenerator(LowerCaseStrategy())
    password = generator.generate_password(length)
    assert len(password) == length, "O comprimento da senha deve ser igual ao solicitado"
    assert password.islower(), "A senha deve conter apenas caracteres minúsculos"

def test_mixed_case_and_special_strategy():
    length = 10
    generator = PasswordGenerator(MixedCaseAndSpecialStrategy())
    password = generator.generate_password(length)
    assert len(password) == length, "O comprimento da senha deve ser igual ao solicitado"
    assert any(c.isupper() for c in password), "A senha deve conter ao menos uma letra maiúscula"
    assert any(c.islower() for c in password), "A senha deve conter ao menos uma letra minúscula"
    assert any(c in '!@#$%^&*()-_=+[]{}|;:",.<>?/\\' for c in password), "A senha deve conter ao menos um caractere especial"

def test_minimum_length():
    generator = PasswordGenerator(UpperCaseStrategy())
    with pytest.raises(ValueError, match="O número mínimo de caracteres é 6."):
        generator.generate_password(5)

def test_invalid_strategy():
    with pytest.raises(AttributeError):
        generator = PasswordGenerator(None)
        generator.generate_password(8)

def test_negative_length():
    generator = PasswordGenerator(UpperCaseStrategy())
    with pytest.raises(ValueError, match="O número mínimo de caracteres é 6."):
        generator.generate_password(-1)

def test_exact_minimum_length():
    generator = PasswordGenerator(LowerCaseStrategy())
    password = generator.generate_password(6)
    assert len(password) == 6