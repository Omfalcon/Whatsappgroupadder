from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    input("Scan QR code and press Enter to continue...")

    # Search for the group
    group_name = input("Enter the group name: ") #Replace this with your group name
    search_box = driver.find_element(By.CLASS_NAME, "selectable-text.copyable-text.x15bjb6t.x1n2onr6")
    search_box.send_keys(group_name)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)

    # Click to open Group Info
    time.sleep(3)  # Wait a bit longer
    try:
        # Try the exact header class first
        group_info = driver.find_element(By.CLASS_NAME, "x1n2onr6.x9f619.x78zum5.x6s0dn4.xh8yej3.x7j6532.x1pl83jw.x1j6awrg.x1te75w5.x162n7g1.x4eaejv.xcock1l.x1s928wv.xl9llhp.x1qj619r.x1r9ni5o.xvkby78.x42zw1d.x889kno.x1a8lsjc.xf7dkkf.xv54qhq.xu306ak.x1h1zc6f")
    except:
        try:
            # Try to find the div with title "Profile details"
            group_info = driver.find_element(By.CSS_SELECTOR, 'div[title="Profile details"][role="button"]')
        except:
            try:
                # Try finding the group name span
                group_info = driver.find_element(By.CSS_SELECTOR, 'span[dir="auto"][class*="_ao3e"]')
                # Click its parent div to open group info
                group_info = group_info.find_element(By.XPATH, "../../../..")
            except:
                # Last resort: try the header with partial class match
                group_info = driver.find_element(By.CSS_SELECTOR, 'header[class*="x1n2onr6"][class*="x78zum5"]')
    
    group_info.click()
    time.sleep(2)  # Wait after clicking

    # Click the "Add Member" option
    time.sleep(2)
    add_option = driver.find_element(By.CLASS_NAME, "_ak72.false._ak73._ak76._ak77")
    add_option.click()

    # Read contacts from file
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    # Add members
    for contact in contacts:
        contact = contact.strip()
        contact = "91" + contact  # Always add 91, no condition

        number_input = driver.find_element(By.CLASS_NAME, "selectable-text.copyable-text.x15bjb6t.x1n2onr6")
        number_input.send_keys(contact)
        time.sleep(1)
        number_input.send_keys(Keys.ENTER)
        time.sleep(2)

        # Click to confirm addition
        print("Waiting for confirm button...")
        time.sleep(4)
        try:
            # Wait for any element with checkmark-medium icon
            wait = WebDriverWait(driver, 10)
            confirm_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-icon="checkmark-medium"]'))
            )
            print("Found confirm button, clicking...")
            confirm_button.click()
        except Exception as e:
            print(f"Error finding confirm button: {str(e)}")
            print("Trying alternative method...")
            try:
                # Try finding parent div of checkmark
                buttons = driver.find_elements(By.TAG_NAME, "div")
                for button in buttons:
                    try:
                        if button.get_attribute("role") == "button" and "checkmark-medium" in button.get_attribute("innerHTML"):
                            print("Found confirm button through alternative method, clicking...")
                            button.click()
                            break
                    except:
                        continue
            except Exception as e:
                print(f"Alternative method also failed: {str(e)}")

        # Click the final button
        print("\nWaiting for Add member button...")
        time.sleep(4)
        try:
            # Wait for button containing "Add member" text
            wait = WebDriverWait(driver, 10)
            final_button = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Add member')]/ancestor::button"))
            )
            print("Found Add member button, clicking...")
            final_button.click()
        except Exception as e:
            print(f"Error finding Add member button: {str(e)}")
            print("Trying alternative method...")
            try:
                # Try finding any button with Add member text
                buttons = driver.find_elements(By.TAG_NAME, "button")
                for button in buttons:
                    try:
                        if "Add member" in button.text:
                            print("Found Add member button through alternative method, clicking...")
                            button.click()
                            break
                    except:
                        continue
            except Exception as e:
                print(f"Alternative method also failed: {str(e)}")

        print("\nWaiting for process to complete...")

    # Wait for process to complete
    time.sleep(360)

    print("All members added successfully!")

except Exception as e:
    print("Error occurred")  # Generic error message
    time.sleep(120)  # Freeze execution for 2 minutes (120 seconds)

finally:
    driver.quit()