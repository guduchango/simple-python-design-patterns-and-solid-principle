from validators import PaymentValidator, AmountValidation, CardNumberValidation, ExpirationDateValidation, CVVValidation, CardTypeValidation
from configs import ACCEPTED_CARD_TYPES
from notifications import NotificationManager, LogNotification,EmailNotification,SMSNotification

# Example usage
if __name__ == "__main__":

        # Configurar el gestor de notificaciones
    notification_manager = NotificationManager()
    notification_manager.add_strategy(LogNotification())
    notification_manager.add_strategy(EmailNotification())
    notification_manager.add_strategy(SMSNotification())

    validator = PaymentValidator()
    validator.add_strategy(AmountValidation())
    validator.add_strategy(CardNumberValidation())
    validator.add_strategy(ExpirationDateValidation())
    validator.add_strategy(CVVValidation())
    validator.add_strategy(CardTypeValidation())

    payment_data = {
        "amount": 150.0,
        "card_number": "4111111111111111",
        "expiration_date": "12/25",
        "cvv": "123",
        "card_type": "Visa"
    }

    validation_errors = validator.validate(payment_data)

    if validation_errors:
        notification_manager.notify("Validation errors occurred.", recipient="admin@example.com")
        for error in validation_errors:
            notification_manager.notify(f"- {error}")
    else:
        notification_manager.notify("Payment validation successful.", recipient="user@example.com")