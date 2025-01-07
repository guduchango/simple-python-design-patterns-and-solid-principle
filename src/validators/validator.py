import re
from datetime import datetime

from typing import List, Dict, Optional, Any
from configs import MIN_AMOUNT,MAX_AMOUNT,ACCEPTED_CARD_TYPES


class ValidationError:
    """Encapsulates details about a validation error."""
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message

    def __str__(self) -> str:
        return f"[{self.field}] {self.message}"


# Interfaces for validation strategies
class ValidationStrategy:
    """Base class for validation strategies."""
    def validate(self, data: Dict[str, Any]) -> Optional[ValidationError]:
        raise NotImplementedError("This method must be implemented by subclasses.")


# Concrete validation strategies
class AmountValidation(ValidationStrategy):
    def validate(self, data):
        amount = data.get("amount", 0)
        if amount <= 0:
            return ValidationError(field="amount", message="The amount must be a positive number.")
        if not (MIN_AMOUNT <= amount <= MAX_AMOUNT):
            return ValidationError(field="amount", message=f"The amount must be between {MIN_AMOUNT} and {MAX_AMOUNT}.")
        return None


class CardNumberValidation(ValidationStrategy):
    def validate(self, data: Dict[str, Any]) -> Optional[ValidationError]:
        card_number = data.get("card_number", "")
        if not card_number.isdigit():
            return ValidationError("card_number", "Card number must contain only digits.")
        if not self.luhn_algorithm(card_number):
            return ValidationError("card_number", "Invalid card number.")
        return None

    @staticmethod
    def luhn_algorithm(card_number: str) -> bool:
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
    def validate(self, data: Dict[str, Any]) -> Optional[ValidationError]:
        expiration_date = data.get("expiration_date", "")
        try:
            exp_date = datetime.strptime(expiration_date, "%m/%y")
            if exp_date < datetime.now():
                return ValidationError("expiration_date", "The card has expired.")
        except ValueError:
            return ValidationError("expiration_date", "Expiration date format must be MM/YY.")
        return None


class CVVValidation(ValidationStrategy):
    def validate(self, data: Dict[str, Any]) -> Optional[ValidationError]:
        cvv = data.get("cvv", "")
        if not re.match(r"^\d{3,4}$", cvv):
            return ValidationError("cvv", "CVV must contain 3 or 4 digits.")
        return None


class CardTypeValidation(ValidationStrategy):
    def validate(self, data):
        card_type = data.get("card_type", "")
        if card_type not in ACCEPTED_CARD_TYPES:
            accepted_types = ", ".join(ACCEPTED_CARD_TYPES)
            return ValidationError(field="card_type", message=f"The card type '{card_type}' is not accepted. Accepted types: {accepted_types}.")
        return None
    

# Main Validator
class PaymentValidator:
    def __init__(self):
        self.strategies: List[ValidationStrategy] = []

    def add_strategy(self, strategy: ValidationStrategy) -> None:
        self.strategies.append(strategy)

    def validate(self, data: Dict[str, Any]) -> List[ValidationError]:
        errors = []
        for strategy in self.strategies:
            error = strategy.validate(data)
            if error:
                errors.append(error)
        return errors

