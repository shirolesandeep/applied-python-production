class OrderError(Exception):
    """Base class for order-related errors."""


class MissingOrderIdError(OrderError):
    """Raised when order ID is missing."""


class InvalidOrderAmountError(OrderError):
    """Raised when order amount is invalid."""


def process_order(order: dict) -> str:
    if "id" not in order:
        raise MissingOrderIdError("order must contain an 'id'")

    amount = order.get("amount")
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise InvalidOrderAmountError("order amount must be positive")

    return "Order processed"
