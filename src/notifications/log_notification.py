# notifications/log_notification.py

from notifications.notification_strategy import NotificationStrategy

class LogNotification(NotificationStrategy):
    def send(self, message, recipient=None):
        print(f"Internal Log: {message}")