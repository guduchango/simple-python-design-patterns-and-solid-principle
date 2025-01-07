from validators import PaymentValidator, AmountValidation, CardNumberValidation, ExpirationDateValidation, CVVValidation, CardTypeValidation

if __name__ == "__main__":
    # Validator configuration
    validator = PaymentValidator()
    validator.add_strategy(AmountValidation())
    validator.add_strategy(CardNumberValidation())
    validator.add_strategy(ExpirationDateValidation())
    validator.add_strategy(CVVValidation())
    validator.add_strategy(CardTypeValidation(["Visa", "MasterCard", "Amex"]))

    # Example data
    payment_data = {
        "amount": 150.0,
        "card_number": "4111111111111111",
        "expiration_date": "12/25",
        "cvv": "123a3",
        "card_type": "Visaaa"
    }

    # Validation
    validation_errors = validator.validate(payment_data)

    if validation_errors:
        print("Validation errors:")
        for error in validation_errors:
            print(f"- {error}")
    else:
        print("Validation successful. The payment can be processed.")