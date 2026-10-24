def validate_name(name):
    """
    Validate a person's name.

    Returns:
        bool: True if name is not empty.
    """
    return bool(name.strip())


def validate_age(age):
    """
    Validate a person's age.

    Returns:
        bool: True if age is between 1 and 120.
    """
    return 1 <= age <= 120


def validate_phone(phone):
    """
    Validate a phone number.

    Returns:
        bool: True if phone contains exactly 10 digits.
    """
    return phone.isdigit() and len(phone) == 10


def validate_blood_group(blood_group):
    """
    Validate blood group.

    Returns:
        bool: True if blood group is valid.
    """

    valid_groups = {
        "A+", "A-",
        "B+", "B-",
        "AB+", "AB-",
        "O+", "O-"
    }

    return blood_group.upper() in valid_groups