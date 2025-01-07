Crear una Interfaz para Notificaciones
Definiremos una interfaz base para las notificaciones que las diferentes implementaciones seguirán. Esto sigue el Patrón Strategy, similar a lo que hicimos con las validaciones.

```python
# notifications/notification_strategy.py

from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, message, recipient=None):
        """
        Envía una notificación.

        :param message: El mensaje a enviar.
        :param recipient: El destinatario de la notificación, si aplica.
        """
        pass
```

Implementar Notificaciones Concretas
Añadiremos varias estrategias de notificación. Por simplicidad, incluiremos una implementación básica para cada tipo de notificación.

Notificación por Email
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

Crear un Gestor de Notificaciones
El gestor se encargará de manejar las estrategias de notificación y de enviar notificaciones según sea necesario.
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

