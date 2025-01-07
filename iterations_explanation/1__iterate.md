How Our Example Works
1. Base Interface: ValidationStrategy

It is an abstract class that defines the “contract”. All validations have to implement the validate method.
This ensures that the validations are consistent.

```python
class ValidationStrategy:
    def validate(self, data):
        raise NotImplementedError("You must implement the 'validate' method.")

```
2. Concrete Strategies

Each specific validation (e.g., validating amounts, dates, CVV, etc.) is a separate class that implements the ValidationStrategy interface.

For example, AmountValidation is responsible only for validating the amount:

```python
class AmountValidation(ValidationStrategy):
    def validate(self, data):
        amount = data.get("amount", 0)
        if amount <= 0:
            return "The amount must be a positive number."
        return None

```
Advantage: If tomorrow you need another validation, you only have to create a new class without touching the others.

3. Main Validator: PaymentValidator

It is a “container” of strategies. You decide which validations to add.
This validator goes through all the strategies and applies each validation to the dataset.

```python
class PaymentValidator:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def validate(self, data):
        errors = []
        for strategy in self.strategies:
            error = strategy.validate(data)
            if error:
                errors.append(error)
        return errors

```
4. Practical Use

First you configure the validator by adding the strategies you want to use:

```python
validator.add_strategy(AmountValidation())
validator.add_strategy(CardNumberValidation())
```
Then you validate the payment data:

```python
payment_data = {
    "amount": 150.0,
    "card_number": "4111111111111111",
    "expiration_date": "12/25",
    "cvv": "123",
    "card_type": "Visa"
}

validation_errors = validator.validate(payment_data)
```
The validator passes the data to each strategy and collects any errors found.

5. Advantages of the Change
* Modularity: Each validation is separated in its own class.
* Scalability: You can easily add new validations without modifying the existing ones.
* Maintainability: If there is an error in a validation, you only have to check its class.
* Reusability: You can use the same validations in other projects or contexts.
