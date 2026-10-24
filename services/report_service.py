import csv
from pathlib import Path
import pandas as pd


class ReportService:
    """
    Exports hospital billing reports and analyzes billing data.
    """

    @staticmethod
    def export_bills_to_csv(bills):
        """Export all bills to a CSV file."""

        if not bills:
            print("No bills available to export.")
            return

        reports_folder = Path("reports")
        reports_folder.mkdir(parents=True, exist_ok=True)

        filename = reports_folder / "billing_report.csv"

        try:
            with open(
                filename,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                fieldnames = [
                    "bill_id",
                    "patient_id",
                    "consultation_fee",
                    "test_charges",
                    "medicine_charges",
                    "total",
                    "bill_date",
                    "payment_status"
                ]

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(bills)

            print(f"CSV report saved to: {filename}")

        except OSError as error:
            print(f"Could not export CSV: {error}")

    @staticmethod
    def analyze_bills(bills):
        """Analyze billing data using Pandas."""

        if not bills:
            print("No bills available for analysis.")
            return

        try:
            dataframe = pd.DataFrame(bills)

            total_billed = dataframe["total"].sum()

            total_collected = dataframe.loc[
                dataframe["payment_status"] == "Paid",
                "total"
            ].sum()

            unpaid_amount = dataframe.loc[
                dataframe["payment_status"] == "Unpaid",
                "total"
            ].sum()

            print("\n========== BILLING ANALYSIS ==========")
            print(f"Number of bills : {len(dataframe)}")
            print(f"Total billed    : Rs. {total_billed:.2f}")
            print(f"Total collected : Rs. {total_collected:.2f}")
            print(f"Unpaid amount   : Rs. {unpaid_amount:.2f}")

            print("\nPayment Status Summary:")
            print(
                dataframe.groupby("payment_status")["total"]
                .agg(["count", "sum"])
                .to_string()
            )

            reports_folder = Path("reports")
            reports_folder.mkdir(parents=True, exist_ok=True)

            summary = pd.DataFrame({
                "Metric": [
                    "Number of Bills",
                    "Total Billed",
                    "Total Collected",
                    "Unpaid Amount"
                ],
                "Value": [
                    len(dataframe),
                    total_billed,
                    total_collected,
                    unpaid_amount
                ]
            })

            summary.to_csv(
                reports_folder / "billing_summary.csv",
                index=False
            )

            print("\nAnalysis saved to reports/billing_summary.csv")

        except (KeyError, TypeError, ValueError) as error:
            print(f"Could not analyze billing data: {error}")