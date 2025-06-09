"""
WhatsApp Group Member Adder - Google Contacts Integration
This module handles the integration with Google Contacts and WhatsApp Web for adding group members.
"""

import os
import time
from typing import List, Optional
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import tkinter as tk
from tkinter import messagebox

class ContactImporter:
    """Handles the automation of importing contacts to Google and adding them to WhatsApp groups."""
    
    def __init__(self):
        """Initialize the ContactImporter with default configuration."""
        self.driver: Optional[uc.Chrome] = None
        self.wait: Optional[WebDriverWait] = None
        self.contacts_file = "contacts.txt"
        self.csv_file = "contacts.csv"
        self.country_code = "91"  # Default country code for India
        self.wait_time = 20  # Default wait time in seconds
    
    def create_driver(self) -> bool:
        """
        Create and configure the Chrome WebDriver.
        
        Returns:
            bool: True if driver creation successful, False otherwise
        """
        try:
            options = uc.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--start-maximized')
            options.add_argument('--disable-popup-blocking')
            options.add_argument('--disable-notifications')
            
            self.driver = uc.Chrome(version_main=136, options=options, use_subprocess=True)
            self.wait = WebDriverWait(self.driver, self.wait_time)
            return True
        except Exception as e:
            print(f"❌ Failed to start Chrome: {e}")
            return False

    def wait_for_element(self, by: By, value: str, timeout: int = None) -> Optional[any]:
        """
        Wait for an element to be clickable and return it.
        
        Args:
            by: Selenium By locator
            value: Selector value
            timeout: Optional custom timeout
            
        Returns:
            Optional[WebElement]: The found element or None
        """
        try:
            wait = WebDriverWait(self.driver, timeout or self.wait_time)
            return wait.until(EC.element_to_be_clickable((by, value)))
        except TimeoutException:
            return None

    def import_contacts(self) -> bool:
        """
        Import contacts from CSV file to Google Contacts.
        
        Returns:
            bool: True if import successful, False otherwise
        """
        if not self.create_driver():
            return False
            
        try:
            print("\n📱 Starting Google Contacts import process...")
            self.driver.get("https://contacts.google.com/")
            input("✋ Sign in to Google Contacts and press Enter to continue...")
            
            # Click Import button
            import_button = self.wait_for_element(By.CLASS_NAME, "d5NbRd-EScbFb-JIbuQc.dgqZp")
            if not import_button:
                raise Exception("Import button not found")
            import_button.click()
            time.sleep(2)
            
            # Upload CSV file
            file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(os.path.abspath(self.csv_file))
            time.sleep(2)
            
            # Click final import button
            final_import = self.wait_for_element(
                By.XPATH, 
                "//button[contains(@class, 'mUIrbf-LgbsSe') and .//span[text()='Import']]"
            )
            if not final_import:
                raise Exception("Final import button not found")
            final_import.click()
            
            print("✅ Contacts imported successfully!")
            time.sleep(5)
            return True
            
        except Exception as e:
            print(f"❌ Error during import: {e}")
            return False

    def find_group_header(self) -> Optional[any]:
        """Find the WhatsApp group header using multiple fallback methods."""
        try:
            # Method 1: Exact header class
            return self.driver.find_element(
                By.CLASS_NAME, 
                "x1n2onr6.x9f619.x78zum5.x6s0dn4.xh8yej3.x7j6532.x1pl83jw.x1j6awrg.x1te75w5.x162n7g1"
            )
        except NoSuchElementException:
            try:
                # Method 2: Profile details button
                return self.driver.find_element(
                    By.CSS_SELECTOR, 
                    'div[title="Profile details"][role="button"]'
                )
            except NoSuchElementException:
                try:
                    # Method 3: Group name span
                    span = self.driver.find_element(
                        By.CSS_SELECTOR, 
                        'span[dir="auto"][class*="_ao3e"]'
                    )
                    return span.find_element(By.XPATH, "../../../..")
                except NoSuchElementException:
                    # Method 4: Header with partial class match
                    return self.driver.find_element(
                        By.CSS_SELECTOR, 
                        'header[class*="x1n2onr6"][class*="x78zum5"]'
                    )

    def click_button_with_retry(self, primary_method: callable, fallback_method: callable, 
                              button_name: str, wait_time: int = 4) -> bool:
        """
        Try to click a button using primary and fallback methods.
        
        Args:
            primary_method: Primary method to find and click button
            fallback_method: Fallback method if primary fails
            button_name: Name of the button for logging
            wait_time: Time to wait before/after clicking
            
        Returns:
            bool: True if button was clicked successfully
        """
        print(f"\n⏳ Waiting for {button_name}...")
        time.sleep(wait_time)
        
        try:
            primary_method()
            print(f"✅ Found and clicked {button_name} using primary method")
            return True
        except Exception as e:
            print(f"ℹ️ Primary method failed: {str(e)}")
            print("↪️ Trying alternative method...")
            
            try:
                fallback_method()
                print(f"✅ Found and clicked {button_name} using fallback method")
                return True
            except Exception as e:
                print(f"❌ All methods failed for {button_name}: {str(e)}")
                return False

    def click_confirm_button(self) -> bool:
        """Click the confirm button with fallback methods."""
        def primary():
            confirm = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-icon="checkmark-medium"]'))
            )
            confirm.click()
            
        def fallback():
            buttons = self.driver.find_elements(By.TAG_NAME, "div")
            for button in buttons:
                if (button.get_attribute("role") == "button" and 
                    "checkmark-medium" in button.get_attribute("innerHTML")):
                    button.click()
                    return
            raise Exception("Confirm button not found in fallback")
            
        return self.click_button_with_retry(primary, fallback, "confirm button")

    def click_add_member_button(self) -> bool:
        """Click the final add member button with fallback methods."""
        def primary():
            button = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Add member')]/ancestor::button")
                )
            )
            button.click()
            
        def fallback():
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if "Add member" in button.text:
                    button.click()
                    return
            raise Exception("Add member button not found in fallback")
            
        return self.click_button_with_retry(primary, fallback, "Add member button")

    def add_contacts_to_group(self) -> bool:
        """Add contacts from file to the WhatsApp group."""
        try:
            # Read contacts from file
            with open(self.contacts_file, "r") as file:
                contacts = [line.strip() for line in file if line.strip()]

            # Add each contact
            for i, contact in enumerate(contacts, 1):
                contact = f"{self.country_code}{contact}"  # Add country code
                print(f"👤 Adding contact {i}/{len(contacts)}: {contact}")

                number_input = self.driver.find_element(
                    By.CLASS_NAME, 
                    "selectable-text.copyable-text.x15bjb6t.x1n2onr6"
                )
                number_input.send_keys(contact)
                time.sleep(1)
                number_input.send_keys(Keys.ENTER)
                time.sleep(2)

            # Click confirm and add member buttons
            if not self.click_confirm_button():
                return False
                
            if not self.click_add_member_button():
                return False

            print("\n⏳ Waiting for process to complete...")
            time.sleep(10)  # Reduced from 360 to 10 seconds
            print("✅ All members added successfully!")
            return True

        except Exception as e:
            print(f"\n❌ Error adding contacts: {e}")
            return False

    def add_to_whatsapp(self) -> bool:
        """
        Add contacts to a WhatsApp group.
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.driver and not self.create_driver():
            return False
                
        try:
            print("\n📱 Starting WhatsApp Web automation...")
            self.driver.get("https://web.whatsapp.com/")
            
            print("\nPlease:")
            print("1. 📱 Scan the WhatsApp QR code")
            print("2. ⏳ Wait until you see your chats")
            print("3. ↩️ Press Enter to continue")
            input("Press Enter when ready...")

            # Get group name and search
            group_name = input("\n👥 Enter your WhatsApp group name: ")
            print(f"\n🔍 Searching for group: {group_name}")
            
            search_box = self.driver.find_element(
                By.CLASS_NAME, 
                "selectable-text.copyable-text.x15bjb6t.x1n2onr6"
            )
            search_box.send_keys(group_name)
            time.sleep(2)
            search_box.send_keys(Keys.ENTER)

            # Open group info and click add member
            time.sleep(3)
            group_header = self.find_group_header()
            if not group_header:
                raise Exception("Could not find group header")
            group_header.click()
            time.sleep(2)

            add_option = self.driver.find_element(
                By.CLASS_NAME, 
                "_ak72.false._ak73._ak76._ak77"
            )
            add_option.click()

            # Add contacts to group
            return self.add_contacts_to_group()

        except Exception as e:
            print(f"\n❌ Error during WhatsApp automation: {e}")
            return False
        finally:
            input("\n↩️ Press Enter to close the browser...")
            if self.driver:
                self.driver.quit()

def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askyesno(title, message)
    root.destroy()
    return response

def main():
    if not os.path.exists("contacts.txt"):
        show_popup("Error", "Please create number.txt file first!")
        return
    
    if show_popup("Continue", "Do you want to import contacts to Google Contacts?"):
        if not os.path.exists("contacts.csv"):
            show_popup("Error", "Please run contactmaker.py first to generate contacts.csv!")
            return
            
        importer = ContactImporter()
        if importer.import_contacts():
            show_popup("Success", "Contacts imported successfully!")
        else:
            show_popup("Error", "Failed to import contacts. Please try again.")

if __name__ == "__main__":
    main()