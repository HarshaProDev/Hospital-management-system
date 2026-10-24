from models.bill import Bill
from services.file_service import FileService


class BillingService:
    """
    Handles bill creation, payment tracking, and JSON storage.
    """

    def __init__(self, filename="data/bills.json"):
        self._bills = {}
        self._filename = filename
        self.load_bills()

    def generate_bill(
        self,
        bill_id,
        patient_id,
        consultation_fee,
        test_charges,
        medicine_charges,
        bill_date
    ):
        """Create a bill for a patient."""

        if bill_id in self._bills:
            print("Bill ID already exists.")
            return False

        bill = Bill(
            bill_id,
            patient_id,
            consultation_fee,
            test_charges,
            medicine_charges,
            bill_date
        )

        self._bills[bill_id] = bill
        self.save_bills()

        print("Bill generated successfully.")
        bill.display_info()
        return True

    def view_all_bills(self):
        """Display every bill."""

        if not self._bills:
            print("No bills found.")
            return

        for bill in self._bills.values():
            bill.display_info()

    def search_bill(self, bill_id):
        """Find a bill by its ID."""
        return self._bills.get(bill_id)

    def mark_bill_paid(self, bill_id):
        """Mark an existing bill as paid."""

        bill = self.search_bill(bill_id)

        if bill is None:
            print("Bill not found.")
            return False

        if bill.get_payment_status() == "Paid":
            print("This bill is already paid.")
            return False

        bill.mark_paid()
        self.save_bills()

        print("Payment recorded successfully.")
        return True

    def save_bills(self):
        """Save all bills to JSON."""

        bill_list = [
            bill.to_dict()
            for bill in self._bills.values()
        ]

        FileService.save_data(self._filename, bill_list)

    def load_bills(self):
        """Load saved bills from JSON."""

        bill_list = FileService.load_data(self._filename)

        for data in bill_list:
            bill = Bill(
                bill_id=data["bill_id"],
                patient_id=data["patient_id"],
                consultation_fee=data["consultation_fee"],
                test_charges=data["test_charges"],
                medicine_charges=data["medicine_charges"],
                bill_date=data["bill_date"]
            )

            if data.get("payment_status") == "Paid":
                bill.mark_paid()

            self._bills[bill.get_bill_id()] = bill

    def get_all_bills_as_dicts(self):
        """Return bill data for reporting."""
        return [
            bill.to_dict()
            for bill in self._bills.values()
        ]