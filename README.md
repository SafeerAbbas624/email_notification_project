# Email Notification on new car ad.
This Python script automates the process of searching for new car ads on the Dutch marketplace website Marktplaats using Selenium. It sets up the browser, navigates to the website, selects car filters, and continuously checks for new ads. If a new ad is found, it sends a notification email. You can set the filters as per your demand. this is the website it works on [link]( https://www.marktplaats.nl/cp/91/auto-kopen/)

## Installation
To install and run this script, you'll need to have Python and the necessary libraries installed on your system. Follow these steps:


- Install Python: Download and install the latest version of Python from the official website (https://www.python.org/downloads/).

- Install Selenium: Open a terminal or command prompt and run the following command to install Selenium:
```python
pip install selenium
```
- Install Chromedriver: Download the latest version of Chromedriver from the official website (https://chromedriver.chromium.org/downloads) and extract the executable file to a same directory of this project.

- download this project from [here](https://github.com/SafeerAbbas624/email_notification_project/archive/refs/heads/main.zip).

- Replace the placeholders in the code with your actual email addresses and password. edit them with you emails
```python
email = 'Put the recieving Email here'

  email_addr = 'Put sending email address here.'
  email_passwd = 'put the password here'
```
- Save the file.


## Running the Script
To run the script, open a terminal or command prompt, navigate to the directory where you saved the project file, and run the following command:
```bash
python Email.py
```
OR 
```bash
python3 Email.py
```

The script will start running and will display the current and new ad titles as it checks for new ads. If a new ad is found, it will send an email notification.

## Compatibility
This script has been tested on macOS and Windows systems. It should work on any system that has Python and the required libraries installed.

Please note that you may need to adjust the code or install additional libraries based on your specific requirements and system configuration.
