from models.person import Person


class Doctor(Person):
    """
    Represents a doctor working in the hospital.

    Doctor inherits common information from Person.
    """

    def __init__(
        self,
        doctor_id,
        name,
        age,
        phone,
        specialization
    ):
        """
        Initialize a Doctor object.

        Args:
            doctor_id (str): Unique doctor ID.
            name (str): Doctor's name.
            age (int): Doctor's age.
            phone (str): Doctor's phone number.
            specialization (str): Doctor's specialization.
        """

        super().__init__(name, age, phone)

        self._doctor_id = doctor_id
        self._specialization = specialization

        # Set prevents duplicate available days
        self._available_days = set()

    def get_doctor_id(self):
        """Return the doctor's ID."""
        return self._doctor_id

    def get_specialization(self):
        """Return the doctor's specialization."""
        return self._specialization

    def add_available_day(self, day):
        """Add a working day to the doctor's schedule."""

        self._available_days.add(day)

    def get_available_days(self):
        """Return available working days."""

        return self._available_days

    def display_info(self):
        """Display doctor information."""

        print("\n========== DOCTOR INFORMATION ==========")
        print(f"Doctor ID      : {self._doctor_id}")
        print(f"Name           : {self._name}")
        print(f"Age            : {self._age}")
        print(f"Phone          : {self._phone}")
        print(f"Specialization : {self._specialization}")

        print("Available Days :", end=" ")

        for day in sorted(self._available_days):
            print(day, end=" ")

        print()