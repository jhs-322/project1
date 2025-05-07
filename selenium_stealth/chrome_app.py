# from pathlib import Path
# from .wrapper import evaluateOnNewDocument
# from selenium.webdriver import Chrome as Driver


# def chrome_app(driver: Driver, **kwargs) -> None:
#     evaluateOnNewDocument(
#         driver, Path(__file__).parent.joinpath("js/chrome.app.js").read_text()
#     )

from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .resource_loader import resource_path

def chrome_app(driver: Driver, **kwargs) -> None:
    js_path = resource_path("selenium_stealth/js/chrome.app.js")
    evaluateOnNewDocument(
        driver, open(js_path, encoding="utf-8").read()
    )