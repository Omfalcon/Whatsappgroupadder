import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import tkinter as tk
from tkinter import messagebox
import os
import time

class ContactImporter:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def create_driver(self):
        options = uc.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-notifications')
        
        try:
            self.driver = uc.Chrome(version_main=136, options=options, use_subprocess=True)
            self.wait = WebDriverWait(self.driver, 20)
            return True
        except Exception as e:
            print(f"Failed to start Chrome: {e}")
            return False
    
    def import_contacts(self):
        if not self.create_driver():
            return False
            
        try:
            self.driver.get("https://contacts.google.com/")
            input("Sign in to Google Contacts and press Enter to continue...")
            
            import_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "d5NbRd-EScbFb-JIbuQc.dgqZp"))
            )
            import_button.click()
            time.sleep(2)
            
            select_file_button = self.wait.until(
                EC.element_to_be_clickable((
                    By.CLASS_NAME, "UywwFc-LgbsSe.UywwFc-LgbsSe-OWXEXe-dgl2Hf.UywwFc-StrnGf-YYd4I-VtOx3e.UywwFc-kSE8rc-FoKg4d-sLO9V-YoZ4jf"
                ))
            )
            
            file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(os.path.abspath("contacts.csv"))
            time.sleep(2)
            
            final_import_button = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, "//button[contains(@class, 'mUIrbf-LgbsSe') and .//span[text()='Import']]"
                ))
            )
            final_import_button.click()
            time.sleep(5)
            return True
            
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            input("Press Enter to close the browser...")
            self.driver.quit()

def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askyesno(title, message)
    root.destroy()
    return response

def main():
    if not os.path.exists("number.txt"):
        show_popup("Error", "Please create number.txt file first!")
        return
    
    if show_popup("Continue", "Do you want to import contacts to Google Contacts?"):
        if not os.path.exists("contacts.csv"):
            show_popup("Error", "Please run new.py first to generate contacts.csv!")
            return
            
        importer = ContactImporter()
        if importer.import_contacts():
            show_popup("Success", "Contacts imported successfully!")
        else:
            show_popup("Error", "Failed to import contacts. Please try again.")

if __name__ == "__main__":
    main()