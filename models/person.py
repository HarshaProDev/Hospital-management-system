class Person:
    """
    Represents a general person in the hospital system.

    This is the parent class for Patient and Doctor.
    """

    def __init__(self, name, age, phone):
        """
        Initialize a Person object.

        Args:
            name (str): Person's name.
            age (int): Person's age.
            phone (str): Person's phone number.
        """

        self._name = name
        self._age = age
        self._phone = phone

    def get_name(self):
        """Return the person's name."""
        return self._name

    def get_age(self):
        """Return the person's age."""
        return self._age

    def get_phone(self):
        """Return the person's phone number."""
        return self._phone

    def set_age(self, age):
        """Update the person's age."""
        self._age = age

    def set_phone(self, phone):
        """Update the person's phone number."""
        self._phone = phone

    def display_info(self):
        """Display basic information about the person."""

        print(f"Name  : {self._name}")
        print(f"Age   : {self._age}")
        print(f"Phone : {self._phone}")