from validators import PaymentValidator, AmountValidation, CardNumberValidation, ExpirationDateValidation, CVVValidation, CardTypeValidation
from configs import ACCEPTED_CARD_TYPES

# Example usage
if __name__ == "__main__":
    validator = PaymentValidator()
    validator.add_strategy(AmountValidation())
    validator.add_strategy(CardNumberValidation())
    validator.add_strategy(ExpirationDateValidation())
    validator.add_strategy(CVVValidation())
    validator.add_strategy(CardTypeValidation())

    payment_data = {
        "amount": 150.0,
        "card_number": "4111111111111111",
        "expiration_date": "12/254",
        "cvv": "123aa",
        "card_type": "Visa12"
    }

    validation_errors = validator.validate(payment_data)

    if validation_errors:
        print("Errores de validación:")
        for error in validation_errors:
            print(f"- {error}")
    else:
        print("Validación exitosa. El pago puede ser procesado.")