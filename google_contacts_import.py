import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import tkinter as tk
from tkinter import messagebox
import os
import time

def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    response = messagebox.askyesno(title, message)
    root.destroy()
    return response

def check_file_exists(filename):
    return os.path.exists(filename)

def create_driver():
    print("Configuring Chrome...")
    options = uc.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    
    try:
        driver = uc.Chrome(
            version_main=136,  # Explicitly set to your Chrome version
            options=options,
            use_subprocess=True
        )
        return driver
    except Exception as e:
        print(f"Failed to create Chrome instance: {str(e)}")
        return None

def import_to_google_contacts():
    driver = create_driver()
    if not driver:
        print("Failed to start Chrome. Please try again.")
        return False
        
    try:
        # Navigate to Google Contacts
        print("Opening Google Contacts...")
        driver.get("https://contacts.google.com/")
        
        # Wait for user to login and verify
        print("\nPlease:")
        print("1. Sign in to your Google account")
        print("2. Wait until you see your contacts page")
        print("3. Press Enter to continue")
        input("Press Enter when ready...")
        
        # Wait for and click the Import button
        print("Looking for Import button...")
        wait = WebDriverWait(driver, 20)
        import_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "d5NbRd-EScbFb-JIbuQc.dgqZp"))
        )
        import_button.click()
        time.sleep(2)  # Wait for dialog to fully open
        
        # Wait for and click the Select File button
        print("Selecting file...")
        select_file_button = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "UywwFc-LgbsSe.UywwFc-LgbsSe-OWXEXe-dgl2Hf.UywwFc-StrnGf-YYd4I-VtOx3e.UywwFc-kSE8rc-FoKg4d-sLO9V-YoZ4jf")
            )
        )
        
        # Send the file path to the input
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        abs_path = os.path.abspath("contacts.csv")
        print(f"Using file: {abs_path}")
        file_input.send_keys(abs_path)
        time.sleep(2)  # Wait for file to be processed
        
        # Click the final Import button with the correct class
        print("Clicking final Import button...")
        try:
            final_import_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-dgl2Hf-ppHlrf-sM5MNb"))
            )
            final_import_button.click()
        except TimeoutException:
            print("Could not find Import button automatically.")
            print("Please click the Import button manually and press Enter when done.")
            input()
        
        # Wait for import to complete
        print("Waiting for import to complete...")
        time.sleep(5)
        print("✅ Contacts imported successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        return False
    finally:
        print("\nClosing browser...")
        try:
            input("Press Enter to close the browser...")
            driver.quit()
        except:
            pass

def main():
    # First check if numbers.txt exists
    if not check_file_exists("number.txt"):
        show_popup("Error", "Please create number.txt file first!")
        return
    
    # Ask if user wants to proceed with contact import
    if show_popup("Continue", "Do you want to import contacts to Google Contacts?"):
        # Check if contacts.csv exists
        if not check_file_exists("contacts.csv"):
            show_popup("Error", "Please run new.py first to generate contacts.csv!")
            return
            
        # Proceed with import
        if import_to_google_contacts():
            show_popup("Success", "Contacts imported successfully! You can now proceed with WhatsApp automation.")
        else:
            show_popup("Error", "Failed to import contacts. Please try again.")
    else:
        show_popup("Information", "Operation cancelled by user.")

if __name__ == "__main__":
    main()