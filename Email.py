from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import smtplib as smtp
import chromedriver_binary



# Set up the browser options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('log-level=3')



# Set up the browser
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options, )
# Navigate to the marketplace site
driver.get("https://www.marktplaats.nl/cp/91/auto-kopen/")
time.sleep(8)
driver.find_element(By.XPATH, '//*[@id="cars-search-form-root"]/article[2]/section/section/form/div[1]/div[3]/div/button[2]').click()

# Set the brand 
print('All the brands:')
for i in range(1, 100):
    try:
        brand = driver.find_element(By.XPATH, f'//*[@id="l2CategoryId"]/optgroup[2]/option[{i}]')
        print(f"[{i}]. {brand.text}")
    except:
        break
print('\n')
brand_num = input('Select the brand number: ')
driver.find_element(By.XPATH, f'//*[@id="l2CategoryId"]/optgroup[2]/option[{brand_num}]').click()
time.sleep(5)


# Set the model
print('\n \n')
print('All the Models:')
for i in range(2, 150):
    try:
        model = driver.find_element(By.XPATH, f'//*[@id="model"]/option[{i}]')
        print(f"[{i}]. {model.text}")
    except:
        break
print('\n')
model_num = input('Select the Model number: ')
driver.find_element(By.XPATH, f'//*[@id="model"]/option[{model_num}]').click()
time.sleep(3)

# Set the fuel
print('\n \n')
print('All the Fuel list:')
for i in range(2, 10):
    try:
        fuel = driver.find_element(By.XPATH, f'//*[@id="fuel"]/option[{i}]')
        print(f"[{i}]. {fuel.text}")
    except:
        break
print('\n')
fuel_num = input('Select the Fuel number: ')
driver.find_element(By.XPATH, f'//*[@id="fuel"]/option[{fuel_num}]').click()
time.sleep(3)


# Set the price
print('\n \n')
print('All the Prices list:')
for i in range(2, 200):
    try:
        price = driver.find_element(By.XPATH, f'//*[@id="PriceCents.to"]/option[{i}]')
        print(f"[{i}]. {price.text}")
    except:
        break
print('\n')
price_num = input('Select the Price number: ')
driver.find_element(By.XPATH, f'//*[@id="PriceCents.to"]/option[{price_num}]').click()
time.sleep(3)


# Set the Construction Year
print('\n \n')
print('All the Construction years:')
for i in range(2, 200):
    try:
        year = driver.find_element(By.XPATH, f'//*[@id="constructionYear.from"]/option[{i}]')
        print(f"[{i}]. {year.text}")
    except:
        break
print('\n')
year_num = input('Select the Year of construction number: ')
driver.find_element(By.XPATH, f'//*[@id="constructionYear.from"]/option[{year_num}]').click()
time.sleep(3)


# Click on search button after selecting all the filters
driver.find_element(By.XPATH, '//*[@type="submit"]').click()
time.sleep(10)


# Select the transmision
print('\n \n')
print('All the Transmission list:')
print('[1]. Automatic Transmission')
print('[2]. Manual Transmission')
print('\n')
transmission_num = input('Select the transmission number: ')
if '1' in transmission_num:
    driver.find_element(By.XPATH, '//*[@id="transmission-Automaat"]').click()
else:
    driver.find_element(By.XPATH, '//*[@id="transmission-Handgeschakeld"]').click()


# Select the range/milage
print('\n \n')
print('All the Milage:')
for i in range(2, 200):
    try:
        year_milage = driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/main/div/aside/div[1]/div[1]/div/div/div[7]/div[2]/div[2]/div/select/option[{i}]')
        print(f"[{i}]. {year_milage.text}")
    except Exception as e:
        break
print('\n')
year_milage_num = input('Select the Milage number: ')
driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/main/div/aside/div[1]/div[1]/div/div/div[7]/div[2]/div[2]/div/select/option[{year_milage_num}]').click()
time.sleep(8)



email = 'Put the recieving Email here'





def send_notification(email, message):

    connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
    email_addr = 'Put sending email address here.'
    email_passwd = 'put the password here'
    connection.login(email_addr, email_passwd)
    connection.sendmail(from_addr=email_addr, to_addrs=email, msg=message)
    connection.close()


send_notification(email=email, message= "This is just a demo email for notifications of new car ad, please ignore.")
while True:
    # Get the current ads
    old_ads = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[3]/ul[1]/li[1]/a[1]/div[2]/div[1]/h3[1]').text
    print(old_ads)

    # Refresh the page
    driver.refresh()
    time.sleep(3)
    link_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div/div[3]/ul/li[1]/a')
    link = link_element.get_attribute("href")
    print(link)
    # Get the new ads
    new_ads = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[3]/ul[1]/li[1]/a[1]/div[2]/div[1]/h3[1]').text
    print(new_ads)
    if old_ads  == new_ads:
        print('\n \nNo new ad found. Please wait i will check again in 10 minutes.\n \n')
        time.sleep(600)
        continue
    else:
        print("New ad found: " + link)
        send_notification(email, f"Check the marketplace site for new ads!\n new ad link is:{link}")