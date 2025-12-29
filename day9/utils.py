def calculate_discount(price: float) -> float:
    if price > 100:
        return price * 0.9
    return price