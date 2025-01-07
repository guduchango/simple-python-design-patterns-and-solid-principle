from validators import PaymentValidator

if __name__ == "__main__":
    # Datos de ejemplo
    payment_data = {
        "amount": 150.0,
        "card_number": "4111111111111111",
        "expiration_date": "12/25",
        "cvv": "123",
        "card_type": "Visa"
    }

    validator = PaymentValidator()
    validation_errors = validator.validate_payment(payment_data)

    if validation_errors:
        print("Errores de validación:")
        for error in validation_errors:
            print(f"- {error}")
    else:
        print("Validación exitosa. El pago puede ser procesado.")