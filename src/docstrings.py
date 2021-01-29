def say_hi(name, age):
    """function example

    Args:
        param1 (str): name
        param2 (int): age

    Returns:
        bool: The return value

    """
    print(f"hi {name}")

    return True


say_hi("kenta", 31)

print(say_hi.__doc__)
help(say_hi)
