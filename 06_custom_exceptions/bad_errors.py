def process_order(order):
    if "id" not in order:
        raise Exception("Invalid order")

    if order.get("amount", 0) <= 0:
        raise Exception("Invalid order")

    return "Order processed"