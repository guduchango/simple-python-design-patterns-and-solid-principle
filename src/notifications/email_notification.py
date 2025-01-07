# notifications/email_notification.py

from notifications.notification_strategy import NotificationStrategy

class EmailNotification(NotificationStrategy):
    def send(self, message, recipient=None):
        if not recipient:
            raise ValueError("Recipient email is required for email notifications.")
        print(f"Sending Email to {recipient}: {message}")