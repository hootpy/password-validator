def validate_pw(password: str) -> bool:
    """
    Validate password

    :param password: password
    :type password: str
    :return: True if password is valid, False otherwise
    :rtype: bool
    """
    # Password must have at least 8 characters
    if len(password) < 8:
        return False

    # Password must have at least 1 lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Password must have at least 1 uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # # Password must have at least 1 digit
    # if not any(char.isdigit() for char in password):
    #     return False

    # # Password must have at least 1 special character
    # special_characters = "!@#$%^&*()-+"
    # return any((char in special_characters for char in password))
