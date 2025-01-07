import re
from datetime import datetime

class PaymentValidator:
    def __init__(self):
        self.accepted_card_types = ["Visa", "MasterCard", "Amex"]
        self.transaction_limits = {"min": 1.0, "max": 10000.0}

    def validate_amount(self, amount):
        if amount <= 0:
            return "El monto debe ser un número positivo."
        if not (self.transaction_limits["min"] <= amount <= self.transaction_limits["max"]):
            return f"El monto debe estar entre {self.transaction_limits['min']} y {self.transaction_limits['max']}."
        return None

    def validate_card_number(self, card_number):
        if not card_number.isdigit():
            return "El número de la tarjeta debe contener solo dígitos."
        if not self.luhn_algorithm(card_number):
            return "El número de la tarjeta no es válido."
        return None

    def validate_card_expiration(self, expiration_date):
        try:
            exp_date = datetime.strptime(expiration_date, "%m/%y")
            if exp_date < datetime.now():
                return "La tarjeta ha expirado."
        except ValueError:
            return "El formato de la fecha de vencimiento debe ser MM/YY."
        return None

    def validate_cvv(self, cvv):
        if not re.match(r"^\d{3,4}$", cvv):
            return "El CVV debe contener 3 o 4 dígitos."
        return None

    def validate_card_type(self, card_type):
        if card_type not in self.accepted_card_types:
            return f"El tipo de tarjeta '{card_type}' no es aceptado. Tipos aceptados: {', '.join(self.accepted_card_types)}."
        return None

    def luhn_algorithm(self, card_number):
        digits = [int(d) for d in card_number[::-1]]
        checksum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        return checksum % 10 == 0

    def validate_payment(self, data):
        errors = []
        errors.append(self.validate_amount(data.get("amount", 0)))
        errors.append(self.validate_card_number(data.get("card_number", "")))
        errors.append(self.validate_card_expiration(data.get("expiration_date", "")))
        errors.append(self.validate_cvv(data.get("cvv", "")))
        errors.append(self.validate_card_type(data.get("card_type", "")))

        return [error for error in errors if error is not None]