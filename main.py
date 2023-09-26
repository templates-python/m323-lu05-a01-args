def multiply_all(*args):
    """
    Multiplies all the given numbers together and returns the product.

    Parameters:
        *args (float or int): Variable number of arguments to be multiplied.

    Returns:
        float or int: The product of all the given numbers.
    """
    product = 1
    for num in args:
        product *= num
    return product


if __name__ == '__main__':
    # Teste deine Funktion
    print(multiply_all(1, 2, 3))  # Erwarteter Output: 6