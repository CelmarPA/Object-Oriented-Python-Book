# order_pizza_with_none.py

PRICE_OF_TOPPING: float = 1.50  # price for any topping

def order_pizza(size: str, style: str = "regular", topping: str | None = None) -> None:
    # Do some calculations based on the size and style
    # Check if a topping was specified


    if size == "small":
        price: float = 10.00

    elif size == "medium":
        price: float = 14.00

    else:   # large
        price: float = 18.00

    if style == "deepdish":
        price += 2.00   # charge extra for deepdish

    line: str = f"You have ordered a {size} {style} pizza with "

    if topping is None:
        print(line + "no topping")

    else:
        print(line + topping)
        price += PRICE_OF_TOPPING

    print(f"The price is ${price:.2f}")
    print()

# You could order a pizza in the following ways:
order_pizza('large') # large, defaults to regular, no topping
order_pizza('large', style='regular') # same as above
order_pizza('medium', style='deepdish', topping='mushrooms')
order_pizza('small', topping='mushrooms') # style defaults to regular
