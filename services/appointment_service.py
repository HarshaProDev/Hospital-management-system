from models.appointment import Appointment
from services.file_service import FileService


class AppointmentService:
    """
    Manages hospital appointments and JSON storage.
    """

    def __init__(self, filename="data/appointments.json"):
        self._appointments = {}
        self._filename = filename
        self.load_appointments()

    def add_appointment(self, appointment):
        """Add an appointment if its ID is unique."""

        appointment_id = appointment.get_appointment_id()

        if appointment_id in self._appointments:
            print("Appointment ID already exists.")
            return False

        self._appointments[appointment_id] = appointment
        self.save_appointments()

        print("Appointment booked successfully.")
        return True

    def view_all_appointments(self):
        """Display all appointments."""

        if not self._appointments:
            print("No appointments found.")
            return

        print("\n========== ALL APPOINTMENTS ==========")

        for appointment in self._appointments.values():
            appointment.display_info()

    def search_appointment(self, appointment_id):
        """Find an appointment using its ID."""

        return self._appointments.get(appointment_id)

    def cancel_appointment(self, appointment_id):
        """Cancel an existing appointment."""

        appointment = self.search_appointment(appointment_id)

        if appointment is None:
            print("Appointment not found.")
            return False

        if appointment.get_status() == "Cancelled":
            print("Appointment is already cancelled.")
            return False

        appointment.cancel()
        self.save_appointments()

        print("Appointment cancelled successfully.")
        return True

    def save_appointments(self):
        """Save appointments to a JSON file."""

        appointment_list = []

        for appointment in self._appointments.values():
            appointment_list.append({
                "appointment_id": appointment.get_appointment_id(),
                "patient_id": appointment.get_patient_id(),
                "doctor_id": appointment.get_doctor_id(),
                "date": appointment.get_date(),
                "time": appointment.get_time(),
                "status": appointment.get_status()
            })

        FileService.save_data(
            self._filename,
            appointment_list
        )

    def load_appointments(self):
        """Load appointments from a JSON file."""

        appointment_list = FileService.load_data(self._filename)

        for data in appointment_list:
            appointment = Appointment(
                appointment_id=data["appointment_id"],
                patient_id=data["patient_id"],
                doctor_id=data["doctor_id"],
                date=data["date"],
                time=data["time"]
            )

            if data.get("status") == "Cancelled":
                appointment.cancel()

            self._appointments[
                appointment.get_appointment_id()
            ] = appointment