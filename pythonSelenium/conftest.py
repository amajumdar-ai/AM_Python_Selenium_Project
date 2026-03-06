import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Instantiate the browser"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name").lower()
    if browser_name == "chrome":
        service_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"{browser_name} is not supported")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs['browserInstance']
        screenshot = driver.get_screenshot_as_base64()

        extra.append(pytest_html.extras.image(screenshot, "Screenshot"))

    report.extra = extra

