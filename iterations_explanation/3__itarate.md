Create an Interface for Notifications
We will define a base interface for the notifications that the different implementations will follow. This follows the Strategy Pattern, similar to what we did with validations.

```python
# notifications/notification_strategy.py

from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, message, recipient=None):
        """
        Sends a notification.

        param message: The message to send.
        param recipient: The recipient of the notification, if applicable.
        """
        pass
```

Implementing Specific Notifications
We will add several notification strategies. For simplicity, we will include a basic implementation for each type of notification.

Email Notification
```python
# notifications/email_notification.py

from notifications.notification_strategy import NotificationStrategy

class EmailNotification(NotificationStrategy):
    def send(self, message, recipient=None):
        if not recipient:
            raise ValueError("Recipient email is required for email notifications.")
        print(f"Sending Email to {recipient}: {message}")
```

Notificación por SMS
```python
# notifications/sms_notification.py

from notifications.notification_strategy import NotificationStrategy

class SMSNotification(NotificationStrategy):
    def send(self, message, recipient=None):
        if not recipient:
            raise ValueError("Recipient phone number is required for SMS notifications.")
        print(f"Sending SMS to {recipient}: {message}")

```

Notificación Interna (Logs)
```python
# notifications/log_notification.py

from notifications.notification_strategy import NotificationStrategy

class LogNotification(NotificationStrategy):
    def send(self, message, recipient=None):
        print(f"Internal Log: {message}")
```

Create a Notification Manager
The manager will handle notification strategies and send notifications as needed.
```python
# notifications/notification_manager.py

class NotificationManager:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def notify(self, message, recipient=None):
        for strategy in self.strategies:
            strategy.send(message, recipient)
```

