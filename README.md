# WhatsApp Group Member Adder 🚀

Easily automate adding members to WhatsApp groups using **Selenium**. This tool extracts phone numbers from a text file, formats them correctly, and adds them to a specified WhatsApp group. Ideal for **college clubs, businesses, and community management**, ensuring a seamless bulk-adding process.

## Features ✨

- 📱 Automatically add multiple contacts to WhatsApp groups
- 📊 Google Contacts integration for better contact management
- 🔄 Robust error handling and fallback methods
- 💪 Reliable button detection and clicking
- 🎯 Easy to use interface

## Step-by-Step Installation Guide 📥

### Step 1: Install Python
1. Go to [Python Download Page](https://www.python.org/downloads/)
2. Click on "Download Python 3.8" or newer
3. Run the downloaded file
4. **IMPORTANT**: Check ✅ "Add Python to PATH" during installation
5. Click "Install Now"

### Step 2: Install Visual Studio Code (VSCode)
1. Go to [VSCode Download Page](https://code.visualstudio.com/download)
2. Click on "Windows" download button
3. Run the downloaded file
4. Follow the installation steps (use all default options)

### Step 3: Download & Setup This Tool

#### Option A: Using GitHub (For Advanced Users)
1. Clone this repository:
```bash
git clone https://github.com/yourusername/whatsapp-group-adder.git
cd whatsapp-group-adder
```

#### Option B: Direct Download (Recommended for Beginners)
1. Download the Tool:
   - Click the green "Code" button above
   - Select "Download ZIP"
   - Wait for download to complete

2. Extract Files:
   - Find the downloaded ZIP file (usually in Downloads folder)
   - Right-click on it
   - Select "Extract All"
   - Choose "Desktop" as the destination
   - Click "Extract"

3. Setup in VSCode:
   - Open VSCode (installed in Step 2)
   - Click "File" in the top menu
   - Click "Open Folder"
   - Navigate to Desktop
   - Select the "WhatsAppGroupAdder" folder
   - Click "Select Folder"
   - If asked "Do you trust the authors?", click "Yes"

4. Prepare Files:
   - In VSCode's file explorer (left side), you should see:
     - `main.py`
     - `whatsappadder.py`
     - `contactmaker.py`
     - `requirements.txt`
     - `contacts.txt`
   - If any file is missing, make sure you extracted correctly

### Step 4: Install Required Packages
1. In VSCode:
   - Press Ctrl + ` (backtick key, under Esc) to open terminal
   - The terminal will open at the bottom
   - Type or copy-paste this command:
   ```
   pip install -r requirements.txt
   ```
   - Press Enter and wait for installation to complete

## How to Use 📱

### Before Starting:
1. Edit a file named `contacts.txt` in the tool folder
2. Add phone numbers in this format (one per line):
```
9876543210
9876543211
9876543212
```
Note: Don't add +91 or 0 before numbers, the tool will handle it automatically

### Method 1: Complete Process (Recommended)
1. In VSCode:
   - Find `main.py` in the file explorer on the left
   - Right-click on it
   - Select "Run Python File in Terminal"
2. Follow the on-screen steps:
   - Sign in to your Google account when Chrome opens
   - Scan WhatsApp QR code when shown
   - Type your group name when asked
   - Let the tool do its work!

### Method 2: Direct WhatsApp Addition
1. In VSCode:
   - Find `whatsappadder.py` in the file explorer on the left
   - Right-click on it
   - Select "Run Python File in Terminal"
2. Follow the on-screen steps:
   - Scan WhatsApp QR code when shown
   - Type your group name when asked
   - Let the tool do its work!

## Important Things to Remember ⚠️

1. Make sure you're a group admin in the WhatsApp group
2. Don't add country code in contacts.txt (no +91 or 0)
3. Keep Chrome browser updated to version 136 or newer
4. Keep your internet connection stable

## Common Problems & Solutions 🔧

### "Button not clicking" or "Element not found":
- Keep the Chrome window visible on screen
- Update Chrome to version 136 or newer

### "Contacts not being added":
- Check if numbers in contacts.txt are correct
- Make sure there are no spaces or extra characters
- Verify that you're a group admin

### "Google Contacts issues":
- Make sure you're logged into your Google account
- Check if you have permission to add contacts

## Need Help? 💬

If something's not working:

1. Check the "Common Problems & Solutions" section above
2. Make sure you followed all steps in order
3. Verify that all files are in the correct folder
4. Make sure Chrome is updated to version 136 or change the chrome version in the code according to your version
5. Raise the issue i will help you out 

## License 📄

This project is free to use - see the LICENSE file for details.

