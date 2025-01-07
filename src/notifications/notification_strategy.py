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