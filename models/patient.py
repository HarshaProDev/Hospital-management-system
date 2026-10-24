from models.person import Person


class Patient(Person):
    """
    Represents a patient registered in the hospital.

    Patient inherits common information from Person and
    adds patient-specific information.
    """

    def __init__(
        self,
        patient_id,
        name,
        age,
        phone,
        gender,
        blood_group
    ):
        """
        Initialize a Patient object.

        Args:
            patient_id (str): Unique patient ID.
            name (str): Patient's name.
            age (int): Patient's age.
            phone (str): Patient's phone number.
            gender (str): Patient's gender.
            blood_group (str): Patient's blood group.
        """

        # Initialize attributes inherited from Person
        super().__init__(name, age, phone)

        self._patient_id = patient_id
        self._gender = gender
        self._blood_group = blood_group

        # List used to store the patient's medical history
        self._medical_history = []

    def get_patient_id(self):
        """Return the patient's unique ID."""
        return self._patient_id

    def get_gender(self):
        """Return the patient's gender."""
        return self._gender

    def get_blood_group(self):
        """Return the patient's blood group."""
        return self._blood_group

    def add_medical_record(self, record):
        """
        Add a medical record to the patient's history.

        Args:
            record (MedicalRecord): Medical record object.
        """

        self._medical_history.append(record)

    def get_medical_history(self):
        """Return the patient's medical history."""
        return self._medical_history

    def display_info(self):
        """Display complete patient information."""

        print("\n========== PATIENT INFORMATION ==========")
        print(f"Patient ID  : {self._patient_id}")
        print(f"Name        : {self._name}")
        print(f"Age         : {self._age}")
        print(f"Phone       : {self._phone}")
        print(f"Gender      : {self._gender}")
        print(f"Blood Group : {self._blood_group}")
        print(f"Records     : {len(self._medical_history)}")