from models.medical_record import MedicalRecord
from services.file_service import FileService


class MedicalRecordService:
    """
    Manages patient medical records and JSON storage.
    """

    def __init__(self, filename="data/medical_records.json"):
        self._records = {}
        self._filename = filename
        self.load_records()

    def add_record(self, record):
        """Add a medical record if its ID is unique."""

        record_id = record.get_record_id()

        if record_id in self._records:
            print("Medical record ID already exists.")
            return False

        self._records[record_id] = record
        self.save_records()

        print("Medical record added successfully.")
        return True

    def view_patient_records(self, patient_id):
        """Display all medical records belonging to a patient."""

        found = False

        for record in self._records.values():
            if record.get_patient_id() == patient_id:
                record.display_info()
                found = True

        if not found:
            print("No medical records found for this patient.")

    def save_records(self):
        """Save medical records to a JSON file."""

        record_list = []

        for record in self._records.values():
            record_list.append({
                "record_id": record.get_record_id(),
                "patient_id": record.get_patient_id(),
                "doctor_id": record.get_doctor_id(),
                "diagnosis": record.get_diagnosis(),
                "symptoms": record.get_symptoms(),
                "medicines": record.get_medicines()
            })

        FileService.save_data(
            self._filename,
            record_list
        )

    def load_records(self):
        """Load medical records from a JSON file."""

        record_list = FileService.load_data(self._filename)

        for data in record_list:
            record = MedicalRecord(
                record_id=data["record_id"],
                patient_id=data["patient_id"],
                doctor_id=data["doctor_id"],
                diagnosis=data["diagnosis"],
                symptoms=data["symptoms"],
                medicines=data["medicines"]
            )

            self._records[
                record.get_record_id()
            ] = record