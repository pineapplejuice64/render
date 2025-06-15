from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os

print("🚀 Login bot started")

while True:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.binary_location = "/usr/bin/google-chrome"
    service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://lemehost.com/")
        time.sleep(2)

        # Set login cookies
        for name in ['cf_clearance', 'advanced-frontend', '_identity-frontend']:
            value = os.environ.get(f"LEME_{name.upper().replace('-', '_')}")
            if value:
                driver.add_cookie({
                    'name': name,
                    'value': value,
                    'domain': '.lemehost.com',
                    'path': '/',
                })

        driver.refresh()
        time.sleep(2)
        print("✅ Logged in at", time.strftime('%Y-%m-%d %H:%M:%S'))

    except Exception as e:
        print("❌ Error during login:", e)

    finally:
        driver.quit()

    time.sleep(10 * 60)  # Wait 10 minutes
