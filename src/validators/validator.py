from datetime import datetime
import re

# Interface for strategies
class ValidationStrategy:
    def validate(self, data):
        raise NotImplementedError("You must implement the 'validate' method.")

# Concrete validation strategies
class AmountValidation(ValidationStrategy):
    def __init__(self, min_amount=1.0, max_amount=10000.0):
        self.min_amount = min_amount
        self.max_amount = max_amount

    def validate(self, data):
        amount = data.get("amount", 0)
        if amount <= 0:
            return "The amount must be a positive number."
        if not (self.min_amount <= amount <= self.max_amount):
            return f"The amount must be between {self.min_amount} and {self.max_amount}."
        return None


class CardNumberValidation(ValidationStrategy):
    def validate(self, data):
        card_number = data.get("card_number", "")
        if not card_number.isdigit():
            return "The card number must contain only digits."
        if not self.luhn_algorithm(card_number):
            return "The card number is not valid."
        return None

    @staticmethod
    def luhn_algorithm(card_number):
        digits = [int(d) for d in card_number[::-1]]
        checksum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        return checksum % 10 == 0


class ExpirationDateValidation(ValidationStrategy):
    def validate(self, data):
        expiration_date = data.get("expiration_date", "")
        try:
            exp_date = datetime.strptime(expiration_date, "%m/%y")
            if exp_date < datetime.now():
                return "The card has expired."
        except ValueError:
            return "The expiration date must be in the format MM/YY."
        return None


class CVVValidation(ValidationStrategy):
    def validate(self, data):
        cvv = data.get("cvv", "")
        if not re.match(r"^\d{3,4}$", cvv):
            return "The CVV must contain 3 or 4 digits."
        return None


class CardTypeValidation(ValidationStrategy):
    def __init__(self, accepted_card_types):
        self.accepted_card_types = accepted_card_types

    def validate(self, data):
        card_type = data.get("card_type", "")
        if card_type not in self.accepted_card_types:
            return f"The card type '{card_type}' is not accepted. Accepted types: {', '.join(self.accepted_card_types)}."
        return None
    
# Main validator using strategies
class PaymentValidator:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def validate(self, data):
        errors = []
        for strategy in self.strategies:
            error = strategy.validate(data)
            if error:
                errors.append(error)
        return errors
