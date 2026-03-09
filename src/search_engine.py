
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def start_driver():

    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    service = Service("chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)

    return driver

def google_search(domain):
    """
    Search Google and return first result URL
    """

    query = domain + " company"

    driver = start_driver()

    driver.get("https://www.google.com")

    time.sleep(2)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.submit()

    time.sleep(3)

    results = driver.find_elements(By.CSS_SELECTOR, "div.g")

    first_link = None

    for result in results:
        try:
            link = result.find_element(By.TAG_NAME, "a").get_attribute("href")

            if link and "google" not in link:
                first_link = link
                break
        except:
            continue

    driver.quit()

    return first_link


def google_company_description(domain):
    """
    Extract company description from Google snippets
    """

    query = domain + " company"

    driver = start_driver()

    try:
       driver.get("https://www.google.com")
    except: 
          driver.quit()
          return ""  

    time.sleep(2)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.submit()

    time.sleep(3)

    snippets = driver.find_elements(By.CSS_SELECTOR, "div.VwiC3b")

    text = ""

    for s in snippets[:3]:
        text += s.text + " "

    driver.quit()

    return text


def detect_affiliation(domain):
    """
    Detect if domain belongs to university or company
    """

    if ".ac." in domain or ".edu" in domain:
        return "University"

    return "Company"