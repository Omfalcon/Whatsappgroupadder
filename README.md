# WhatsApp Group Auto Adder | Bulk WhatsApp Member Adder

Easily automate adding members to WhatsApp groups using **Selenium**. This tool extracts phone numbers from a text file, formats them correctly, and adds them to a specified WhatsApp group. Ideal for **college clubs, businesses, and community management**, ensuring a seamless bulk-adding process.

---

## 📌 Features

✅ **Automated Bulk Member Addition** – Add multiple contacts in one go.  
✅ **Error Handling** – Prevents crashes by freezing for 2 minutes if an error occurs.  
✅ **Lightweight & Fast** – Runs smoothly with minimal setup.  
✅ **Fully Automated** – Once started, the script does everything on its own.  

---

## 🚀 How to Use (Step-by-Step)

### **1️⃣ Prepare Contacts (`contacts.txt`)**

- Extract the **contact column** from your Excel file.
- Paste it into a new file and **save it as `contacts.txt`**.
- Ensure the file contains only **phone numbers**, one per line.
- Save it in the **same folder** as this script.

### **2️⃣ Set the WhatsApp Group Name**

- Open the script and edit the group name directly in the code.
- Save the file.

### **3️⃣ Run the Script**

- Open the terminal and navigate to the script folder.
- Run the following command:
  ```bash
  python script.py
  ```
- **Scan the WhatsApp QR code** when prompted.
- Once scanned, **press Enter in the terminal** to start the process.

### **4️⃣ Let the Script Work Automatically**

- It will read `contacts.txt`, add `91` before every number, and add them to the specified group.
- **Ensure you are the admin** and have permission to add members.

---

## 🛠 Prerequisites

- Install **Google Chrome** and **ChromeDriver**.
- Install **Python 3.7+**.
- Install required dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

---

## ❗ Important Notes

- **You must manually extract the contact column from Excel** and save it as `contacts.txt`.
- **The script will automatically add `+91` before each number**.
- If an error occurs, **the script will freeze for 2 minutes** instead of crashing.
- You **must be an admin** to add members.

---

🚀 **Optimized for WhatsApp Bulk Adding | Automate Your WhatsApp Groups Now!**

