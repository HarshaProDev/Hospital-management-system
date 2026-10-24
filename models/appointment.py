class Appointment:
    """
    Represents an appointment between a patient and a doctor.
    """

    def __init__(
        self,
        appointment_id,
        patient_id,
        doctor_id,
        date,
        time
    ):
        """
        Initialize an Appointment object.

        Args:
            appointment_id (str): Unique appointment ID.
            patient_id (str): ID of the patient.
            doctor_id (str): ID of the doctor.
            date (str): Appointment date.
            time (str): Appointment time.
        """

        self._appointment_id = appointment_id
        self._patient_id = patient_id
        self._doctor_id = doctor_id
        self._date = date
        self._time = time

        # Default appointment status
        self._status = "Scheduled"

    def get_appointment_id(self):
        """Return the appointment ID."""
        return self._appointment_id

    def get_patient_id(self):
        """Return the patient ID."""
        return self._patient_id

    def get_doctor_id(self):
        """Return the doctor ID."""
        return self._doctor_id

    def get_date(self):
        """Return the appointment date."""
        return self._date

    def get_time(self):
        """Return the appointment time."""
        return self._time

    def get_status(self):
        """Return the current appointment status."""
        return self._status

    def cancel(self):
        """Cancel the appointment."""
        self._status = "Cancelled"

    def display_info(self):
        """Display appointment information."""

        print("\n========== APPOINTMENT ==========")
        print(f"Appointment ID : {self._appointment_id}")
        print(f"Patient ID     : {self._patient_id}")
        print(f"Doctor ID      : {self._doctor_id}")
        print(f"Date           : {self._date}")
        print(f"Time           : {self._time}")
        print(f"Status         : {self._status}")