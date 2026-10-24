class Bill:
    """
    Represents a hospital bill.
    """

    def __init__(
        self,
        bill_id,
        patient_id,
        consultation_fee,
        test_charges,
        medicine_charges,
        bill_date
    ):
        """Initialize a bill and calculate the total."""

        self._bill_id = bill_id
        self._patient_id = patient_id
        self._consultation_fee = consultation_fee
        self._test_charges = test_charges
        self._medicine_charges = medicine_charges
        self._bill_date = bill_date

        self._total = (
            consultation_fee
            + test_charges
            + medicine_charges
        )

        self._payment_status = "Unpaid"

    def get_bill_id(self):
        """Return the bill ID."""
        return self._bill_id

    def get_patient_id(self):
        """Return the patient ID."""
        return self._patient_id

    def get_total(self):
        """Return the total bill amount."""
        return self._total

    def get_payment_status(self):
        """Return the payment status."""
        return self._payment_status

    def mark_paid(self):
        """Mark the bill as paid."""
        self._payment_status = "Paid"

    def to_dict(self):
        """Convert the bill into a dictionary for JSON storage."""

        return {
            "bill_id": self._bill_id,
            "patient_id": self._patient_id,
            "consultation_fee": self._consultation_fee,
            "test_charges": self._test_charges,
            "medicine_charges": self._medicine_charges,
            "total": self._total,
            "bill_date": self._bill_date,
            "payment_status": self._payment_status
        }

    def display_info(self):
        """Display bill details."""

        print("\n========== HOSPITAL BILL ==========")
        print(f"Bill ID           : {self._bill_id}")
        print(f"Patient ID        : {self._patient_id}")
        print(f"Bill Date         : {self._bill_date}")
        print(f"Consultation Fee  : Rs. {self._consultation_fee:.2f}")
        print(f"Test Charges      : Rs. {self._test_charges:.2f}")
        print(f"Medicine Charges  : Rs. {self._medicine_charges:.2f}")
        print(f"Total             : Rs. {self._total:.2f}")
        print(f"Payment Status    : {self._payment_status}")