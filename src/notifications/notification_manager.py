# notifications/notification_manager.py

class NotificationManager:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def notify(self, message, recipient=None):
        for strategy in self.strategies:
            strategy.send(message, recipient)