from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os
import sys
sys.stdout.reconfigure(line_buffering=True)

print("🚀 Bot started", flush=True)

# Run every 20 minutes forever
while True:
    chrome_options = Options()
    
   
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # disable GPU hardware acceleration
    chrome_options.add_argument("--remote-debugging-port=9222")  # enables DevTools listening on this port
    chrome_options.add_argument("--disable-software-rasterizer")  
    chrome_options.binary_location = "/usr/bin/google-chrome"

    service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open initial page to set cookies
        driver.get("https://lemehost.com/")
        time.sleep(2)

        # Inject all required cookies
        cookies = [
            {
                'name': 'cf_clearance',
                'value': os.environ.get("LEME_CF_CLEARANCE"),
                'domain': 'lemehost.com',
                'path': '/',
            },
            {
                'name': 'advanced-frontend',
                'value': os.environ.get("LEME_ADVANCED_FRONTEND"),
                'domain': 'lemehost.com',
                'path': '/',
            },
            {
                'name': '_identity-frontend',
                'value': os.environ.get("LEME_IDENTITY_FRONTEND"),
                'domain': 'lemehost.com',
                'path': '/',
            },
        ]

        for cookie in cookies:
            driver.add_cookie(cookie)

        # Go to the server page directly
        driver.get("https://lemehost.com/server/3057073/free_plan")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))


        

        print("----- PAGE SOURCE START -----")
        print(driver.page_source)
        print("----- PAGE SOURCE END -----")


        # Click the "Extend time" button
        extend_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class, 'btn-primary') and contains(., 'Extend time')]")
            )
        )
        extend_button.click()
        print("✅ Clicked Extend Time at", time.strftime('%Y-%m-%d %H:%M:%S'))
    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()

    # Wait 20 minutes before next run
    time.sleep(20 * 60)
