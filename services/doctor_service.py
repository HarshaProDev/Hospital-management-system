from models.doctor import Doctor
from services.file_service import FileService


class DoctorService:
    """
    Handles doctor management and JSON persistence.
    """

    def __init__(self, filename="data/doctors.json"):
        self._doctors = {}
        self._filename = filename

        # Load doctors when program starts
        self.load_doctors()

    def add_doctor(self, doctor):
        """Add a new doctor."""

        doctor_id = doctor.get_doctor_id()

        if doctor_id in self._doctors:
            print("Doctor ID already exists.")
            return False

        self._doctors[doctor_id] = doctor

        self.save_doctors()

        print("Doctor added successfully.")
        return True

    def view_all_doctors(self):
        """Display all registered doctors."""

        if not self._doctors:
            print("No doctors registered.")
            return

        print("\n========== ALL DOCTORS ==========")

        for doctor in self._doctors.values():
            doctor.display_info()

    def search_doctor(self, doctor_id):
        """Search for a doctor using doctor ID."""

        return self._doctors.get(doctor_id)

    def save_doctors(self):
        """Save all doctors into JSON."""

        doctor_list = []

        for doctor in self._doctors.values():

            doctor_data = {
                "doctor_id": doctor.get_doctor_id(),
                "name": doctor.get_name(),
                "age": doctor.get_age(),
                "phone": doctor.get_phone(),
                "specialization": doctor.get_specialization(),
                "available_days": list(
                    doctor.get_available_days()
                )
            }

            doctor_list.append(doctor_data)

        FileService.save_data(
            self._filename,
            doctor_list
        )

    def load_doctors(self):
        """Load doctors from JSON."""

        doctor_list = FileService.load_data(
            self._filename
        )

        for data in doctor_list:

            doctor = Doctor(
                doctor_id=data["doctor_id"],
                name=data["name"],
                age=data["age"],
                phone=data["phone"],
                specialization=data["specialization"]
            )

            for day in data["available_days"]:
                doctor.add_available_day(day)

            self._doctors[
                doctor.get_doctor_id()
            ] = doctor