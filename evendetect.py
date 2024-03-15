def is_even(input_num) -> bool:
    """
    Check if the input is an even integer.
    
    Parameters:
    input_num (int): The input number to be checked.
    
    Returns:
    bool: True if input is an even integer, False otherwise.
    """
    try:
        input_num = int(input_num)
        return input_num % 2 == 0
    except (ValueError, TypeError):
        return False
