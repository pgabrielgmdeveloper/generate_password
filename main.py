import sys
from src.generator.generator import PasswordGenerator
from src.strategy.generate_password import UpperCaseStrategy
from src.strategy.generate_password import LowerCaseStrategy
from src.strategy.generate_password import MixedCaseAndSpecialStrategy

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python -m password_generator.main <tamanho> <tipo>")
        print("Tipo: 'M' para maiúsculas, 'm' para minúsculas, 'E' para misto com especiais.")
        sys.exit(1)

    try:
        length = int(sys.argv[1])
        password_type = sys.argv[2]

        if password_type == 'M':
            strategy = UpperCaseStrategy()
        elif password_type == 'm':
            strategy = LowerCaseStrategy()
        elif password_type == 'E':
            strategy = MixedCaseAndSpecialStrategy()
        else:
            raise ValueError("Tipo de senha inválido. Use 'M', 'm' ou 'E'.")

        generator = PasswordGenerator(strategy)
        password = generator.generate_password(length)
        print(f"Senha gerada: {password}")

    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)
