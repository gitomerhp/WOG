import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

# setup chrome
opt = webdriver.ChromeOptions()
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)


def test_scores_service(app_url):
    """
    get the application URL as an input,
    open a browser to that URL,
    select the score element in our web page and check that it is a number between 1 to 1000
    and return a boolean value if it is true or not
    """

    driver.get(app_url)

    try:
        # check if server is running
        response = requests.get(app_url, timeout=3)
        response.raise_for_status()
        score = driver.find_element(By.ID, "score").text
        if 1 <= int(score) <= 1000:
            return True
        else:
            return False

    except requests.RequestException:
        print("Server is not running or unreachable.")
        return False

    # Handle the case where the element is not found on the page
    except NoSuchElementException:
        print("Element not found on the page.")
        return False

    except Exception as e:
        print(f"something went wrong: {e}")
        return False


def main_function():
    """call our tests function,
     and return -1 as an OS exit code if the tests failed and 0 if they passed"""

    APP_URL = "http://127.0.0.1:5000/"
    if test_scores_service(APP_URL):
        return 0
    else:
        return -1


print(main_function())
