from models.patient import Patient
from services.file_service import FileService


class PatientService:
    """
    Handles patient management and JSON persistence.
    """

    def __init__(self, filename="data/patients.json"):
        self._patients = {}
        self._filename = filename

        # Load existing patients when program starts
        self.load_patients()

    def add_patient(self, patient):
        """Add a new patient."""

        patient_id = patient.get_patient_id()

        if patient_id in self._patients:
            print("Patient ID already exists.")
            return False

        self._patients[patient_id] = patient

        self.save_patients()

        print("Patient added successfully.")
        return True

    def view_all_patients(self):
        """Display all registered patients."""

        if not self._patients:
            print("No patients registered.")
            return

        print("\n========== ALL PATIENTS ==========")

        for patient in self._patients.values():
            patient.display_info()

    def search_patient(self, patient_id):
        """Search for a patient using patient ID."""

        return self._patients.get(patient_id)

    def update_patient(self, patient_id, phone=None, age=None):
        """Update patient information."""

        patient = self.search_patient(patient_id)

        if patient is None:
            print("Patient not found.")
            return False

        if phone is not None:
            patient.set_phone(phone)

        if age is not None:
            patient.set_age(age)

        self.save_patients()

        print("Patient updated successfully.")
        return True

    def delete_patient(self, patient_id):
        """Delete a patient."""

        if patient_id not in self._patients:
            print("Patient not found.")
            return False

        del self._patients[patient_id]

        self.save_patients()

        print("Patient deleted successfully.")
        return True

    def save_patients(self):
        """Save all patients into JSON."""

        patient_list = []

        for patient in self._patients.values():

            patient_data = {
                "patient_id": patient.get_patient_id(),
                "name": patient.get_name(),
                "age": patient.get_age(),
                "phone": patient.get_phone(),
                "gender": patient.get_gender(),
                "blood_group": patient.get_blood_group()
            }

            patient_list.append(patient_data)

        FileService.save_data(
            self._filename,
            patient_list
        )

    def load_patients(self):
        """Load patients from JSON."""

        patient_list = FileService.load_data(
            self._filename
        )

        for data in patient_list:

            patient = Patient(
                patient_id=data["patient_id"],
                name=data["name"],
                age=data["age"],
                phone=data["phone"],
                gender=data["gender"],
                blood_group=data["blood_group"]
            )

            self._patients[
                patient.get_patient_id()
            ] = patient