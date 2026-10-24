class MedicalRecord:
    """
    Represents a medical record created during a patient's visit.
    """

    def __init__(
        self,
        record_id,
        patient_id,
        doctor_id,
        diagnosis,
        symptoms,
        medicines
    ):
        """
        Initialize a MedicalRecord object.

        Args:
            record_id (str): Unique medical record ID.
            patient_id (str): Patient ID.
            doctor_id (str): Doctor ID.
            diagnosis (str): Patient diagnosis.
            symptoms (str): Patient symptoms.
            medicines (list): List of prescribed medicines.
        """

        self._record_id = record_id
        self._patient_id = patient_id
        self._doctor_id = doctor_id
        self._diagnosis = diagnosis
        self._symptoms = symptoms

        # List of medicines
        self._medicines = medicines

    def get_record_id(self):
        """Return the medical record ID."""
        return self._record_id

    def get_patient_id(self):
        """Return the patient ID."""
        return self._patient_id

    def get_doctor_id(self):
        """Return the doctor ID."""
        return self._doctor_id

    def get_diagnosis(self):
        """Return the diagnosis."""
        return self._diagnosis

    def get_symptoms(self):
        """Return the symptoms."""
        return self._symptoms

    def get_medicines(self):
        """Return the list of medicines."""
        return self._medicines

    def display_info(self):
        """Display the medical record."""

        print("\n========== MEDICAL RECORD ==========")
        print(f"Record ID  : {self._record_id}")
        print(f"Patient ID : {self._patient_id}")
        print(f"Doctor ID  : {self._doctor_id}")
        print(f"Symptoms   : {self._symptoms}")
        print(f"Diagnosis  : {self._diagnosis}")

        print("Medicines  :", end=" ")

        # Loop through the list of medicines
        for medicine in self._medicines:
            print(medicine, end=", ")

        print()