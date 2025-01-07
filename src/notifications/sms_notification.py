# notifications/sms_notification.py

from notifications import NotificationStrategy

class SMSNotification(NotificationStrategy):
    def send(self, message, recipient=None):
        if not recipient:
            raise ValueError("Recipient phone number is required for SMS notifications.")
        print(f"Sending SMS to {recipient}: {message}")