"""
WhatsApp Group Member Adder Automation
This script automates the process of adding members to a WhatsApp group using Google Contacts.
"""

import os
import tkinter as tk
from tkinter import messagebox
from contactmaker import generate_contacts_csv
from googleimport import ContactImporter

class WhatsAppAutomation:
    def __init__(self):
        """Initialize the WhatsApp automation class."""
        self.contacts_file = "contacts.txt"
        self.csv_file = "contacts.csv"

    def show_message(self, title: str, message: str) -> bool:
        """
        Show a popup message to the user.
        
        Args:
            title (str): Title of the popup
            message (str): Message to display
            
        Returns:
            bool: User's response (True for Yes, False for No)
        """
        root = tk.Tk()
        root.withdraw()
        response = messagebox.askyesno(title, message)
        root.destroy()
        return response

    def check_required_files(self) -> bool:
        """
        Check if required files exist.
        
        Returns:
            bool: True if all required files are present or created successfully
        """
        # Check for contacts.txt
        if not os.path.exists(self.contacts_file):
            self.show_message("Error", "Please create contacts.txt file first!")
            return False

        # Generate contacts.csv if needed
        if not os.path.exists(self.csv_file):
            print("\nGenerating contacts.csv...")
            generate_contacts_csv()
            print("✅ contacts.csv generated successfully!")

        return True

    def run(self):
        """Execute the main automation workflow."""
        try:
            print("Starting WhatsApp Group Member Adder...")

            # Step 1: Check required files
            if not self.check_required_files():
                return

            # Step 2: Initialize Contact Importer
            print("\nStarting Chrome for Google Contacts import...")
            importer = ContactImporter()

            # Step 3: Import contacts to Google
            if not importer.import_contacts():
                print("❌ Failed to import contacts to Google!")
                return

            # Step 4: Add contacts to WhatsApp group
            print("\nStarting WhatsApp automation...")
            if not importer.add_to_whatsapp():
                print("❌ Failed to add contacts to WhatsApp group!")
                return

            print("\n✅ All tasks completed successfully!")

        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            print(f"\n❌ {error_msg}")
            self.show_message("Error", error_msg)

def main():
    """Main entry point of the script."""
    automation = WhatsAppAutomation()
    automation.run()

if __name__ == "__main__":
    main() 