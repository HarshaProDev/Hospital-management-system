from models.patient import Patient
from models.doctor import Doctor

from services.patient_service import PatientService
from services.doctor_service import DoctorService

from models.appointment import Appointment
from models.medical_record import MedicalRecord

from services.appointment_service import AppointmentService
from services.medical_record_service import MedicalRecordService

from datetime import date

from services.billing_service import BillingService
from services.report_service import ReportService

from getpass import getpass
from services.auth_service import AuthService

from utils.validators import (
    validate_name,
    validate_age,
    validate_phone,
    validate_blood_group
)


def get_valid_age():
    """
    Get a valid age from the user.

    Returns:
        int: Valid age.
    """

    while True:

        try:
            age = int(input("Enter age: "))

            if validate_age(age):
                return age

            print("Age must be between 1 and 120.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_phone():
    """
    Get a valid phone number.

    Returns:
        str: Valid phone number.
    """

    while True:

        phone = input("Enter Phone: ")

        if validate_phone(phone):
            return phone

        print("Phone number must contain exactly 10 digits.")


def get_valid_blood_group():
    """
    Get a valid blood group.

    Returns:
        str: Valid blood group.
    """

    while True:

        blood_group = input(
            "Enter Blood Group: "
        ).upper()

        if validate_blood_group(blood_group):
            return blood_group

        print("Invalid blood group.")


def get_valid_name():
    """
    Get a valid name.

    Returns:
        str: Valid name.
    """

    while True:

        name = input("Enter Name: ")

        if validate_name(name):
            return name

        print("Name cannot be empty.")


def add_patient(patient_service):
    """Collect patient details and add a patient."""

    print("\n========== ADD PATIENT ==========")

    patient_id = input("Enter Patient ID: ")

    name = get_valid_name()

    age = get_valid_age()

    phone = get_valid_phone()

    gender = input("Enter Gender: ")

    blood_group = get_valid_blood_group()

    patient = Patient(
        patient_id=patient_id,
        name=name,
        age=age,
        phone=phone,
        gender=gender,
        blood_group=blood_group
    )

    patient_service.add_patient(patient)


def search_patient(patient_service):
    """Search and display a patient."""

    print("\n========== SEARCH PATIENT ==========")

    patient_id = input("Enter Patient ID: ")

    patient = patient_service.search_patient(
        patient_id
    )

    if patient:
        patient.display_info()
    else:
        print("Patient not found.")


def update_patient(patient_service):
    """Update patient information."""

    print("\n========== UPDATE PATIENT ==========")

    patient_id = input("Enter Patient ID: ")

    patient = patient_service.search_patient(
        patient_id
    )

    if patient is None:
        print("Patient not found.")
        return

    print("\n1. Update Phone")
    print("2. Update Age")

    choice = input("Enter choice: ")

    if choice == "1":

        phone = get_valid_phone()

        patient_service.update_patient(
            patient_id,
            phone=phone
        )

    elif choice == "2":

        age = get_valid_age()

        patient_service.update_patient(
            patient_id,
            age=age
        )

    else:
        print("Invalid choice.")


def delete_patient(patient_service):
    """Delete a patient."""

    print("\n========== DELETE PATIENT ==========")

    patient_id = input("Enter Patient ID: ")

    patient_service.delete_patient(
        patient_id
    )


def add_doctor(doctor_service):
    """Collect doctor details and add a doctor."""

    print("\n========== ADD DOCTOR ==========")

    doctor_id = input("Enter Doctor ID: ")

    name = get_valid_name()

    age = get_valid_age()

    phone = get_valid_phone()

    specialization = input(
        "Enter Specialization: "
    )

    doctor = Doctor(
        doctor_id=doctor_id,
        name=name,
        age=age,
        phone=phone,
        specialization=specialization
    )

    days = input(
        "Enter available days separated by comma: "
    )

    for day in days.split(","):

        day = day.strip()

        if day:
            doctor.add_available_day(day)

    doctor_service.add_doctor(doctor)


def search_doctor(doctor_service):
    """Search and display a doctor."""

    print("\n========== SEARCH DOCTOR ==========")

    doctor_id = input("Enter Doctor ID: ")

    doctor = doctor_service.search_doctor(
        doctor_id
    )

    if doctor:
        doctor.display_info()
    else:
        print("Doctor not found.")


def book_appointment(
    patient_service,
    doctor_service,
    appointment_service
):
    """Book an appointment for a registered patient."""

    print("\n========== BOOK APPOINTMENT ==========")

    appointment_id = input("Enter Appointment ID: ").strip()
    patient_id = input("Enter Patient ID: ").strip()
    doctor_id = input("Enter Doctor ID: ").strip()

    # Check whether the patient exists
    patient = patient_service.search_patient(patient_id)

    if patient is None:
        print("Patient not found. Register the patient first.")
        return

    # Check whether the doctor exists
    doctor = doctor_service.search_doctor(doctor_id)

    if doctor is None:
        print("Doctor not found. Register the doctor first.")
        return

    date = input("Enter appointment date (YYYY-MM-DD): ").strip()
    time = input("Enter appointment time (HH:MM): ").strip()

    if not date or not time:
        print("Date and time cannot be empty.")
        return

    appointment = Appointment(
        appointment_id=appointment_id,
        patient_id=patient_id,
        doctor_id=doctor_id,
        date=date,
        time=time
    )

    appointment_service.add_appointment(appointment)


def add_medical_record(
    patient_service,
    doctor_service,
    medical_record_service
):
    """Create a medical record for a registered patient."""

    print("\n========== ADD MEDICAL RECORD ==========")

    record_id = input("Enter Medical Record ID: ").strip()
    patient_id = input("Enter Patient ID: ").strip()
    doctor_id = input("Enter Doctor ID: ").strip()

    patient = patient_service.search_patient(patient_id)

    if patient is None:
        print("Patient not found. Register the patient first.")
        return

    doctor = doctor_service.search_doctor(doctor_id)

    if doctor is None:
        print("Doctor not found. Register the doctor first.")
        return

    symptoms = input("Enter Symptoms: ").strip()
    diagnosis = input("Enter Diagnosis: ").strip()

    medicines_input = input(
        "Enter Medicines separated by commas: "
    )

    medicines = [
        medicine.strip()
        for medicine in medicines_input.split(",")
        if medicine.strip()
    ]

    if not symptoms or not diagnosis:
        print("Symptoms and diagnosis cannot be empty.")
        return

    record = MedicalRecord(
        record_id=record_id,
        patient_id=patient_id,
        doctor_id=doctor_id,
        diagnosis=diagnosis,
        symptoms=symptoms,
        medicines=medicines
    )

    medical_record_service.add_record(record)


def get_valid_charge(prompt):
    """Get a valid non-negative monetary amount."""

    while True:
        try:
            amount = float(input(prompt))

            if amount < 0:
                print("Charge cannot be negative.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Invalid amount. Enter a number, such as 250 or 250.50.")

def generate_patient_bill(patient_service, billing_service):
    """Generate a bill for a registered patient."""

    print("\n========== GENERATE BILL ==========")

    bill_id = input("Enter Bill ID: ").strip()
    patient_id = input("Enter Patient ID: ").strip()

    patient = patient_service.search_patient(patient_id)

    if patient is None:
        print("Patient not found. Register the patient first.")
        return

    consultation_fee = get_valid_charge(
        "Enter Consultation Fee: Rs. "
    )

    test_charges = get_valid_charge(
        "Enter Test Charges: Rs. "
    )

    medicine_charges = get_valid_charge(
        "Enter Medicine Charges: Rs. "
    )

    billing_service.generate_bill(
        bill_id=bill_id,
        patient_id=patient_id,
        consultation_fee=consultation_fee,
        test_charges=test_charges,
        medicine_charges=medicine_charges,
        bill_date=date.today().isoformat()
    )


def has_permission(role, choice):
    """Check which menu operations a user may perform."""

    permissions = {
        "admin": {
            str(number) for number in range(1, 21)
        },

        "doctor": {
            "2", "3", "7", "8",
            "11", "13", "14"
        },

        "receptionist": {
            "1", "2", "3", "4", "5",
            "6", "7", "8",
            "10", "11", "12",
            "15", "16", "17", "18"
        }
    }

    # Everyone can exit.
    if choice == "9":
        return True

    return choice in permissions.get(role, set())


def login_system():
    auth_service = AuthService()

    # Create the first admin account on first launch.
    if not auth_service.users:
        print("\n========== FIRST-TIME SETUP ==========")
        print("Create your hospital administrator account.")

        while not auth_service.users:
            username = input("Create admin username: ").strip()
            password = getpass("Create admin password: ")
            confirm_password = getpass("Confirm admin password: ")

            if password != confirm_password:
                print("Passwords do not match. Try again.")
                continue

            auth_service.create_user(username, password, "admin")

    # Require login before entering the system.
    while True:
        print("\n========== HOSPITAL LOGIN ==========")
        username = input("Username: ").strip()
        password = getpass("Password: ")

        user = auth_service.authenticate(username, password)

        if user is not None:
            print(f"\nLogin successful. Welcome, {user['username']}!")
            print(f"Role: {user['role'].title()}")
            return auth_service, user

        print("Invalid username or password. Please try again.")


def create_hospital_user(auth_service):
    """Allow an authorized admin to register another account."""

    print("\n========== CREATE USER ==========")
    username = input("New username: ").strip()
    password = getpass("New password (minimum 8 characters): ")
    confirm_password = getpass("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return

    role = input(
        "Enter role (admin/doctor/receptionist): "
    ).strip().lower()

    auth_service.create_user(username, password, role)


def main():
    """
    Main function of the Hospital Patient Record System.
    """
    auth_service, current_user = login_system()
    # Create service objects.
    # Existing JSON data will automatically be loaded.
    patient_service = PatientService()
    doctor_service = DoctorService()
    appointment_service = AppointmentService()
    medical_record_service = MedicalRecordService()
    billing_service = BillingService()

    while True:

        print("\n======================================")
        print("   HOSPITAL PATIENT RECORD SYSTEM")
        print("======================================")

        print(
           f"\nLogged in: {current_user['username']} "
           f"({current_user['role'].title()})"
        )

        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Add Doctor")
        print("7. View All Doctors")
        print("8. Search Doctor")
        print("9. Exit")
        print("10. Book Appointment")
        print("11. View All Appointments")
        print("12. Cancel Appointment")
        print("13. Add Medical Record")
        print("14. View Patient Medical Records")
        print("15. Generate Patient Bill")
        print("16. View All Bills")
        print("17. Mark Bill as Paid")
        print("18. Export Bills to CSV")
        print("19. Analyze Billing Data")
        print("20. Create User (Admin Only)")

        choice = input("Enter your choice: ").strip()

        valid_choices = {str(number) for number in range(1, 21)}

        if choice not in valid_choices:
           print("Invalid choice. Please try again.")
           continue

        if not has_permission(current_user["role"], choice):
           print("Access denied. You do not have permission.")
           continue

        if choice == "1":
            add_patient(patient_service)

        elif choice == "2":
            patient_service.view_all_patients()

        elif choice == "3":
            search_patient(patient_service)

        elif choice == "4":
            update_patient(patient_service)

        elif choice == "5":
            delete_patient(patient_service)

        elif choice == "6":
            add_doctor(doctor_service)

        elif choice == "7":
            doctor_service.view_all_doctors()

        elif choice == "8":
            search_doctor(doctor_service)

        elif choice == "9":
            print("\nThank you for using the system.")
            break

        elif choice == "10":
            book_appointment(
                patient_service,
                doctor_service,
                appointment_service
            )

        elif choice == "11":
            appointment_service.view_all_appointments()

        elif choice == "12":
            appointment_id = input(
                "Enter Appointment ID to cancel: "
            ).strip()

            appointment_service.cancel_appointment(
                appointment_id
            )

        elif choice == "13":
            add_medical_record(
                patient_service,
                doctor_service,
                medical_record_service
            )

        elif choice == "14":
            patient_id = input(
                "Enter Patient ID: "
            ).strip()

            patient = patient_service.search_patient(patient_id)

            if patient is None:
                print("Patient not found.")
            else:
                medical_record_service.view_patient_records(
                    patient_id
                )

        elif choice == "15":
            generate_patient_bill(
                patient_service,
                billing_service
            )

        elif choice == "16":
            billing_service.view_all_bills()

        elif choice == "17":
            bill_id = input(
                "Enter Bill ID to mark as paid: "
            ).strip()

            billing_service.mark_bill_paid(bill_id)

        elif choice == "18":
            ReportService.export_bills_to_csv(
                billing_service.get_all_bills_as_dicts()
            )

        elif choice == "19":
            ReportService.analyze_bills(
                billing_service.get_all_bills_as_dicts()
            )

        elif choice == "20":
            create_hospital_user(auth_service)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()