from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    input("Scan QR code and press Enter to continue...")

    # Search for the group
    group_name = "Enter the group name" #Replace this with your group name
    search_box = driver.find_element(By.CLASS_NAME, "selectable-text.copyable-text.x15bjb6t.x1n2onr6")
    search_box.send_keys(group_name)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)

    # Click to open Group Info
    time.sleep(2)
    group_info = driver.find_element(By.CLASS_NAME, "x1n2onr6.xfo81ep.x9f619.x78zum5.x6s0dn4.xh8yej3.x7j6532.x1pl83jw.x1j6awrg.x1te75w5.x162n7g1.x4eaejv.xcock1l.x1s928wv.xl9llhp.x1qj619r.x1r9ni5o.xvkby78.x889kno.x1a8lsjc.x1swvt13.x1pi30zi.xu306ak.x1h1zc6f")
    group_info.click()

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
        time.sleep(1)

    # Click to confirm addition
    confirm_button = driver.find_element(By.CLASS_NAME, "x78zum5.x6s0dn4.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1f6kntn.xk50ysn.x7o08j2.xtvhhri.x1rluvsa.x14yjl9h.xudhj91.x18nykt9.xww2gxu.xu306ak.x12s1jxh.xkdsq27.xwwtwea.x1gfkgh9.x1247r65.xng8ra")
    confirm_button.click()

    # Click the final button
    time.sleep(2)
    final_button = driver.find_element(By.CLASS_NAME, "x889kno.x1a8lsjc.xbbxn1n.xxbr6pl.x1n2onr6.x1rg5ohu.xk50ysn.x1f6kntn.xyesn5m.x1z11no5.xjy5m1g.x1mnwbp6.x4pb5v6.x178xt8z.xm81vs4.xso031l.xy80clv.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1v8p93f.xogb00i.x16stqrj.x1ftr3km.x1hl8ikr.xfagghw.x9dyr19.x9lcvmn.xbtce8p.x14v0smp.xo8ufso.xcjl5na.x1k3x3db.xuxw1ft.xv52azi")
    final_button.click()

    # Wait for process to complete
    time.sleep(360)

    print("All members added successfully!")

except Exception as e:
    print("Error occurred")  # Generic error message
    time.sleep(120)  # Freeze execution for 2 minutes (120 seconds)

finally:
    driver.quit()
